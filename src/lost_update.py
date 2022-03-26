from psycopg2 import *

def transaction1(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select createdby from post where id = 1')
        cur.execute('update post set createdby = 50 where id = 1')
        cur.execute('commit')
        cur.close()
        print('success1')
    except (Exception, DatabaseError) as error:
        print(error)

def transaction2(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select createdby from post where id = 1')
        cur.execute('update post set createdby = 80 where id = 1')
        cur.execute('commit')
        cur.close()
        print('success2')
    except (Exception, DatabaseError) as error:
        print(error)

