"""LLM 摘要路径的测试。用假的 client，不联网、不花钱。"""
import json
from datetime import datetime, timezone

import pytest

from aidigest import summarize as S
from aidigest.config import Config
from aidigest.models import Item


@pytest.fixture(scope="module")
def cfg():
    return Config.load(".")


def _items(n=2):
    return [
        Item(uid=f"u{i}", source="arxiv", title=f"Paper {i}", url="http://x",
             published=datetime.now(timezone.utc), abstract="We do a thing.",
             authors=["Someone Real"], categories=["cs.LG"])
        for i in range(n)
    ]


class _Block:
    type = "text"

    def __init__(self, text):
        self.text = text


class _Resp:
    def __init__(self, payload):
        self.content = [_Block(json.dumps(payload))]


def _fake_client(payload_fn, calls):
    class Msgs:
        def create(self, **kw):
            calls.append(kw)
            return _Resp(payload_fn(kw))

    class Client:
        messages = Msgs()

    return Client()


def test_summarize_fills_fields_and_can_fix_topic(cfg, monkeypatch):
    calls = []
    payload = {"items": [
        {"index": 0, "summary": "把动作离散化成 token 来训机器人策略。", "why": "范式换了", "topic": "vla"},
        {"index": 1, "summary": "第二条摘要", "why": "增量改进", "topic": "llm"},
    ]}
    import anthropic
    monkeypatch.setattr(anthropic, "Anthropic", lambda *a, **k: _fake_client(lambda kw: payload, calls))

    items = _items(2)
    out, errors = S.summarize(cfg, items)
    assert errors == []
    assert out[0].summary.startswith("把动作离散化")
    assert out[0].why == "范式换了"
    assert out[0].primary_topic == "vla"      # LLM 纠正了关键词分类
    assert out[1].primary_topic == "llm"
    # 请求本身：用了配置里的模型、开了 adaptive thinking、带了结构化输出 schema
    kw = calls[0]
    assert kw["model"] == cfg.main["llm"]["model"]
    assert kw["thinking"] == {"type": "adaptive"}
    assert kw["output_config"]["format"]["type"] == "json_schema"


def test_summarize_degrades_gracefully_on_api_error(cfg, monkeypatch):
    import anthropic

    class Boom:
        class messages:
            @staticmethod
            def create(**kw):
                raise RuntimeError("429 rate limited")

    monkeypatch.setattr(anthropic, "Anthropic", lambda *a, **k: Boom())
    items = _items(2)
    out, errors = S.summarize(cfg, items)
    assert len(out) == 2
    assert out[0].summary == ""          # 没有摘要，但条目还在
    assert errors and "LLM 摘要失败" in errors[0]


def test_summarize_ignores_out_of_range_index(cfg, monkeypatch):
    """模型返回了越界的 index 也不能崩。"""
    import anthropic
    payload = {"items": [{"index": 99, "summary": "x", "why": "y", "topic": "llm"}]}
    monkeypatch.setattr(anthropic, "Anthropic", lambda *a, **k: _fake_client(lambda kw: payload, []))
    out, errors = S.summarize(cfg, _items(1))
    assert out[0].summary == ""
    assert errors == []


def test_batching_splits_requests(cfg, monkeypatch):
    import anthropic
    calls = []
    monkeypatch.setattr(anthropic, "Anthropic",
                        lambda *a, **k: _fake_client(lambda kw: {"items": []}, calls))
    n = cfg.main["llm"]["batch_size"] * 2 + 1
    S.summarize(cfg, _items(n))
    assert len(calls) == 3
