"""重要性打分。

核心思想：**人比关键词可靠**。watchlist 里的人出手，权重压倒一切；
其次是机构信号、社区热度（HF 票数）、「大想法」句式、新鲜度。
"""
from __future__ import annotations

import math
import re

from .models import AuthorHit, Item
from .util import compile_patterns, names_match, norm_text


class Scorer:
    def __init__(self, cfg):
        sc = cfg.main.get("scoring", {})
        self.w = sc.get("weights", {})
        self.min_score = float(sc.get("min_score", 9.0))
        self.min_name_conf = float(sc.get("min_name_confidence", 1.0))
        self.max_authors = int(sc.get("max_authors_for_author_match", 30))
        self.idea_pats = compile_patterns(sc.get("idea_signal_patterns") or [])

        wl = cfg.watchlist
        defaults = wl.get("defaults", {})
        self.default_weight = float(defaults.get("weight", 2.0))
        self.authors = []
        for a in wl.get("authors", []):
            self.authors.append(
                {
                    "name": a["name"],
                    "names": [a["name"], *(a.get("aliases") or [])],
                    "weight": float(a.get("weight", self.default_weight)),
                    "affiliation": a.get("affiliation", ""),
                    "categories": set(a.get("categories") or []),
                }
            )
        self.labs = [
            {"name": l["name"], "pats": compile_patterns(l.get("patterns") or []),
             "weight": float(l.get("weight", 1.0))}
            for l in wl.get("labs", [])
        ]

    # ---------------- 匹配 ----------------
    def match_authors(self, item: Item) -> list[AuthorHit]:
        # 大型合作组论文（BESIII、LHCb…）作者数以百计，姓名巧合几乎必然发生。
        if len(item.authors) > self.max_authors:
            return []
        hits: dict[str, AuthorHit] = {}
        for paper_author in item.authors:
            for wa in self.authors:
                if wa["categories"] and not (wa["categories"] & set(item.categories)):
                    continue
                best = 0.0
                for cand in wa["names"]:
                    best = max(best, names_match(paper_author, cand))
                if best >= self.min_name_conf:
                    prev = hits.get(wa["name"])
                    if not prev or best > prev.confidence:
                        hits[wa["name"]] = AuthorHit(
                            name=wa["name"], weight=wa["weight"],
                            affiliation=wa["affiliation"], confidence=best,
                        )
        return sorted(hits.values(), key=lambda h: -h.weight * h.confidence)

    def match_labs(self, item: Item) -> list[str]:
        found = []
        if item.lab:
            found.append(item.lab)
        blob = norm_text(f"{item.comment} {item.venue} {item.abstract[:400]}")
        for l in self.labs:
            if any(p.search(blob) for p in l["pats"]):
                if l["name"] not in found:
                    found.append(l["name"])
        # watchlist 作者的机构也算机构信号
        for h in item.author_hits:
            if h.affiliation and h.affiliation != "—" and h.affiliation not in found:
                found.append(h.affiliation)
        return found

    def idea_signals(self, item: Item) -> list[str]:
        t = norm_text(item.title)
        blob = f"{t} {norm_text(item.abstract[:600])}"
        out = []
        for p in self.idea_pats:
            m = p.search(t) or p.search(blob)
            if m:
                out.append(m.group(0).strip())
        if re.search(r"\b(position|perspective|opinion) paper\b", norm_text(item.comment)):
            out.append("position paper")
        return out

    # ---------------- 打分 ----------------
    def score(self, item: Item, *, max_window_days: float = 180.0) -> Item:
        item.author_hits = self.match_authors(item)
        item.lab_hits = self.match_labs(item)
        item.idea_signals = self.idea_signals(item)

        b: dict[str, float] = {}

        author_raw = sum(h.weight * h.confidence for h in item.author_hits)
        b["watchlist"] = float(self.w.get("watchlist_author", 6.0)) * author_raw

        lab_raw = min(len(item.lab_hits), 2) * 0.5
        b["lab"] = float(self.w.get("lab", 2.0)) * lab_raw

        b["hf"] = float(self.w.get("hf_upvotes", 1.2)) * math.log1p(max(0, item.upvotes))

        topic_conf = item.topics[0][1] if item.topics else 0.0
        b["topic"] = float(self.w.get("topic_confidence", 0.6)) * min(topic_conf, 12.0)

        b["idea"] = float(self.w.get("idea_signal", 2.5)) * min(len(item.idea_signals), 2)

        age = item.compute_age()
        recency = max(0.0, 1.0 - age / max(max_window_days, 1.0))
        b["recency"] = float(self.w.get("recency", 1.5)) * recency

        n_topics = len([1 for _, s in item.topics if s >= 3.0])
        b["cross_topic"] = float(self.w.get("cross_topic", 0.8)) * max(0, n_topics - 1)

        if item.source == "rss":
            # 博客没有作者列表也没有票数，靠上面几项永远过不了线；
            # 但 DeepMind / OpenAI / Anthropic 的博客正是新想法的首发地。
            b["blog"] = float(self.w.get("blog", 3.5)) * (1.0 if item.lab and item.lab != "—" else 0.5)
        if item.source == "pagewatch":
            b["pagewatch"] = float(item.extra.get("pagewatch_weight", 1.5)) * 3.0
        if item.is_resurfaced:
            b["resurface"] = 4.0

        item.breakdown = {k: round(v, 2) for k, v in b.items() if v}
        item.score = round(sum(b.values()), 2)
        return item

    def keep(self, item: Item) -> bool:
        """watchlist 命中的永远保留 —— 这是整个工具存在的理由。"""
        return bool(item.author_hits) or item.is_resurfaced or item.score >= self.min_score
