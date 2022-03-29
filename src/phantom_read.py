import random
from psycopg2 import *
from .transaction import Transaction

very_large_id_range = (10 ** 8, 10 ** 9)

class transaction1(Transaction):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute("select * from cal where z = 'male'")
        cur.execute("select * from cal where z = 'male'")
        cur.execute('commit')
        cur.close()

class transaction2(Transaction):
    def __init__(self, conn):
        super().__init__(conn)
        
    def process(self):
        rnd = random.randint(very_large_id_range[0], very_large_id_range[1])
        cur = self.conn.cursor()
        cur.execute('begin')
        cur.execute("INSERT INTO cal (id, x, y, z) VALUES(%s, %s, %s, %s)", (rnd, 100, 100, 'male'))
        cur.execute('commit')
        cur.close()
