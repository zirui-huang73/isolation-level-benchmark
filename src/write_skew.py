import time

from .transaction import Transaction


class transaction1(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    # constraint: x + y <= 100
    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')

        # cur.execute('update cal set y = 60 where id = %s', (table_id,))
        cur.execute('select y from cal where id = %s', (table_id,))  # get x = 30
        y = cur.fetchone()[0]
        if y == 0:
            self.correct = True
        else:
            cur.execute('update cal set x = 0 where id = %s', (table_id,))
            cur.execute('select x from cal where id = %s', (table_id,))  # get x = 30
            x = cur.fetchone()[0]
            cur.execute('select y from cal where id = %s', (table_id,))  # get x = 30
            y = cur.fetchone()[0]
            self.correct = (x + y != 0)

        self.conn.commit()
        cur.close()

        # x = 0, y = 100


class transaction2(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        # cur.execute('select y from cal where id = %s', (table_id,))  # get y = 10
        # y = cur.fetchone()[0]
        # cur.execute('update cal set x = 50 where id = %s', (table_id,))

        cur.execute('update cal set y = 0 where id = %s', (table_id,))

        self.correct = True
        self.conn.commit()
        cur.close()
