from pathlib import Path

PROJECT_DIR = Path(r"C:\Users\harry\UFC Project")
DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
DOCS_DIR = PROJECT_DIR / "docs"
IMAGES_DIR = PROJECT_DIR / "images"
QUERIES_DIR = PROJECT_DIR / "queries"
SQL_DIR = PROJECT_DIR / "sql"
SCRIPTS_DIR = PROJECT_DIR / "scripts"
DAGS_DIR = PROJECT_DIR / "dags"
OUTPUT_DIR = PROJECT_DIR / "output"
AIRFLOW_HOME = PROJECT_DIR / "airflow_home"
DB_PATH = DATA_DIR / "ufc.db"
MONGO_DB_NAME = "UFC2022"