import sys, psycopg2, random, json, os, logging
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
    'RC': 'READ COMMITTED',
    'RR': 'REPEATABLE READ',
    'S': 'Serializable'
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

    N = 10

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        isolationLevel = isolationMap[IL]
        conn.set_session(isolation_level=isolationLevel, autocommit=False)

        TransactionClasses = TransactionClassMap[TYPE]

        result = {}
        for i in range(N):
            index = random.randint(0, len(TransactionClasses) - 1)
            TransactionClass = TransactionClasses[index]
            transaction = TransactionClass(conn)
            result[i] = transaction.exec()

        # write results to json file
        dirPath = 'logs/{0}'.format(startTime)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open('{0}/{1}.json'.format(dirPath, iteration), 'w') as outputFile:
            json.dump(result, outputFile)

    except (Exception, psycopg2.DatabaseError) as error:
        logging.exception(error)
    finally:
        if conn is not None:
            conn.close()


