from .transaction import Transaction
import time

class transaction1(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        res1 = cur.fetchone()
        cur.execute('select x from cal where id = 1')
        res2 = cur.fetchone()
        self.correct = (res1 == res2)
        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('update cal set x = 100 where id = 1')
        self.conn.commit()
        cur.close()

