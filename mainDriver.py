import sys, psycopg2, random, json, os, logging
import multiprocessing
from init import config
from src import lost_update, phantom_read, nonrepeatable_read, read_skew, write_skew

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

TransactionClassMap = {
    'LU': [lost_update.transaction1, lost_update.transaction2],
    'PR': [phantom_read.transaction1, phantom_read.transaction2],
    'NR': [nonrepeatable_read.transaction1, nonrepeatable_read.transaction2],
    'RS': [read_skew.transaction1, read_skew.transaction2],
    'WS': [write_skew.transaction1, write_skew.transaction2],
}

isolationMap = {
    'RC': psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED,
    'RR': psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ,
    'S': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE
}

"""
@:param1: Anomaly Type
    Lost-Update
    Non-Repeatable-Read
    Phantom-Read
    Read-Skew
    Write-Skew
@:param2: Isolation Level
    RC: read committed
    RR: repeatable read
    S:  serializable
"""
if __name__ == '__main__':

    TYPE = sys.argv[1]          # anomaly type
    IL = sys.argv[2]            # isolation level
    startTime = sys.argv[3]
    iteration = sys.argv[4]
    # logFileName = sys.argv[3]            # ID passed from shell script

    N = 1

    conn = None
    try:
        params = config()
        # conn = psycopg2.connect(**params)
        # conn.set_session(autocommit=False)

        isolationLevel = isolationMap[IL]
        TransactionClasses = TransactionClassMap[TYPE]

        ret = {}
        queue = multiprocessing.Queue()
        queue.put(ret)
        for i in range(N):
            # i represent the id
            TransactionClass1 = TransactionClasses[0]
            TransactionClass2 = TransactionClasses[1]

            txn1 = TransactionClass1(isolationLevel)
            txn2 = TransactionClass2(isolationLevel)

            # Transaction.exec() takes two arguments: transaction id (i-1, i-2), result dict)
            job1 = multiprocessing.Process(target=txn1.exec, args=(str(i+1)+"-1", queue, params))
            job2 = multiprocessing.Process(target=txn2.exec, args=(str(i+1)+"-2", queue, params))
            job1.start()
            job2.start()

            job1.join()
            job2.join()

        # write results to json file
        dirPath = 'logs/{0}'.format(startTime+str(random.randint(1, 100)))
        result = queue.get()
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open('{0}/{1}.json'.format(dirPath, iteration), 'w') as outputFile:
            json.dump(result, outputFile)

    except (Exception, psycopg2.DatabaseError) as error:
        logging.exception(error)
    finally:
        if conn is not None:
            conn.close()




