from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

def main():
    src = RAW / "raw_total_fight_data.csv"
    dst = RAW / "ufc_raw.csv"
    if not src.exists():
        raise FileNotFoundError(src)
    shutil.copyfile(src, dst)
    print(dst)

if __name__ == "__main__":
    main()