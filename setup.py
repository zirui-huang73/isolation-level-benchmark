import sys
import psycopg2
from init import config

if __name__ == '__main__':
    params = config()
    conn = psycopg2.connect(**params)
    conn.set_session(autocommit=True)
    with conn.cursor() as cur:
        cur.execute(open("sql/schema.sql", "r").read())
