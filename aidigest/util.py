from __future__ import annotations

import logging
import re
import time
import unicodedata
from datetime import datetime, timezone

import httpx

log = logging.getLogger("aidigest")

UA = "ai-frontier-radar/0.1 (personal research digest; +https://github.com/)"

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_WS = re.compile(r"\s+")


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def norm_text(s: str) -> str:
    s = strip_accents(s or "").lower()
    s = _PUNCT.sub(" ", s)
    return _WS.sub(" ", s).strip()


def name_parts(name: str) -> tuple[str, str]:
    """返回 (first, last)，忽略中间名/中间缩写。支持 'Last, First' 形式。"""
    n = norm_text(name)
    if not n:
        return "", ""
    if "," in name:
        last, _, rest = name.partition(",")
        return norm_text(rest).split(" ")[0] if rest.strip() else "", norm_text(last)
    toks = n.split(" ")
    if len(toks) == 1:
        return "", toks[0]
    return toks[0], toks[-1]


def names_match(a: str, b: str) -> float:
    """0.0 不匹配 / 0.7 缩写匹配 / 1.0 全名匹配。"""
    fa, la = name_parts(a)
    fb, lb = name_parts(b)
    if not la or la != lb:
        return 0.0
    if fa == fb and len(fa) > 1:
        return 1.0
    if not fa or not fb:
        return 0.0
    # 一方是缩写：R. vs Richard
    if len(fa) == 1 or len(fb) == 1:
        return 0.7 if fa[0] == fb[0] else 0.0
    return 0.0


def compile_patterns(pats: list[str]) -> list[re.Pattern]:
    out = []
    for p in pats or []:
        try:
            out.append(re.compile(rf"(?<!\w){p}(?!\w)" if p.isalnum() else p, re.IGNORECASE))
        except re.error:
            out.append(re.compile(re.escape(p), re.IGNORECASE))
    return out


def count_hits(patterns: list[re.Pattern], text: str) -> tuple[int, list[str]]:
    n, found = 0, []
    for p in patterns:
        m = p.search(text)
        if m:
            n += 1
            found.append(m.group(0).strip())
    return n, found


def parse_dt(s: str) -> datetime:
    s = (s or "").strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.%fZ"):
        try:
            dt = datetime.strptime(s, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return datetime.now(timezone.utc)


def fetch(url: str, *, timeout: float = 30.0, retries: int = 2, params: dict | None = None) -> str | None:
    """GET 一个 URL，失败返回 None（不抛异常 —— 单个源挂掉不该拖垮整轮）。"""
    for attempt in range(retries + 1):
        try:
            r = httpx.get(
                url,
                params=params,
                timeout=timeout,
                follow_redirects=True,
                headers={"User-Agent": UA, "Accept": "*/*"},
            )
            if r.status_code == 200:
                return r.text
            log.warning("fetch %s -> HTTP %s", url, r.status_code)
            if r.status_code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(2.0 * (attempt + 1))
                continue
            return None
        except Exception as e:  # noqa: BLE001
            log.warning("fetch %s failed (%s/%s): %s", url, attempt + 1, retries + 1, e)
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    return None


def truncate(s: str, n: int) -> str:
    s = _WS.sub(" ", (s or "").strip())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"
