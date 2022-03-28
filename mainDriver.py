import sys
import psycopg2
from init import config
from src import lost_update, phantom_read, nonrepeatable_read, Read_Skew, Write_Skew
import random
import json
import os
from datetime import datetime
import logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

TransactionClassMap = {
    'LU': [lost_update.transaction1, lost_update.transaction2],
    'PR': [phantom_read.transaction1, phantom_read.transaction2],
    'NR': [nonrepeatable_read.transaction1, nonrepeatable_read.transaction2],
    'RS': [Read_Skew.transaction1, Read_Skew.transaction2],
    'WS': [Write_Skew.transaction1, Write_Skew.transaction2],
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
        if not os.path.exists('logs'):
            os.makedirs('logs')
        date_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        with open('logs/{0}-{1}-{2}.json'.format(TYPE, IL, date_time), 'w') as outputFile:
            json.dump(result, outputFile)

    except (Exception, psycopg2.DatabaseError) as error:
        logging.exception(error)
    finally:
        if conn is not None:
            conn.close()


