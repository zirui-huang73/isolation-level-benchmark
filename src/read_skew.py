from .transaction import Transaction


class transaction1(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    # constraint: x + y = 100
    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')

        cur.execute('select y from cal where id = %s', (table_id,))
        y = cur.fetchone()[0]
        if y == 0:
            self.correct = True
            return

        cur.execute('select x from cal where id = %s', (table_id,))
        x = cur.fetchone()[0]
        cur.execute('select y from cal where id = %s', (table_id,))
        y = cur.fetchone()[0]
        self.correct = (y != 0)
        self.conn.commit()
        cur.close()


class transaction2(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute('update cal set y = 0 where id = %s', (table_id,))
        self.conn.commit()
        cur.close()