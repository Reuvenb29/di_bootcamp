# api_to_db.py
# Single-file solution for: Web API -> DB (REST Countries)
# - Creates table if missing
# - Fetches countries from REST Countries API
# - Inserts 10 random countries (skips duplicates by name)

import random
import requests
import psycopg2

# ====== EDIT THESE 5 LINES FOR YOUR LOCAL POSTGRES ======
DB_NAME = "restaurant_db"   # or any DB you want to use
DB_USER = "postgres"
DB_PASS = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
# ========================================================

API_URL = "https://restcountries.com/v3.1/all"
FIELDS = "name,capital,subregion,population,flag,flags"

def get_conn():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS,
        host=DB_HOST, port=DB_PORT
    )

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS countries (
  country_id  SERIAL PRIMARY KEY,
  name        VARCHAR(100) NOT NULL UNIQUE,
  capital     VARCHAR(150),
  flag        VARCHAR(200),
  subregion   VARCHAR(100),
  population  BIGINT
);
"""

INSERT_SQL = """
INSERT INTO countries (name, capital, flag, subregion, population)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (name) DO NOTHING;
"""

def ensure_table():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)

def fetch_all_countries():
    r = requests.get(f"{API_URL}?fields={FIELDS}", timeout=30)
    r.raise_for_status()
    return r.json()

def normalize(country):
    name = (country.get("name", {}).get("common") or "").strip()
    caps = country.get("capital") or []
    capital = caps[0].strip() if isinstance(caps, list) and caps else ""
    # Prefer emoji flag; fall back to PNG/SVG URL
    flag_emoji = country.get("flag") or ""
    flags_obj = country.get("flags") or {}
    flag_url = flags_obj.get("png") or flags_obj.get("svg") or ""
    flag = flag_emoji or flag_url
    subregion = (country.get("subregion") or "").strip()
    population = int(country.get("population") or 0)
    return (name, capital, flag, subregion, population)

def insert_rows(rows):
    inserted = 0
    with get_conn() as conn:
        with conn.cursor() as cur:
            for row in rows:
                cur.execute(INSERT_SQL, row)
                inserted += cur.rowcount  # 1 if inserted, 0 if skipped
    return inserted

def main():
    ensure_table()
    data = fetch_all_countries()
    if not data:
        print("No data from API.")
        return

    sample = random.sample(data, 10)
    rows = [normalize(c) for c in sample]
    added = insert_rows(rows)
    print(f"Attempted to add 10 countries; actually inserted: {added}")

    # Show a few rows so there’s visible output
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name, capital, subregion, population, flag
                FROM countries
                ORDER BY name
                LIMIT 10;
            """)
            for name, capital, subregion, population, flag in cur.fetchall():
                print(f"- {name} | {capital or '—'} | {subregion or '—'} | {population:,} | {flag}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
