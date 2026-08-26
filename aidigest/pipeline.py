"""一轮完整的抓取 → 分类 → 打分 → 摘要 → 渲染。"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from .classify import Classifier
from .config import Config
from .models import Item, item_from_dict, item_to_dict
from .render import render_digest
from .score import Scorer
from .sources import fetch_arxiv, fetch_hf_papers, fetch_pagewatch, fetch_rss
from .state import State
from .summarize import has_credentials, summarize

log = logging.getLogger("aidigest")


def _merge(items: list[Item]) -> list[Item]:
    """同一 uid 的多个来源合并（HF 的票数 + arXiv 的摘要/作者）。"""
    merged: dict[str, Item] = {}
    for it in items:
        cur = merged.get(it.uid)
        if cur is None:
            merged[it.uid] = it
            continue
        # 以信息量大的为主体
        base, other = (cur, it) if len(cur.abstract) >= len(it.abstract) else (it, cur)
        base.upvotes = max(cur.upvotes, it.upvotes)
        if not base.authors:
            base.authors = other.authors
        if not base.categories:
            base.categories = other.categories
        if not base.lab:
            base.lab = other.lab
        base.extra.update({k: v for k, v in other.extra.items() if k not in base.extra})
        if base.source != other.source:
            base.extra.setdefault("also_in", []).append(other.source)
        merged[it.uid] = base
    return list(merged.values())


def collect(cfg: Config, state: State, *, mode: str, author_window_days: int | None = None,
            sources: set[str] | None = None, persist: bool = True) -> tuple[list[Item], list[str]]:
    raw: list[Item] = []
    errors: list[str] = []
    want = sources or {"arxiv", "hf", "rss", "pagewatch"}

    if "arxiv" in want:
        got, err = fetch_arxiv(cfg, author_window_days=author_window_days)
        raw += got
        errors += err
    if "hf" in want:
        got, err = fetch_hf_papers(cfg)
        raw += got
        errors += err
    if "rss" in want:
        got, err = fetch_rss(cfg)
        raw += got
        errors += err
    if "pagewatch" in want:
        got, err = fetch_pagewatch(cfg, state, report_on_init=(mode == "backfill"),
                                   persist=persist)
        raw += got
        errors += err

    return _merge(raw), errors


def _select(cfg: Config, candidates: list[Item], limit: int | None,
            mode: str = "daily") -> tuple[list[Item], int]:
    """按分数取，但每个领域不超过上限、总数不超过上限。返回 (选中, 积压数)。"""
    out_cfg = cfg.main.get("output", {})
    if mode == "backfill" and not limit:
        # 补课是一次性归档，不该被日常容量限制截断
        return list(candidates), 0
    per_topic = int(out_cfg.get("max_items_per_topic", 8))
    max_total = limit or int(out_cfg.get("max_items_total", 60))
    reserve = out_cfg.get("reserve") or {}

    picked: list[Item] = []
    chosen: set[str] = set()

    # 第一轮：先把预留名额发给弱势来源（博客、页面更新、HF 热榜）
    max_venue = int(out_cfg.get("max_per_venue", 2))
    for src, n in reserve.items():
        taken = 0
        per_venue: dict[str, int] = {}
        for it in candidates:
            if taken >= n or len(picked) >= max_total:
                break
            if it.source != src or it.uid in chosen:
                continue
            # HF 热榜天然只有一个 venue，不该受 venue 上限限制
            v = it.venue or "?"
            if src != "hf" and per_venue.get(v, 0) >= max_venue:
                continue    # 单个高产 feed 不许把预留名额吃光
            per_venue[v] = per_venue.get(v, 0) + 1
            picked.append(it)
            chosen.add(it.uid)
            taken += 1

    # 第二轮：剩下的名额按分数填，受单领域配额限制
    per: dict[str, int] = {}
    for it in picked:
        per[it.primary_topic] = per.get(it.primary_topic, 0) + 1
    for it in candidates:
        if len(picked) >= max_total:
            break
        if it.uid in chosen:
            continue
        t = it.primary_topic
        # 关注名单命中的条目不受单领域配额挤出
        if per.get(t, 0) >= per_topic and not it.author_hits:
            continue
        per[t] = per.get(t, 0) + 1
        picked.append(it)
        chosen.add(it.uid)

    picked.sort(key=lambda i: -i.score)
    return picked, len(candidates) - len(picked)


def _raw_cache_path(cfg: Config) -> Path:
    return cfg.db_path.parent / "last_raw.json"


def run(cfg: Config, *, mode: str = "daily", use_llm: bool = True, dry_run: bool = False,
        author_window_days: int | None = None, limit: int | None = None,
        sources: set[str] | None = None, date: str | None = None,
        from_raw: bool = False) -> tuple[str, dict]:
    state = State(cfg.db_path)
    classifier = Classifier(cfg)
    scorer = Scorer(cfg)

    cache = _raw_cache_path(cfg)
    if from_raw:
        if not cache.exists():
            raise SystemExit(f"没有原始数据缓存：{cache}（先正常跑一次 run）")
        items = [item_from_dict(d) for d in json.loads(cache.read_text("utf-8"))]
        errors = ["使用了 --from-raw 缓存，本轮未联网抓取"]
        log.info("loaded %d items from raw cache", len(items))
    else:
        items, errors = collect(cfg, state, mode=mode, author_window_days=author_window_days,
                                sources=sources, persist=not dry_run)
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps([item_to_dict(i) for i in items], ensure_ascii=False),
                         encoding="utf-8")
    n_fetched = len(items)
    log.info("collected %d unique items", n_fetched)

    resurface_delta = int(cfg.sources.get("hf_papers", {}).get("resurface_upvote_delta", 40))

    candidates: list[Item] = []
    for it in items:
        already = state.is_reported(it.uid)
        if already:
            # 已经推过 —— 只有热度显著上涨才重新浮出
            prev = state.upvotes_of(it.uid)
            if it.upvotes and it.upvotes - prev >= resurface_delta:
                it.is_resurfaced = True
                it.is_new = False
            else:
                state.record_seen(it)   # 更新票数，但不进 digest
                continue
        classifier.classify(it)
        scorer.score(it)
        if scorer.keep(it):
            candidates.append(it)

    candidates.sort(key=lambda i: -i.score)

    # 只保留真正会出现在简报里的条目。没被选中的**不记为已推送**，
    # 于是它们会自然排进后面几天 —— 首次运行捞出几百篇时不会被静默吞掉。
    selected, backlog = _select(cfg, candidates, limit, mode)

    llm_status = "off"
    if use_llm and cfg.main.get("llm", {}).get("enabled", True):
        if has_credentials():
            selected, llm_errors = summarize(cfg, selected)
            errors += llm_errors
            llm_status = cfg.main["llm"].get("model", "claude-opus-5")
        else:
            llm_status = "off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）"

    date = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    meta = {
        "date": date,
        "n_fetched": n_fetched,
        "errors": errors,
        "mode": mode,
        "llm": llm_status,
        "backlog": backlog,
    }
    md = render_digest(cfg, selected, meta)

    if not dry_run:
        for it in selected:
            state.record_seen(it, reported_on=date)
        state.log_run(mode, n_fetched, len(selected), "; ".join(errors[:5]))

    meta["n_selected"] = len(selected)
    meta["items"] = selected
    state.close()
    return md, meta
