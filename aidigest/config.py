from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


def _load(p: Path) -> dict[str, Any]:
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@dataclass
class Config:
    root: Path
    main: dict
    topics: dict
    watchlist: dict
    sources: dict

    @classmethod
    def load(cls, root: str | Path = ".") -> "Config":
        root = Path(root).resolve()
        cfg = root / "config"
        return cls(
            root=root,
            main=_load(cfg / "config.yaml"),
            topics=_load(cfg / "topics.yaml"),
            watchlist=_load(cfg / "watchlist.yaml"),
            sources=_load(cfg / "sources.yaml"),
        )

    # 便捷访问
    @property
    def out_dir(self) -> Path:
        return self.root / self.main.get("output", {}).get("dir", "digests")

    @property
    def db_path(self) -> Path:
        return self.root / self.main.get("state", {}).get("db_path", ".state/seen.sqlite3")

    @property
    def language(self) -> str:
        return self.main.get("output", {}).get("language", "zh")

    def topic_by_id(self, tid: str) -> dict:
        for t in self.topics.get("topics", []):
            if t["id"] == tid:
                return t
        return {"id": tid, "name_zh": tid, "name_en": tid, "emoji": "📄"}
