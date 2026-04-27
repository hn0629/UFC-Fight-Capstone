import logging
import sqlite3

import pandas as pd

from config import SILVER_DIR
from scripts.utils import get_sqlite_connection, ensure_directories, bootstrap_logging


LOGGER = logging.getLogger(__name__)


def load_silver_to_sqlite(table_name: str = "ufc_silver") -> None:
    ensure_directories()
    silver_path = SILVER_DIR / "ufc_silver.csv"
    df = pd.read_csv(silver_path)

    conn = get_sqlite_connection()
    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        LOGGER.info("Loaded %s records into SQLite table %s", len(df), table_name)
    finally:
        conn.close()


if __name__ == "__main__":
    bootstrap_logging()
    load_silver_to_sqlite()