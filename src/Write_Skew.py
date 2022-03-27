from psycopg2 import *
from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        cur.execute('update cal set t = 60 where id = 1')
        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select y from cal where id = 1')
        cur.execute('update cal set x = 50 where id = 1')
        self.conn.commit()
        cur.close()
