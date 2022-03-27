from psycopg2 import *
from .transaction import Transaction
import time

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        time.sleep(0.1)
        cur.execute('select x from cal where id = 1')
        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('update cal set x = 100 where id = 1')
        self.conn.commit()
        cur.close()

# def transaction1(conn):
#     try:
#         cur = conn.cursor()
#         cur.execute('begin')

#         cur.execute('select x from cal where id = 1')
#         cur.execute('select x from cal where id = 1')
#         cur.execute('commit')
#         cur.close()
#         print('success1')
#     except (Exception, DatabaseError) as error:
#         print(error)

# def transaction2(conn):
#     try:
#         cur = conn.cursor()
#         cur.execute('begin')
#         cur.execute('update cal set x = 100 where id = 1')
#         cur.execute('commit')
#         cur.close()
#         print('success2')
#     except (Exception, DatabaseError) as error:
#         print(error)

