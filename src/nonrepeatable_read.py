from psycopg2 import *

def transaction1(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select creatby from post where id = 1')
        cur.execute('select creatby from post where id = 1')
        cur.execute('commit')
        cur.close()
        print('success1')
    except (Exception, DatabaseError) as error:
        print(error)

def transaction2(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('update post set createdby = 100 where id = 1')
        cur.execute('commit')
        cur.close()
        print('success2')
    except (Exception, DatabaseError) as error:
        print(error)

