"""不联网的单元测试：姓名匹配、分类、打分、页面链接提取、渲染。"""
from datetime import datetime, timedelta, timezone

import pytest

from aidigest.classify import Classifier
from aidigest.config import Config
from aidigest.models import Item, make_uid
from aidigest.render import render_digest
from aidigest.score import Scorer
from aidigest.sources.pagewatch import _links
from aidigest.util import names_match, norm_text


@pytest.fixture(scope="module")
def cfg():
    return Config.load(".")


# ---------------- 姓名匹配 ----------------
@pytest.mark.parametrize("a,b,expected", [
    ("Richard S. Sutton", "Richard Sutton", 1.0),   # 中间名不影响
    ("Richard Sutton", "Richard S. Sutton", 1.0),
    ("R. S. Sutton", "Richard Sutton", 0.7),        # 缩写 -> 低置信度
    ("Rich Sutton", "Richard Sutton", 0.0),         # 昵称必须靠 aliases 显式配
    ("Kaiming He", "Kaiming He", 1.0),
    ("Kaiming He", "He Wang", 0.0),                 # 姓不同
    ("Yann LeCun", "Yann Lecun", 1.0),              # 大小写无关
    ("Jürgen Schmidhuber", "Jurgen Schmidhuber", 1.0),  # 变音符号归一
    ("Xiaoming Li", "Richard Sutton", 0.0),
])
def test_names_match(a, b, expected):
    assert names_match(a, b) == expected


def test_norm_text_strips_punct_and_accents():
    assert norm_text("Vision-Language-Action!") == "vision language action"


# ---------------- 分类 ----------------
def _paper(title, abstract="", cats=None, authors=None, **kw):
    return Item(
        uid=make_uid("arxiv", title), source="arxiv", title=title, url="http://x",
        published=datetime.now(timezone.utc), abstract=abstract,
        categories=cats or [], authors=authors or [], **kw,
    )


def test_classify_vla(cfg):
    it = _paper("A Vision-Language-Action model for robot manipulation",
                "We train a robot policy with action chunking on teleoperation data.",
                cats=["cs.RO"])
    Classifier(cfg).classify(it)
    assert it.primary_topic == "vla"


def test_classify_world_model(cfg):
    it = _paper("Learning a world model for interactive environment generation",
                "We build a latent dynamics model and use model-based reinforcement learning.",
                cats=["cs.LG"])
    Classifier(cfg).classify(it)
    assert it.primary_topic == "world_model"


def test_classify_falls_back_when_nothing_matches(cfg):
    it = _paper("On the crystallography of certain ternary alloys")
    Classifier(cfg).classify(it)
    assert it.primary_topic == "misc"


# ---------------- 打分 ----------------
def test_watchlist_author_dominates_score(cfg):
    scorer = Scorer(cfg)
    big = _paper("Some quiet paper about credit assignment",
                 "A short note.", cats=["cs.LG"], authors=["Richard S. Sutton"])
    small = _paper("Another incremental benchmark result",
                   "We improve accuracy by 0.3%.", cats=["cs.LG"], authors=["Anonymous Person"])
    Classifier(cfg).classify(big)
    Classifier(cfg).classify(small)
    scorer.score(big)
    scorer.score(small)
    assert big.author_hits and big.author_hits[0].name == "Richard S. Sutton"
    assert big.score > small.score
    assert scorer.keep(big)          # 名单命中永远保留…
    assert not scorer.keep(small)    # …无名增量工作被过滤掉


def test_old_watchlist_paper_still_kept(cfg):
    """核心需求：五月发的论文八月才第一次看到，也必须留下。"""
    it = _paper("Enactivism and the nature of intelligence", "A position paper.",
                cats=["cs.AI"], authors=["Richard S. Sutton"])
    it.published = datetime.now(timezone.utc) - timedelta(days=110)
    Classifier(cfg).classify(it)
    Scorer(cfg).score(it)
    assert it.age_days > 100
    assert Scorer(cfg).keep(it)


def test_idea_signal_detected(cfg):
    it = _paper("Rethinking the role of memory in agents", "We argue that current agents…")
    Scorer(cfg).score(it)
    assert it.idea_signals


def test_initial_only_match_is_rejected_by_default(cfg):
    """"K. He" 不该算成 Kaiming He —— 否则 500 作者的合作组论文会霸榜。"""
    it = _paper("Temporal difference revisited", authors=["R. S. Sutton"])
    Scorer(cfg).score(it)
    assert it.author_hits == []
    assert names_match("R. S. Sutton", "Richard Sutton") == 0.7   # 函数本身仍能表达"低置信度"


def test_large_collaboration_paper_gets_no_author_credit(cfg):
    """BESIII/LHCb 那类论文：作者上百，姓名巧合必然发生，一律不给关注名单加分。"""
    authors = [f"Person Number{i}" for i in range(400)] + ["Kaiming He"]
    it = _paper("Measurement of the branching fraction of some meson decay",
                "Using events collected by the detector at the collider.",
                cats=["hep-ex"], authors=authors)
    Classifier(cfg).classify(it)
    Scorer(cfg).score(it)
    assert it.author_hits == []
    assert not Scorer(cfg).keep(it)


def test_normal_sized_paper_still_matches(cfg):
    it = _paper("Masked autoencoders revisited", "vision", cats=["cs.CV"],
                authors=["Kaiming He", "Xinlei Chen"])
    Scorer(cfg).score(it)
    assert {h.name for h in it.author_hits} == {"Kaiming He", "Xinlei Chen"}


