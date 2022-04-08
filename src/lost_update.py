from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = %s', (table_id,))
        x1 = cur.fetchone()[0]
        cur.execute('update cal set x = x - 10 where id = %s', (table_id,))

        # check correctness
        cur.execute('select x from cal where id = %s', (table_id,))
        x2 = cur.fetchone()[0]
        self.correct = (x2 == x1 - 10)

        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)
        
    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = %s', (table_id,))

        x1 = cur.fetchone()[0]
        cur.execute('update cal set x = x - 20 where id = %s', (table_id,))
        # check correctness
        cur.execute('select x from cal where id = %s', (table_id,))
        x2 = cur.fetchone()[0]
        self.correct = (x2 == x1 - 20)

        self.conn.commit()
        cur.close()
