from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from .config import Config
from .pipeline import run as run_pipeline
from .state import State


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )


def _write(cfg: Config, md: str, date: str) -> Path:
    year = date[:4]
    out_dir = cfg.out_dir / year
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{date}.md"
    path.write_text(md, encoding="utf-8")
    if cfg.main.get("output", {}).get("write_latest", True):
        (cfg.out_dir / "latest.md").write_text(md, encoding="utf-8")
    return path


def cmd_run(args) -> int:
    cfg = Config.load(args.root)
    md, meta = run_pipeline(
        cfg,
        mode=args.mode,
        use_llm=not args.no_llm,
        dry_run=args.dry_run,
        author_window_days=args.author_days,
        limit=args.limit,
        sources=set(args.source) if args.source else None,
        date=args.date,
        from_raw=getattr(args, "from_raw", False),
    )
    if args.stdout or args.dry_run:
        print(md)
    if not args.dry_run:
        path = _write(cfg, md, meta["date"])
        print(f"\n✅ 已写入 {path}  （扫描 {meta['n_fetched']} 条 → 入选 {meta['n_selected']} 条）",
              file=sys.stderr)
    for e in meta.get("errors", []):
        print(f"⚠️  {e}", file=sys.stderr)
    return 0


def cmd_backfill(args) -> int:
    args.mode = "backfill"
    args.author_days = args.days
    args.date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"补课模式：把关注名单里所有人近 {args.days} 天的工作捞一遍…", file=sys.stderr)
    return cmd_run(args)


def cmd_stats(args) -> int:
    cfg = Config.load(args.root)
    st = State(cfg.db_path)
    s = st.stats()
    print(f"已见条目 : {s['total_seen']}")
    print(f"已推送   : {s['reported']}")
    print(f"运行次数 : {s['runs']}")
    if s["by_topic"]:
        print("\n按领域：")
        for tid, n in s["by_topic"]:
            t = cfg.topic_by_id(tid or "misc")
            print(f"  {t.get('emoji','📄')} {t.get('name_zh', tid):<24} {n}")
    st.close()
    return 0


def cmd_check(args) -> int:
    """逐个源做连通性检查，不写任何状态。"""
    import feedparser

    from .util import fetch
    cfg = Config.load(args.root)
    ok = True

    print("→ arXiv API …", end=" ", flush=True)
    r = fetch("http://export.arxiv.org/api/query",
              params={"search_query": "cat:cs.AI", "max_results": 1}, timeout=30)
    print("OK" if r and "<entry" in r else "失败")
    ok &= bool(r and "<entry" in r)

    print("→ HF Daily Papers …", end=" ", flush=True)
    r = fetch("https://huggingface.co/api/daily_papers", params={"limit": 1}, timeout=20)
    print("OK" if r and r.strip().startswith("[") else "失败")

    for f in cfg.sources.get("rss", {}).get("feeds", []):
        print(f"→ RSS {f['name']:<26}", end=" ", flush=True)
        raw = fetch(f["url"], timeout=20, retries=1)
        if raw is None:
            print("抓取失败 ❌")
            continue
        n = len(getattr(feedparser.parse(raw), "entries", []) or [])
        print(f"OK ({n} 条)" if n else "无条目 ⚠️")

    for pg in cfg.sources.get("pagewatch", {}).get("pages", []):
        print(f"→ 页面 {pg['name']:<25}", end=" ", flush=True)
        r = fetch(pg["url"], timeout=20)
        print(f"OK ({len(r)} 字节)" if r else "失败")

    return 0 if ok else 1


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="aidigest", description="每日 AI 前沿雷达")
    p.add_argument("--root", default=".", help="仓库根目录（含 config/）")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_run_args(sp):
        sp.add_argument("--no-llm", action="store_true", help="跳过 Claude 摘要")
        sp.add_argument("--dry-run", action="store_true", help="只打印，不写文件也不记状态")
        sp.add_argument("--stdout", action="store_true", help="同时打印到标准输出")
        sp.add_argument("--limit", type=int, help="最多保留多少条")
        sp.add_argument("--date", help="指定 digest 日期 YYYY-MM-DD")
        sp.add_argument("--source", action="append",
                        choices=["arxiv", "hf", "rss", "pagewatch"], help="只跑指定源（可重复）")
        sp.add_argument("--from-raw", action="store_true",
                        help="复用上次抓取的原始数据（调打分权重时用，不联网）")

    r = sub.add_parser("run", help="跑一轮，生成当日简报")
    add_run_args(r)
    r.add_argument("--author-days", type=int, help="覆盖关注名单的回溯天数")
    r.set_defaults(func=cmd_run, mode="daily")

    b = sub.add_parser("backfill", help="补课：把关注名单近 N 天的工作全捞一遍")
    add_run_args(b)
    b.add_argument("--days", type=int, default=180)
    b.set_defaults(func=cmd_backfill)

    s = sub.add_parser("stats", help="看积累了多少")
    s.set_defaults(func=cmd_stats)

    c = sub.add_parser("check", help="检查各数据源是否通")
    c.set_defaults(func=cmd_check)

    args = p.parse_args(argv)
    _setup_logging(args.verbose)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
