"""arXiv API 源。

两种扫描模式：
  1. 分类扫描 —— 近 N 天 cs.AI/cs.LG/... 的新论文（量大，靠打分过滤）
  2. 作者扫描 —— watchlist 作者近 180 天的所有论文（量小，全部保留）

模式 2 是「几个月前的重要论文现在才看到」的解药：只要还没推送过就会冒出来。
"""
from __future__ import annotations

import logging
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from ..models import Item, make_uid
from ..util import fetch, parse_dt

log = logging.getLogger("aidigest.arxiv")

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
_ID_RE = re.compile(r"abs/([^v\s]+)")


def _fmt(dt: datetime) -> str:
    return dt.strftime("%Y%m%d%H%M")


def _query(search: str, max_results: int, delay: float) -> list[Item]:
    xml = fetch(
        API,
        params={
            "search_query": search,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
        timeout=60.0,
    )
    time.sleep(delay)  # arXiv 官方要求的请求间隔
    if not xml:
        return []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        log.warning("arxiv XML parse error: %s", e)
        return []

    items: list[Item] = []
    for e in root.findall("a:entry", NS):
        raw_id = (e.findtext("a:id", "", NS) or "").strip()
        m = _ID_RE.search(raw_id)
        if not m:
            continue
        aid = m.group(1)
        title = " ".join((e.findtext("a:title", "", NS) or "").split())
        summary = " ".join((e.findtext("a:summary", "", NS) or "").split())
        authors = [
            " ".join((a.findtext("a:name", "", NS) or "").split())
            for a in e.findall("a:author", NS)
        ]
        cats = [c.get("term", "") for c in e.findall("a:category", NS)]
        comment = " ".join((e.findtext("arxiv:comment", "", NS) or "").split())
        pdf = ""
        for link in e.findall("a:link", NS):
            if link.get("title") == "pdf":
                pdf = link.get("href", "")
        items.append(
            Item(
                uid=make_uid("arxiv", aid),
                source="arxiv",
                title=title,
                url=f"https://arxiv.org/abs/{aid}",
                pdf_url=pdf,
                published=parse_dt(e.findtext("a:published", "", NS)),
                abstract=summary,
                authors=[a for a in authors if a],
                categories=[c for c in cats if c],
                comment=comment,
                venue="arXiv",
                extra={"arxiv_id": aid, "updated": e.findtext("a:updated", "", NS)},
            )
        )
    return items


def fetch_arxiv(cfg, *, author_window_days: int | None = None) -> tuple[list[Item], list[str]]:
    """返回 (items, errors)。"""
    conf = cfg.sources.get("arxiv", {})
    errors: list[str] = []
    if not conf.get("enabled", True):
        return [], []

    delay = float(conf.get("request_delay_sec", 3.0))
    now = datetime.now(timezone.utc)
    seen: dict[str, Item] = {}

    # ---------- 1. 分类扫描 ----------
    cats = conf.get("categories", [])
    win = int(conf.get("window_days", 2))
    lo, hi = now - timedelta(days=win), now + timedelta(days=1)
    if cats:
        cat_expr = " OR ".join(f"cat:{c}" for c in cats)
        q = f"({cat_expr}) AND submittedDate:[{_fmt(lo)} TO {_fmt(hi)}]"
        got = _query(q, int(conf.get("max_results_per_category", 120)) * 2, delay)
        if not got:
            errors.append(f"arXiv 分类扫描返回 0 条（窗口 {win} 天）")
        for it in got:
            seen[it.uid] = it
        log.info("arxiv categories: %d items", len(got))

    # ---------- 2. watchlist 作者长窗口扫描 ----------
    awin = author_window_days or int(conf.get("author_window_days", 180))
    alo = now - timedelta(days=awin)
    authors = cfg.watchlist.get("authors", [])
    batch = int(conf.get("authors_per_query", 6))

    custom = [a for a in authors if a.get("arxiv_query")]
    plain = [a for a in authors if not a.get("arxiv_query")]

    queries: list[str] = []
    for i in range(0, len(plain), batch):
        chunk = plain[i : i + batch]
        names = []
        for a in chunk:
            for n in [a["name"], *(a.get("aliases") or [])]:
                names.append(f'au:"{n}"')
        queries.append(f"({' OR '.join(names)}) AND submittedDate:[{_fmt(alo)} TO {_fmt(hi)}]")
    for a in custom:
        queries.append(f"({a['arxiv_query']}) AND submittedDate:[{_fmt(alo)} TO {_fmt(hi)}]")

    scan_cats = conf.get("author_scan_categories") or []
    cat_clause = f" AND ({' OR '.join(f'cat:{c}' for c in scan_cats)})" if scan_cats else ""
    queries = [q.replace(" AND submittedDate:", cat_clause + " AND submittedDate:", 1) for q in queries]

    n_author_items = 0
    for q in queries:
        got = _query(q, 200, delay)
        n_author_items += len(got)
        for it in got:
            seen.setdefault(it.uid, it)
    log.info("arxiv authors: %d queries -> %d items (window %dd)", len(queries), n_author_items, awin)
    if queries and n_author_items == 0:
        errors.append("arXiv 作者扫描返回 0 条 —— 可能是网络或 API 限流")

    return list(seen.values()), errors
