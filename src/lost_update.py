from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        x1 = cur.fetchone()[0]

        cur.execute('update cal set x = x - 10 where id = 1')

        # check correctness
        cur.execute('select x from cal where id = 1')
        x2 = cur.fetchone()[0]
        self.correct = (x2 == x1 - 10)

        self.conn.commit()
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)
        
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        x1 = cur.fetchone()[0]
        cur.execute('update cal set x = x - 20 where id = 1')

        # check correctness
        cur.execute('select x from cal where id = 1')
        x2 = cur.fetchone()[0]
        self.correct = (x2 == x1 - 20)

        self.conn.commit()
        cur.close()
