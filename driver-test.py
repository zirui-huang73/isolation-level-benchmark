import psycopg2
from init import config


if __name__ == '__main__':
    conn = None

    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




