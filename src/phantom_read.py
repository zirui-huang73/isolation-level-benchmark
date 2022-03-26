from psycopg2 import *

def transaction1(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select * from count where cash = 100')
        cur.execute('select * from count where cash = 100')
        cur.execute('commit')
        cur.close()
        print('success1')
    except (Exception, DatabaseError) as error:
        print(error)

def transaction2(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select max(id) from post')
        last_id = 0
        row = cur.fetchone()
        if row[0]:
            last_id = row[0]
        cur.execute("INSERT INTO post (id, createdby) VALUES(%s, %s)", (last_id+1, 1))
        cur.execute('commit')
        cur.close()
        print('success2')
    except (Exception, DatabaseError) as error:
        print(error)

