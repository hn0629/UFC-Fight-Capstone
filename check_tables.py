from pathlib import Path
import sqlite3

DB = Path(__file__).resolve().parent / "data" / "ufc.db"

def main():
    conn = sqlite3.connect(DB)
    try:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        rows = [r[0] for r in cur.fetchall()]
        if not rows:
            print("No tables found.")
        else:
            for name in rows:
                print(name)
    finally:
        conn.close()

if __name__ == "__main__":
    main()