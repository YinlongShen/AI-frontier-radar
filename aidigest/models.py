from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuthorHit:
    name: str
    weight: float
    affiliation: str = ""
    confidence: float = 1.0     # 全名精确匹配 1.0；缩写匹配 0.7


@dataclass
class Item:
    """一条候选内容：论文 / 博客 / 页面更新。"""

    uid: str
    source: str                     # arxiv | hf | rss | pagewatch
    title: str
    url: str
    published: datetime
    abstract: str = ""
    authors: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    comment: str = ""
    venue: str = ""                 # feed 名 / 页面名
    lab: str = ""
    upvotes: int = 0
    pdf_url: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    # ---- 分析结果（由 classify / score / summarize 填充）----
    topics: list[tuple[str, float]] = field(default_factory=list)
    primary_topic: str = "misc"
    author_hits: list[AuthorHit] = field(default_factory=list)
    lab_hits: list[str] = field(default_factory=list)
    idea_signals: list[str] = field(default_factory=list)
    score: float = 0.0
    breakdown: dict[str, float] = field(default_factory=dict)

    # ---- LLM 产出 ----
    summary: str = ""               # 一句话中文摘要
    why: str = ""                   # 为什么值得看
    llm_topic: str = ""             # LLM 认为的领域（用于纠正关键词分类）

    # ---- 状态 ----
    is_new: bool = True             # 从未推送过
    is_resurfaced: bool = False     # 旧内容因热度重新浮出
    age_days: float = 0.0

    @property
    def text(self) -> str:
        return f"{self.title}\n{self.abstract}\n{self.comment}"

    @property
    def author_line(self) -> str:
        if not self.authors:
            return ""
        if len(self.authors) <= 4:
            return ", ".join(self.authors)
        return ", ".join(self.authors[:4]) + f", et al. ({len(self.authors)} 人)"

    def compute_age(self, now: datetime | None = None) -> float:
        now = now or datetime.now(timezone.utc)
        pub = self.published
        if pub.tzinfo is None:
            pub = pub.replace(tzinfo=timezone.utc)
        self.age_days = max(0.0, (now - pub).total_seconds() / 86400.0)
        return self.age_days


def item_to_dict(it: Item) -> dict:
    """只序列化抓取阶段的原始字段，分析结果每次重算。"""
    return {
        "uid": it.uid, "source": it.source, "title": it.title, "url": it.url,
        "published": it.published.isoformat(), "abstract": it.abstract,
        "authors": it.authors, "categories": it.categories, "comment": it.comment,
        "venue": it.venue, "lab": it.lab, "upvotes": it.upvotes,
        "pdf_url": it.pdf_url, "extra": it.extra,
    }


def item_from_dict(d: dict) -> Item:
    d = dict(d)
    d["published"] = datetime.fromisoformat(d["published"])
    return Item(**d)


def make_uid(source: str, key: str) -> str:
    if source == "arxiv":
        return f"arxiv:{key}"
    return f"{source}:{hashlib.sha1(key.encode('utf-8')).hexdigest()[:16]}"
