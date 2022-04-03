from psycopg2 import *
import time
import logging

class Transaction(object):
    def __init__(self, conn, isolationLevel):
        self.conn = conn
        self.elapsed_time = -1
        self.num_retry = 0
        self.succeed = False
        self.correct = True
        conn.set_isolation_level(isolationLevel)

    def process(self):
        raise NotImplementedError()

    def exec(self):
        start_time = time.perf_counter()
        while True:
            try:
                self.process()
                self.succeed = True
                break
            except OperationalError as error:
                self.conn.rollback()
                self.num_retry += 1
                if self.num_retry == 4:
                    logging.error("fail with too much retry(4 times)")
                    break
                sleep_time: float = (2 ** self.num_retry) * 0.1
                time.sleep(sleep_time)
                logging.warning("get operational error {}, sleep {} seconds".format(error, sleep_time))
                continue
            except (Exception, DatabaseError) as error:
                logging.warning("get other error {}".format(error))
                break

        self.elapsed_time = time.perf_counter() - start_time
        return { 'elapsed_time_second': self.elapsed_time,
                 'num_retry': self.num_retry,
                 'succeed': self.succeed,
                 'correct': self.correct}

