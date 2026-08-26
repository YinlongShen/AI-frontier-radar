"""实验室 / 个人博客 RSS。论文之外，很多想法首发在博客上。"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

import feedparser

from ..models import Item, make_uid
from ..util import fetch, truncate

log = logging.getLogger("aidigest.rss")


def _entry_dt(e) -> datetime:
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(e, key, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def fetch_rss(cfg) -> tuple[list[Item], list[str]]:
    conf = cfg.sources.get("rss", {})
    errors: list[str] = []
    if not conf.get("enabled", True):
        return [], []

    win = int(conf.get("window_days", 7))
    cutoff = datetime.now(timezone.utc) - timedelta(days=win)
    items: list[Item] = []

    for feed in conf.get("feeds", []):
        name, url = feed.get("name", "?"), feed.get("url", "")
        # 注意：feedparser.parse(url) 自己发请求且**没有超时**，挂起的 feed 会拖死整轮。
        # 一律先用带超时的 httpx 取回文本，再交给 feedparser 解析。
        raw = fetch(url, timeout=20.0, retries=1)
        if raw is None:
            errors.append(f"RSS {name}: 抓取失败 ({url})")
            continue
        try:
            parsed = feedparser.parse(raw)
        except Exception as e:  # noqa: BLE001
            errors.append(f"RSS {name}: 解析失败 {e}")
            continue
        entries = getattr(parsed, "entries", []) or []
        if not entries:
            errors.append(f"RSS {name}: 无条目（feed 可能已失效: {url}）")
            continue
        n = 0
        for e in entries:
            dt = _entry_dt(e)
            if dt < cutoff:
                continue
            link = getattr(e, "link", "") or ""
            title = " ".join((getattr(e, "title", "") or "").split())
            if not link or not title:
                continue
            body = getattr(e, "summary", "") or ""
            if hasattr(e, "content") and e.content:
                body = e.content[0].get("value", body)
            import re as _re
            body = _re.sub(r"<[^>]+>", " ", body)
            items.append(
                Item(
                    uid=make_uid("rss", link),
                    source="rss",
                    title=title,
                    url=link,
                    published=dt,
                    abstract=truncate(body, 1500),
                    venue=name,
                    lab=feed.get("lab", ""),
                    authors=[getattr(e, "author", "")] if getattr(e, "author", "") else [],
                )
            )
            n += 1
        log.info("rss %s: %d items", name, n)

    return items, errors