# ---------------- 页面链接提取 ----------------
def test_pagewatch_link_extraction():
    html = """
    <a href="/IncIdeas/BitterLesson.html">The Bitter Lesson</a>
    <a href="mailto:x@y.z">mail</a>
    <a href="#top">top</a>
    <a href="http://other.com/paper.pdf">A PDF</a>
    """
    got = _links(html, "http://incompleteideas.net/", r"\.(html|pdf)$")
    urls = [u for u, _ in got]
    assert "http://incompleteideas.net/IncIdeas/BitterLesson.html" in urls
    assert "http://other.com/paper.pdf" in urls
    assert not any("mailto" in u for u in urls)
    assert dict(got)["http://incompleteideas.net/IncIdeas/BitterLesson.html"] == "The Bitter Lesson"


# ---------------- 渲染 ----------------
def test_render_produces_sections(cfg):
    it = _paper("A Vision-Language-Action model", "robot policy", cats=["cs.RO"],
                authors=["Chelsea Finn"])
    Classifier(cfg).classify(it)
    Scorer(cfg).score(it)
    it.summary = "一句话摘要"
    md = render_digest(cfg, [it], {"date": "2026-08-26", "n_fetched": 100, "errors": []})
    assert "# AI 前沿雷达 · 2026-08-26" in md
    assert "⭐ 今日必读" in md
    assert "Chelsea Finn" in md
    assert "一句话摘要" in md


def test_render_survives_empty_input(cfg):
    md = render_digest(cfg, [], {"date": "2026-08-26", "n_fetched": 0, "errors": ["源 X 挂了"]})
    assert "AI 前沿雷达" in md
    assert "源 X 挂了" in md


# ---------------- 选择与积压 ----------------
def test_select_respects_caps_and_reports_backlog(cfg):
    from aidigest.pipeline import _select
    items = []
    for i in range(50):
        it = _paper(f"Diffusion model for image generation number {i}",
                    "image synthesis", cats=["cs.CV"])
        it.primary_topic = "cv"
        it.score = 100 - i
        items.append(it)
    picked, backlog = _select(cfg, items, None)
    # 单领域配额生效
    assert len(picked) == cfg.main["output"]["max_items_per_topic"]
    assert backlog == 50 - len(picked)


def test_select_never_drops_watchlist_hits(cfg):
    """名单命中的条目不受单领域配额挤掉 —— 否则又会漏掉大佬的工作。"""
    from aidigest.pipeline import _select
    items = []
    for i in range(20):
        it = _paper(f"Routine CV paper {i}", "image", cats=["cs.CV"])
        it.primary_topic = "cv"
        it.score = 100 - i
        items.append(it)
    star = _paper("Something by Kaiming", "image", cats=["cs.CV"], authors=["Kaiming He"])
    star.primary_topic = "cv"
    star.score = 1.0          # 分数最低，排在最后
    Scorer(cfg).score(star)   # 填充 author_hits
    star.score = 1.0
    items.append(star)
    picked, _ = _select(cfg, items, None)
    assert star in picked


def test_select_reserves_slots_for_blogs(cfg):
    """博客分数天然低于 watchlist 论文，必须靠预留名额才进得来。"""
    from aidigest.pipeline import _select
    items = []
    for i in range(100):
        it = _paper(f"High scoring arxiv paper {i}", "llm", cats=["cs.LG"])
        it.primary_topic, it.score = "llm", 100 - i * 0.1
        items.append(it)
    for i in range(5):
        b = Item(uid=f"rss{i}", source="rss", title=f"DeepMind post {i}", url="http://x",
                 published=datetime.now(timezone.utc), venue=f"Feed {i}", lab="Google DeepMind")
        b.primary_topic, b.score = "llm", 9.5
        items.append(b)
    picked, _ = _select(cfg, items, None)
    assert sum(1 for i in picked if i.source == "rss") >= 3


def test_select_caps_a_single_noisy_feed(cfg):
    """一个高产 feed 不能吃光所有博客名额。"""
    from aidigest.pipeline import _select
    items = [_paper(f"paper {i}", "llm", cats=["cs.LG"]) for i in range(80)]
    for it in items:
        it.primary_topic, it.score = "llm", 50.0
    for i in range(20):
        b = Item(uid=f"spam{i}", source="rss", title=f"Vendor post {i}", url="http://x",
                 published=datetime.now(timezone.utc), venue="Noisy Vendor Blog", lab="X")
        b.primary_topic, b.score = "llm", 9.5
        items.append(b)
    picked, _ = _select(cfg, items, None)
    noisy = sum(1 for i in picked if i.venue == "Noisy Vendor Blog")
    assert noisy <= cfg.main["output"]["max_per_venue"]


def test_rss_short_body_is_not_treated_as_abstract(monkeypatch, cfg):
    """research.google 的 summary 字段放的是 "Algorithms & Theory" 这种分类标签，
    当成正文会把条目分到「理论」领域。"""
    import aidigest.sources.rss as R

    feed_xml = """<?xml version="1.0"?><rss version="2.0"><channel>
      <item><title>How mobility helps language models</title>
      <link>https://research.google/blog/x/</link>
      <description>Algorithms &amp; Theory</description>
      <pubDate>Mon, 24 Aug 2026 00:00:00 GMT</pubDate></item>
    </channel></rss>"""
    monkeypatch.setattr(R, "fetch", lambda *a, **k: feed_xml)
    cfg2 = Config.load(".")
    cfg2.sources["rss"] = {"enabled": True, "window_days": 3650,
                           "feeds": [{"name": "T", "url": "http://x", "lab": "Google DeepMind"}]}
    items, errors = R.fetch_rss(cfg2)
    assert len(items) == 1
    assert items[0].abstract == ""
    assert items[0].extra["feed_tag"] == "Algorithms & Theory"
    Classifier(cfg).classify(items[0])
    assert items[0].primary_topic != "theory"
