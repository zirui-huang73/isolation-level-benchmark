from .transaction import Transaction
import time

class transaction1(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = %s', (table_id,))
        res1 = cur.fetchone()
        cur.execute('select x from cal where id = %s', (table_id,))
        res2 = cur.fetchone()
        self.correct = (res1 == res2)
        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)
        
    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('update cal set x = 100 where id = %s', (table_id,))
        self.conn.commit()
        cur.close()

