"""用 Claude 给进入 digest 的条目写中文速览。

没有凭据时自动降级：直接截断摘要，工具照常出结果（LLM 是增强，不是依赖）。
"""
from __future__ import annotations

import json
import logging
import os

from .models import Item
from .util import truncate

log = logging.getLogger("aidigest.llm")

SYSTEM_ZH = """你在为一位 AI 方向的研究者做每日前沿速览。对每篇给定的论文/文章输出：

1. summary：一句话中文摘要（40 字以内），说清楚**做了什么**，不要写"本文提出了一种方法"这种废话。
2. why：一句话说明**为什么这位研究者值得花时间看**（30 字以内）。可以是：谁做的、
   挑战了什么共识、给出了什么新范式、在哪个基准上跨了一大步、是否只是增量工作。
   如果确实是增量工作，就直说"增量改进"，不要吹。
3. topic：从给定领域 id 列表里选一个最贴切的。

诚实第一：看不出创新点就说看不出。不要编造论文里没有的结果或数字。"""

SYSTEM_EN = """You are preparing a daily AI frontier digest for a researcher. For each paper/post:
1. summary: one sentence (<=25 words) on what was actually done — no "this paper proposes a method" filler.
2. why: one sentence (<=20 words) on why it is worth their time, or plainly say "incremental" if it is.
3. topic: pick the single best-fitting topic id from the provided list.
Be honest; never invent results or numbers that are not in the text."""


def _schema(topic_ids: list[str]) -> dict:
    return {
        "type": "json_schema",
        "schema": {
            "type": "object",
            "properties": {
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "index": {"type": "integer"},
                            "summary": {"type": "string"},
                            "why": {"type": "string"},
                            "topic": {"type": "string", "enum": topic_ids},
                        },
                        "required": ["index", "summary", "why", "topic"],
                        "additionalProperties": False,
                    },
                }
            },
            "required": ["items"],
            "additionalProperties": False,
        },
    }


def _payload(items: list[Item]) -> str:
    blocks = []
    for i, it in enumerate(items):
        blocks.append(
            f"[{i}] 标题: {it.title}\n"
            f"    来源: {it.venue or it.source}"
            + (f" | 作者: {truncate(', '.join(it.authors[:8]), 200)}" if it.authors else "")
            + (f" | arXiv 分类: {', '.join(it.categories[:4])}" if it.categories else "")
            + (f" | 命中关注名单: {', '.join(h.name for h in it.author_hits)}" if it.author_hits else "")
            + (f"\n    摘要: {truncate(it.abstract, 1200)}" if it.abstract else "\n    （无摘要，只有标题和链接）")
        )
    return "\n\n".join(blocks)


def has_credentials() -> bool:
    """环境变量，或者 `ant auth login` 存在本地的 profile。"""
    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
        return True
    from pathlib import Path
    return (Path.home() / ".config" / "anthropic").exists()


def summarize(cfg, items: list[Item]) -> tuple[list[Item], list[str]]:
    """就地填充 item.summary / why / llm_topic。返回 (items, errors)。"""
    conf = cfg.main.get("llm", {})
    errors: list[str] = []
    if not conf.get("enabled", True) or not items:
        return items, []

    try:
        import anthropic
    except ImportError:
        return items, ["未安装 anthropic SDK，跳过 LLM 摘要"]

    try:
        client = anthropic.Anthropic()
    except Exception as e:  # noqa: BLE001
        return items, [f"Anthropic 客户端初始化失败，跳过 LLM 摘要: {e}"]

    topic_ids = [t["id"] for t in cfg.topics.get("topics", [])]
    model = conf.get("model", "claude-opus-5")
    effort = conf.get("effort", "medium")
    batch = int(conf.get("batch_size", 10))
    limit = int(conf.get("max_items", 30))
    targets = items[:limit]
    system = SYSTEM_ZH if cfg.language == "zh" else SYSTEM_EN

    for start in range(0, len(targets), batch):
        chunk = targets[start : start + batch]
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=16000,
                system=system,
                thinking={"type": "adaptive"},
                output_config={"effort": effort, "format": _schema(topic_ids)},
                messages=[{
                    "role": "user",
                    "content": (
                        f"可选领域 id：{', '.join(topic_ids)}\n\n"
                        f"请为下面 {len(chunk)} 条内容各写一条速览：\n\n{_payload(chunk)}"
                    ),
                }],
            )
            text = next((b.text for b in resp.content if b.type == "text"), "")
            data = json.loads(text)
        except Exception as e:  # noqa: BLE001
            errors.append(f"LLM 摘要失败（第 {start // batch + 1} 批，{len(chunk)} 条）：{e}")
            log.warning("llm batch failed: %s", e)
            continue

        for row in data.get("items", []):
            idx = row.get("index")
            if not isinstance(idx, int) or not (0 <= idx < len(chunk)):
                continue
            it = chunk[idx]
            it.summary = (row.get("summary") or "").strip()
            it.why = (row.get("why") or "").strip()
            t = (row.get("topic") or "").strip()
            if t in topic_ids:
                it.llm_topic = t
                it.primary_topic = t

    return items, errors
