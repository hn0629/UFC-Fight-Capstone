import logging
from pathlib import Path

import pandas as pd

from config import RAW_DIR
from scripts.utils import ensure_directories, bootstrap_logging


LOGGER = logging.getLogger(__name__)


def ingest_source_csv(source_file: str | Path) -> Path:
    ensure_directories()
    source_path = Path(source_file)
    df = pd.read_csv(source_path)
    output_path = RAW_DIR / "ufc_raw.csv"
    df.to_csv(output_path, index=False)
    LOGGER.info("Raw data ingested to %s", output_path)
    return output_path


if __name__ == "__main__":
    bootstrap_logging()
    default_source = Path("UFC-Fight-Data-1993-2021-1.csv")
    if default_source.exists():
        ingest_source_csv(default_source)
    else:
        LOGGER.warning("Source CSV not found. Provide a valid input file path.")