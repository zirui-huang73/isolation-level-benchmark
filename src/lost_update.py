from psycopg2 import *
from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select cash from count where id = 1')
        cur.execute('update count set cash = 50 where id = 1')
        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select cash from count where id = 1')
        cur.execute('update count set cash = 80 where id = 1')
        self.conn.commit()
        cur.close()