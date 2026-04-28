from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SILVER = ROOT / "data" / "silver"
DB = ROOT / "data" / "ufc.db"

def main():
    conn = sqlite3.connect(DB)
    try:
        silver = pd.read_csv(SILVER / "ufc_silver.csv")
        silver.to_sql("ufc_silver", conn, if_exists="replace", index=False)
        print(DB)
    finally:
        conn.close()

if __name__ == "__main__":
    main()