from psycopg2 import *
import time
import logging

class Transaction(object):
    def __init__(self, isolationLevel):
        self.elapsed_time = -1
        self.num_retry = 0
        self.succeed = False
        self.correct = True
        self.isolationLevel = isolationLevel
        self.conn = None

    def process(self, cal_id):
        raise NotImplementedError()

    def exec(self, txn_id, queue, connect_params):
        self.conn = connect(**connect_params)
        self.conn.set_session(autocommit=False)
        self.conn.set_isolation_level(self.isolationLevel)
        table_id = txn_id.split("-")[0]
        start_time = time.perf_counter()
        while True:
            try:
                self.process(table_id)
                self.succeed = True
                break
            except OperationalError as error:
                self.conn.rollback()
                self.num_retry += 1

                if self.isolationLevel == "RC":
                    if self.num_retry == 3:
                        logging.error("RC fail with too much retry(4)")
                        break
                if self.isolationLevel == "RR":
                    if self.num_retry == 5:
                        logging.error("RR fail with too much retry(5)")
                        break
                if self.isolationLevel == "S":
                    if self.num_retry == 20:
                        logging.error("S fail with too much retry(15)")
                        break

                # sleep_time: float = (2 ** self.num_retry) * 0.1
                sleep_time = 0.1
                time.sleep(0.1)
                logging.warning("get operational error {}, sleep {} seconds".format(error, sleep_time))
                continue
            except (Exception, DatabaseError) as error:
                logging.warning("get other error {}".format(error))
                break

        self.elapsed_time = time.perf_counter() - start_time

        stats = { 'elapsed_time_second': self.elapsed_time,
                 'num_retry': self.num_retry,
                 'succeed': self.succeed,
                 'correct': self.correct}

        ret = queue.get()
        ret[txn_id] = stats
        queue.put(ret)