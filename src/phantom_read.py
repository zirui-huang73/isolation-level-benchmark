from psycopg2 import *
from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select * from cal where x = 100')
        cur.execute('select * from cal where x = 100')
        cur.execute('commit')
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select max(id) from cal')
        last_id = 0
        row = cur.fetchone()
        if row[0]:
            last_id = row[0]
        cur.execute("INSERT INTO cal (id, x, y) VALUES(%s, %s, %s)", (last_id+1, 100, 100))
        cur.execute('commit')
        cur.close()
