from .transaction import Transaction


class transaction1(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)

    # constraint: x + y = 100
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')
        x = cur.fetchone()[0]
        cur.execute('select y from cal where id = 1')
        y = cur.fetchone()[0]
        self.correct = (x + y == 100)
        self.conn.commit()
        cur.close()


class transaction2(Transaction):
    def __init__(self, conn, isolationLevel):
        super().__init__(conn, isolationLevel)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('update cal set x = 25 where id = 1')
        cur.execute('update cal set y = 75 where id = 1')
        self.conn.commit()
        cur.close()