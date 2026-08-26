"""把打完分的条目渲染成每日 Markdown 简报。"""
from __future__ import annotations

from datetime import datetime, timezone

from .models import Item

SOURCE_LABEL = {"arxiv": "arXiv", "hf": "HF Papers", "rss": "Blog", "pagewatch": "页面更新"}


def _age_str(item: Item) -> str:
    if item.extra.get("no_reliable_date"):
        return "新发现"
    d = int(item.age_days)
    if d <= 0:
        return "今天"
    if d == 1:
        return "昨天"
    if d < 30:
        return f"{d} 天前"
    return f"{item.published.strftime('%m-%d')}（{d} 天前）"


def _badges(item: Item) -> str:
    parts = []
    if item.author_hits:
        names = []
        for h in item.author_hits[:3]:
            tag = h.name if h.confidence >= 1.0 else f"{h.name}?"
            names.append(f"{tag}" + (f" · {h.affiliation}" if h.affiliation and h.affiliation != "—" else ""))
        more = f" +{len(item.author_hits) - 3}" if len(item.author_hits) > 3 else ""
        parts.append("👤 **" + " / ".join(names) + more + "**")
    elif item.lab_hits:
        parts.append("🏛 " + " / ".join(item.lab_hits[:2]))
    if item.upvotes:
        parts.append(f"🔥 {item.upvotes}")
    if item.idea_signals:
        sig = item.idea_signals[0]
        parts.append("💡 " + (sig if len(sig) > 6 else "想法型"))
    parts.append(f"{SOURCE_LABEL.get(item.source, item.source)} · {_age_str(item)}")
    return " | ".join(parts)


def _entry(item: Item, *, numbered: int | None = None) -> str:
    head = f"{numbered}. " if numbered else "- "
    lines = [f"{head}**[{item.title}]({item.url})**"]
    pad = "   " if numbered else "  "
    if item.summary:
        lines.append(f"{pad}{item.summary}")
    elif item.abstract:
        from .util import truncate
        lines.append(f"{pad}{truncate(item.abstract, 180)}")
    if item.why:
        lines.append(f"{pad}*→ {item.why}*")
    lines.append(f"{pad}<sub>{_badges(item)}</sub>")
    return "\n".join(lines)


def render_digest(cfg, items: list[Item], meta: dict) -> str:
    date = meta.get("date") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    top_n = int(cfg.main.get("output", {}).get("top_n_highlights", 10))

    items = sorted(items, key=lambda i: -i.score)
    highlights = items[:top_n]
    resurfaced = [i for i in items if i.is_resurfaced]

    out: list[str] = []
    out.append(f"# AI 前沿雷达 · {date}\n")

    n_watch = len({h.name for i in items for h in i.author_hits})
    out.append(
        f"> 扫描 **{meta.get('n_fetched', 0)}** 条 → 入选 **{len(items)}** 条 ｜ "
        f"关注名单命中 **{n_watch}** 位研究者 ｜ "
        f"生成于 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC\n"
    )

    # ---- 目录 ----
    by_topic: dict[str, list[Item]] = {}
    for it in items:
        by_topic.setdefault(it.primary_topic, []).append(it)
    order = [t["id"] for t in cfg.topics.get("topics", [])]
    present = [t for t in order if by_topic.get(t)]
    if present:
        toc = []
        for tid in present:
            t = cfg.topic_by_id(tid)
            toc.append(f"{t.get('emoji','📄')} {t.get('name_zh', tid)} ({len(by_topic[tid])})")
        out.append("**今日分布**：" + " ｜ ".join(toc) + "\n")

    # ---- 今日必读 ----
    if highlights:
        out.append("\n## ⭐ 今日必读\n")
        for n, it in enumerate(highlights, 1):
            out.append(_entry(it, numbered=n) + "\n")

    # ---- 迟到的热度 ----
    if resurfaced:
        out.append("\n## 🕰️ 迟到的热度\n")
        out.append("*旧内容，但最近热度明显上涨 —— 之前可能被你错过。*\n")
        for it in resurfaced:
            out.append(_entry(it) + "\n")

    # ---- 分领域 ----
    out.append("\n---\n")
    for tid in present:
        t = cfg.topic_by_id(tid)
        group = by_topic[tid]
        out.append(f"\n## {t.get('emoji','📄')} {t.get('name_zh', tid)}\n")
        for it in group:
            out.append(_entry(it) + "\n")

    # ---- 源状态 ----
    out.append("\n---\n\n<details>\n<summary>📡 源状态与运行信息</summary>\n")
    src_counts: dict[str, int] = {}
    for it in items:
        src_counts[it.source] = src_counts.get(it.source, 0) + 1
    dist = ", ".join(
        f"{SOURCE_LABEL.get(k, k)} {v}" for k, v in sorted(src_counts.items(), key=lambda x: -x[1])
    )
    out.append("\n**入选来源分布**：" + (dist or "无"))
    errs = meta.get("errors") or []
    if errs:
        out.append("\n\n**本轮出问题的源**（不影响其他源）：\n")
        for e in errs:
            out.append(f"- {e}")
    else:
        out.append("\n\n所有数据源正常。")
    backlog = int(meta.get("backlog") or 0)
    if backlog:
        out.append(f"\n\n**积压 {backlog} 条**（超出本期容量，未标记为已推送，会出现在后续几期）。")
    out.append(f"\n\n**模式**：{meta.get('mode','daily')}　**LLM 摘要**：{meta.get('llm','off')}\n")
    out.append("</details>\n")

    return "\n".join(out)
