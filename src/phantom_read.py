import random
from .transaction import Transaction
import time
import logging

very_large_id_range = (10 ** 8, 10 ** 9)

class transaction1(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)

    def process(self, table_id):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute("select * from cal where z = 'male'")
        res1 = cur.fetchall()
        cur.execute("select * from cal where z = 'male'")
        res2 = cur.fetchall()
        self.correct = (len(res1) == len(res2))
        cur.execute('commit')
        cur.close()

class transaction2(Transaction):
    def __init__(self, isolationLevel):
        super().__init__(isolationLevel)
        
    def process(self, table_id):
        rnd = random.randint(very_large_id_range[0], very_large_id_range[1])
        cur = self.conn.cursor()
        cur.execute('begin')
        # cur.execute("DELETE FROM cal WHERE id = %s", (rnd,))
        cur.execute('update cal set x = 0 where id = %s', (table_id,))
        cur.execute("INSERT INTO cal (id, x, y, z) VALUES(%s, %s, %s, %s)", (rnd, 100, 100, 'male'))
        cur.execute('commit')
        cur.close()
