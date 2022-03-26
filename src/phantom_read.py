from psycopg2 import *

def transaction1(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select * from cal where x = 100')
        cur.execute('select * from cal where x = 100')
        cur.execute('commit')
        cur.close()
        print('success1')
    except OperationalError as error:
        print("get operational error {}".format(error))
    except (Exception, DatabaseError) as error:
        print(error)

def transaction2(conn):
    try:
        cur = conn.cursor()
        cur.execute('begin')
        cur.execute('select max(id) from cal')
        last_id = 0
        row = cur.fetchone()
        if row[0]:
            last_id = row[0]
        cur.execute("INSERT INTO cal (id, x, y) VALUES(%s, %s, %s)", (last_id+1, 100, 100))
        cur.execute('commit')
        cur.close()
        print('success2')
    except (Exception, DatabaseError) as error:
        print(error)

