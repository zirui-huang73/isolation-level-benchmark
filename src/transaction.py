from psycopg2 import *
import random
import time

class Transaction(object):
    def __init__(self, conn, transaction_1, transaction_2):
        self.conn = conn
        self.transaction_1 = transaction_1
        self.transaction_2 = transaction_2
        self.elapsed_time = -1
        self.num_retry = 0
        self.return_status = "fail"

    def exec(self):
        rand = random.randint(0, 1)
        start_time = time.perf_counter()
        while True:
            try:
                cur = self.conn.cursor()
                cur.execute('begin')
                if (rand == 0):
                    for sql in self.transaction_1:
                        cur.execute(sql)
                else:
                    for sql in self.transaction_2:
                        cur.execute(sql)
                self.conn.commit()
                self.elapsed_time = time.perf_counter() - start_time
                self.conn.close()
                self.return_status = "pass"
                break
            except OperationalError as error:
                self.conn.rollback()
                self.num_retry += 1
                print("get operational error {}".format(error))
                continue
            except (Exception, DatabaseError) as error:
                print("get other error {}".format(error))
                break

        return { 'elapsed_time_second': self.elapsed_time, 'num_retry': self.num_retry, 'return_status': self.return_status }

