import sqlite3

from config import DB_PATH


def list_tables() -> list[str]:
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        return [row[0] for row in cursor.fetchall()]
    finally:
        conn.close()


if __name__ == "__main__":
    tables = list_tables()
    if not tables:
        print("No tables found.")
    else:
        print("Tables in ufc.db:")
        for table in tables:
            print(f"- {table}")