from __future__ import annotations

import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS seen (
    uid           TEXT PRIMARY KEY,
    source        TEXT,
    title         TEXT,
    url           TEXT,
    published     TEXT,
    first_seen    TEXT,
    reported_on   TEXT,          -- 首次出现在 digest 里的日期
    upvotes       INTEGER DEFAULT 0,
    score         REAL DEFAULT 0,
    topic         TEXT
);
CREATE TABLE IF NOT EXISTS pagewatch_links (
    page       TEXT,
    url        TEXT,
    title      TEXT,
    first_seen TEXT,
    PRIMARY KEY (page, url)
);
CREATE TABLE IF NOT EXISTS runs (
    run_at     TEXT PRIMARY KEY,
    mode       TEXT,
    n_fetched  INTEGER,
    n_new      INTEGER,
    notes      TEXT
);
CREATE INDEX IF NOT EXISTS idx_seen_reported ON seen(reported_on);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class State:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        with closing(self.conn.cursor()) as c:
            c.executescript(SCHEMA)
        self.conn.commit()

    # ---------- seen ----------
    def get(self, uid: str) -> sqlite3.Row | None:
        cur = self.conn.execute("SELECT * FROM seen WHERE uid = ?", (uid,))
        return cur.fetchone()

    def is_reported(self, uid: str) -> bool:
        row = self.get(uid)
        return bool(row and row["reported_on"])

    def upvotes_of(self, uid: str) -> int:
        row = self.get(uid)
        return int(row["upvotes"]) if row else 0

    def record_seen(self, item, reported_on: str | None = None) -> None:
        existing = self.get(item.uid)
        if existing:
            self.conn.execute(
                "UPDATE seen SET upvotes = MAX(upvotes, ?), score = ?, topic = ?, "
                "reported_on = COALESCE(reported_on, ?) WHERE uid = ?",
                (item.upvotes, item.score, item.primary_topic, reported_on, item.uid),
            )
        else:
            self.conn.execute(
                "INSERT INTO seen (uid, source, title, url, published, first_seen, "
                "reported_on, upvotes, score, topic) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    item.uid, item.source, item.title, item.url,
                    item.published.isoformat(), _now(), reported_on,
                    item.upvotes, item.score, item.primary_topic,
                ),
            )
        self.conn.commit()

    # ---------- pagewatch ----------
    def known_links(self, page: str) -> set[str]:
        cur = self.conn.execute("SELECT url FROM pagewatch_links WHERE page = ?", (page,))
        return {r["url"] for r in cur.fetchall()}

    def add_links(self, page: str, links: list[tuple[str, str]]) -> None:
        self.conn.executemany(
            "INSERT OR IGNORE INTO pagewatch_links (page, url, title, first_seen) VALUES (?,?,?,?)",
            [(page, u, t, _now()) for u, t in links],
        )
        self.conn.commit()

    def page_initialized(self, page: str) -> bool:
        cur = self.conn.execute("SELECT COUNT(*) n FROM pagewatch_links WHERE page = ?", (page,))
        return cur.fetchone()["n"] > 0

    # ---------- runs ----------
    def log_run(self, mode: str, n_fetched: int, n_new: int, notes: str = "") -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO runs (run_at, mode, n_fetched, n_new, notes) VALUES (?,?,?,?,?)",
            (_now(), mode, n_fetched, n_new, notes),
        )
        self.conn.commit()

    def stats(self) -> dict:
        cur = self.conn.execute(
            "SELECT COUNT(*) total, SUM(reported_on IS NOT NULL) reported FROM seen"
        )
        row = cur.fetchone()
        runs = self.conn.execute("SELECT COUNT(*) n FROM runs").fetchone()["n"]
        by_topic = self.conn.execute(
            "SELECT topic, COUNT(*) n FROM seen WHERE reported_on IS NOT NULL "
            "GROUP BY topic ORDER BY n DESC"
        ).fetchall()
        return {
            "total_seen": row["total"] or 0,
            "reported": row["reported"] or 0,
            "runs": runs,
            "by_topic": [(r["topic"], r["n"]) for r in by_topic],
        }

    def close(self) -> None:
        self.conn.close()
