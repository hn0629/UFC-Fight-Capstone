import logging

import pandas as pd

from config import RAW_DIR, SILVER_DIR, GOLD_DIR
from scripts.utils import ensure_directories, bootstrap_logging


LOGGER = logging.getLogger(__name__)


def validate_pipeline_outputs() -> bool:
    ensure_directories()
    checks = {
        "raw": RAW_DIR / "ufc_raw.csv",
        "silver": SILVER_DIR / "ufc_silver.csv",
        "gold": GOLD_DIR / "gold_fight_summary.csv",
    }

    valid = True
    for layer, path in checks.items():
        if not path.exists():
            LOGGER.error("Missing %s layer file: %s", layer, path)
            valid = False
            continue

        df = pd.read_csv(path)
        if df.empty:
            LOGGER.error("%s layer file is empty: %s", layer, path)
            valid = False
        else:
            LOGGER.info("%s layer validated with %s rows", layer, len(df))

    return valid


if __name__ == "__main__":
    bootstrap_logging()
    result = validate_pipeline_outputs()
    if not result:
        raise SystemExit(1)