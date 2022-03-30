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

