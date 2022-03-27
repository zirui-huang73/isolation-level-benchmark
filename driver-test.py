import psycopg2
from init import config
import logging

def get_conn():
    params = config()

    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    logging.info(db_version)

if __name__ == '__main__':
    conn = None

    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        logging.info(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        if conn is not None:
            conn.close()




