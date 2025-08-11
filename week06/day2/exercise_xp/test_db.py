# test_db.py
from db import get_connection

def main():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                print("Postgres:", cur.fetchone()[0])

                cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema='public'
                    ORDER BY table_name;
                """)
                print("Tables:", [r[0] for r in cur.fetchall()])

                cur.execute("""
                    SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_name='menu_items'
                    ORDER BY ordinal_position;
                """)
                print("menu_items columns:", cur.fetchall())
        print("✅ Connection OK")
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    main()
