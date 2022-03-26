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
        cur.execute('select max(id) from count')
        n = cur.fetone()
        cur.execute("INSERT INTO count (id, cash) VALUES(%s, %s)", (n+1, 100))
        cur.execute('commit')
        cur.close()
        print('success2')
    except (Exception, DatabaseError) as error:
        print(error)

