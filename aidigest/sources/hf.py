"""HuggingFace Daily Papers —— 社区票选，用来抓「正在被讨论」的趋势。"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta, timezone

from ..models import Item, make_uid
from ..util import fetch, parse_dt

log = logging.getLogger("aidigest.hf")
API = "https://huggingface.co/api/daily_papers"


def _to_item(d: dict) -> Item | None:
    p = d.get("paper") or d
    aid = p.get("id") or ""
    title = " ".join((p.get("title") or "").split())
    if not aid or not title:
        return None
    authors = []
    for a in p.get("authors") or []:
        n = a.get("name") if isinstance(a, dict) else str(a)
        if n:
            authors.append(" ".join(n.split()))
    return Item(
        uid=make_uid("arxiv", aid),           # 和 arXiv 共用 uid，天然去重
        source="hf",
        title=title,
        url=f"https://arxiv.org/abs/{aid}",
        published=parse_dt(p.get("publishedAt") or d.get("publishedAt") or ""),
        abstract=" ".join((p.get("summary") or "").split()),
        authors=authors,
        venue="HF Daily Papers",
        upvotes=int(p.get("upvotes") or 0),
        extra={"arxiv_id": aid, "hf_url": f"https://huggingface.co/papers/{aid}"},
    )


def fetch_hf_papers(cfg) -> tuple[list[Item], list[str]]:
    conf = cfg.sources.get("hf_papers", {})
    errors: list[str] = []
    if not conf.get("enabled", True):
        return [], []

    win = int(conf.get("window_days", 3))
    min_up = int(conf.get("min_upvotes", 0))
    now = datetime.now(timezone.utc)
    out: dict[str, Item] = {}

    for k in range(win + 1):
        day = (now - timedelta(days=k)).strftime("%Y-%m-%d")
        raw = fetch(API, params={"date": day}, timeout=30.0)
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            errors.append(f"HF Daily Papers {day} 返回非 JSON")
            continue
        for d in data if isinstance(data, list) else []:
            it = _to_item(d)
            if it and it.upvotes >= min_up:
                prev = out.get(it.uid)
                if not prev or it.upvotes > prev.upvotes:
                    out[it.uid] = it

    if not out:
        errors.append("HF Daily Papers 未取到任何条目")
    log.info("hf: %d items", len(out))
    return list(out.values()), errors
