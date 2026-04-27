import logging
from pathlib import Path

import pandas as pd

from config import SILVER_DIR, GOLD_DIR
from scripts.utils import ensure_directories, bootstrap_logging


LOGGER = logging.getLogger(__name__)


def build_gold_layer() -> Path:
    ensure_directories()
    silver_path = SILVER_DIR / "ufc_silver.csv"
    gold_path = GOLD_DIR / "gold_fight_summary.csv"

    df = pd.read_csv(silver_path)

    if "weight_class" in df.columns and "method" in df.columns:
        gold_df = (
            df.groupby(["weight_class", "method"], dropna=False)
            .size()
            .reset_index(name="fight_count")
            .sort_values("fight_count", ascending=False)
        )
    else:
        gold_df = pd.DataFrame({"message": ["Required columns not found in silver dataset"]})

    gold_df.to_csv(gold_path, index=False)
    LOGGER.info("Gold layer written to %s", gold_path)
    return gold_path


if __name__ == "__main__":
    bootstrap_logging()
    build_gold_layer()