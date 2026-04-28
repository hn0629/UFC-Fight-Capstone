from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SILVER = ROOT / "data" / "silver"
GOLD = ROOT / "data" / "gold"

def main():
    df = pd.read_csv(SILVER / "ufc_silver.csv")
    if set(["weight_class", "method"]).issubset(df.columns):
        out_df = df.groupby(["weight_class", "method"], dropna=False).size().reset_index(name="fight_count")
    else:
        out_df = pd.DataFrame({"message": ["required columns missing"]})
    GOLD.mkdir(parents=True, exist_ok=True)
    out = GOLD / "gold_fight_summary.csv"
    out_df.to_csv(out, index=False)
    print(out)

if __name__ == "__main__":
    main()