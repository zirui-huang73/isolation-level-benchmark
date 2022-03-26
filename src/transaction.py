from psycopg2 import *
import time

class Transaction(object):
    def __init__(self, conn):
        self.conn = conn
        self.elapsed_time = -1
        self.num_retry = 0
        self.return_status = False

    def process(self):
        pass

    def exec(self):
        start_time = time.perf_counter()
        while True:
            try:
                self.elapsed_time = time.perf_counter() - start_time
                if self.num_retry == 3:
                    raise Exception("fail with too much retry(3 times)")
                self.process()
                self.return_status = True
                break
            except OperationalError as error:
                self.conn.rollback()
                self.num_retry += 1
                sleep_time: float = self.num_retry * 0.1
                time.sleep(sleep_time)
                print("get operational error {}, sleep {} seconds".format(error, sleep_time))
                continue
            except (Exception, DatabaseError) as error:
                print("get other error {}".format(error))
                break

        return { 'elapsed_time_second': self.elapsed_time, 'num_retry': self.num_retry, 'return_status': self.return_status }

