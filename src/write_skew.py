from .transaction import Transaction

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    # constraint: x + y <= 100
    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select x from cal where id = 1')  # get x = 30
        x = cur.fetchone()[0]
        cur.execute('update cal set y = 60 where id = 1')

        # check correctness
        cur.execute('select y from cal where id = 1')
        y = cur.fetchone()[0]
        self.correct = (x + y <= 100)

        self.conn.commit()
        cur.close()


class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('select y from cal where id = 1')  # get y = 10
        y = cur.fetchone()[0]
        cur.execute('update cal set x = 50 where id = 1')

        # check correctness
        cur.execute('select x from cal where id = 1')
        x = cur.fetchone()[0]
        self.correct = (x + y <= 100)

        self.conn.commit()
        cur.close()