from pathlib import Path
import json
import sqlite3
from typing import Any

from config import RAW_DIR, SILVER_DIR, GOLD_DIR, DB_PATH
from logging_config import setup_logging


def ensure_directories() -> None:
    for path in [RAW_DIR, SILVER_DIR, GOLD_DIR, DB_PATH.parent]:
        Path(path).mkdir(parents=True, exist_ok=True)


def get_sqlite_connection() -> sqlite3.Connection:
    ensure_directories()
    return sqlite3.connect(DB_PATH)


def read_json(path: str | Path) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: Any, path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def bootstrap_logging():
    setup_logging()