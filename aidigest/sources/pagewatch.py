"""页面差分监控。

有些最重要的想法不在 arXiv 也没有 RSS —— 比如 Sutton 只在 incompleteideas.net 上
贴新文章。这里把页面上的链接抓下来存快照，下次跑的时候只报「新出现的链接」。

首次监控一个页面时默认只建立基线、不报告（否则会一次涌出上百条历史链接）；
backfill 模式下会报告最多 report_cap 条，方便你补看。
"""
from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse

from ..models import Item, make_uid
from ..util import fetch, truncate

log = logging.getLogger("aidigest.pagewatch")

_A_RE = re.compile(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
_SKIP = re.compile(r"^(#|mailto:|javascript:|tel:)")


def _links(html: str, base: str, pattern: str | None) -> list[tuple[str, str]]:
    pat = re.compile(pattern, re.IGNORECASE) if pattern else None
    out, seen = [], set()
    for href, inner in _A_RE.findall(html):
        href = href.strip()
        if not href or _SKIP.match(href):
            continue
        if pat and not pat.search(href):
            continue
        absolute = urljoin(base, href).split("#")[0].rstrip("/")
        if absolute in seen or absolute.rstrip("/") == base.rstrip("/"):
            continue
        seen.add(absolute)
        text = " ".join(_TAG_RE.sub(" ", inner).split())
        out.append((absolute, truncate(text, 200)))
    return out


def fetch_pagewatch(cfg, state, *, report_on_init: bool = False, report_cap: int = 15,
                    persist: bool = True):
    conf = cfg.sources.get("pagewatch", {})
    errors: list[str] = []
    if not conf.get("enabled", True):
        return [], []

    now = datetime.now(timezone.utc)
    items: list[Item] = []

    for page in conf.get("pages", []):
        name, url = page.get("name", "?"), page.get("url", "")
        html = fetch(url, timeout=30.0)
        if not html:
            errors.append(f"页面监控 {name}: 抓取失败 ({url})")
            continue

        links = _links(html, url, page.get("link_pattern"))
        if not links:
            errors.append(f"页面监控 {name}: 未匹配到任何链接（link_pattern 可能需要调整）")
            continue

        known = state.known_links(name)
        initialized = state.page_initialized(name)
        fresh = [(u, t) for u, t in links if u not in known]
        if persist:
            state.add_links(name, links)   # dry-run 时不写基线，否则会"吃掉"下一次的新链接

        if not initialized and not report_on_init:
            log.info("pagewatch %s: 基线已建立 (%d 链接)", name, len(links))
            continue

        report = fresh[:report_cap] if not initialized else fresh
        for u, t in report:
            title = t or urlparse(u).path.rsplit("/", 1)[-1].replace("-", " ")
            items.append(
                Item(
                    uid=make_uid("pagewatch", u),
                    source="pagewatch",
                    title=title,
                    url=u,
                    published=now,          # 页面链接没有可靠日期，用发现时间
                    abstract="",
                    venue=name,
                    lab=page.get("lab", ""),
                    authors=[page["author"]] if page.get("author") else [],
                    extra={"pagewatch_weight": float(page.get("weight", 1.5)),
                           "no_reliable_date": True},
                )
            )
        log.info("pagewatch %s: %d 新链接", name, len(report))

    return items, errors
