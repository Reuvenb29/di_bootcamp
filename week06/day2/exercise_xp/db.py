# db.py
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="restaurant_db",
        user="postgres",              # change if you use another user
        password="1234",
        host="localhost",
        port="5432"
    )
