"""领域分类：关键词打分 + arXiv 分类加成。LLM 可在之后纠正主领域。"""
from __future__ import annotations

from .models import Item
from .util import compile_patterns, count_hits, norm_text

STRONG_W = 3.0
WEAK_W = 1.0
CAT_W = 1.0


class Classifier:
    def __init__(self, cfg):
        self.meta = cfg.topics.get("meta", {})
        self.topics = []
        for t in cfg.topics.get("topics", []):
            self.topics.append(
                {
                    "id": t["id"],
                    "strong": compile_patterns(t.get("strong") or []),
                    "weak": compile_patterns(t.get("weak") or []),
                    "cats": set(t.get("arxiv_categories") or []),
                }
            )
        self.fallback = self.meta.get("fallback_topic", "misc")
        self.sec_thresh = float(self.meta.get("secondary_threshold", 3.0))
        self.min_score = float(self.meta.get("min_score_to_classify", 1.0))

    def classify(self, item: Item) -> Item:
        text = norm_text(item.text)
        cats = set(item.categories)
        scored: list[tuple[str, float]] = []

        for t in self.topics:
            if not t["strong"] and not t["weak"]:
                continue
            ns, _ = count_hits(t["strong"], text)
            nw, _ = count_hits(t["weak"], text)
            s = STRONG_W * ns + WEAK_W * nw
            if s > 0 and cats & t["cats"]:
                s += CAT_W
            if s > 0:
                scored.append((t["id"], round(s, 2)))

        scored.sort(key=lambda x: -x[1])
        item.topics = scored
        if scored and scored[0][1] >= self.min_score:
            item.primary_topic = scored[0][0]
        else:
            item.primary_topic = self.fallback
        return item

    def secondary(self, item: Item) -> list[str]:
        return [t for t, s in item.topics[1:] if s >= self.sec_thresh]
