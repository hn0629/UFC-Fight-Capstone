from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SILVER = ROOT / "data" / "silver"

def main():
    df = pd.read_csv(RAW / "ufc_raw.csv")
    df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
    df = df.drop_duplicates()
    SILVER.mkdir(parents=True, exist_ok=True)
    out = SILVER / "ufc_silver.csv"
    df.to_csv(out, index=False)
    print(out)

if __name__ == "__main__":
    main()