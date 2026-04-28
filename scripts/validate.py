from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SILVER = ROOT / "data" / "silver"
GOLD = ROOT / "data" / "gold"

def main():
    checks = [RAW / "ufc_raw.csv", SILVER / "ufc_silver.csv", GOLD / "gold_fight_summary.csv"]
    ok = True
    for p in checks:
        if p.exists() and not pd.read_csv(p).empty:
            print(f"OK {p}")
        else:
            print(f"FAIL {p}")
            ok = False
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()