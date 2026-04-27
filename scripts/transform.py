import logging
from pathlib import Path

import pandas as pd

from config import RAW_DIR, SILVER_DIR
from scripts.utils import ensure_directories, bootstrap_logging


LOGGER = logging.getLogger(__name__)


def transform_raw_to_silver() -> Path:
    ensure_directories()
    raw_path = RAW_DIR / "ufc_raw.csv"
    silver_path = SILVER_DIR / "ufc_silver.csv"

    df = pd.read_csv(raw_path)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.drop_duplicates()

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.strip()

    df.to_csv(silver_path, index=False)
    LOGGER.info("Silver data written to %s", silver_path)
    return silver_path


if __name__ == "__main__":
    bootstrap_logging()
    transform_raw_to_silver()