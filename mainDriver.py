import sys
import psycopg2
from init import config
from src import lost_update, phantom_read

functionMap = {
    'Lost-Update': [lost_update.transaction1, lost_update.transaction2],
    'Phantom-Read': [phantom_read.transaction1, phantom_read.transaction2],
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

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        isolationLevel = isolationMap[IL]
        funcs = functionMap[TYPE]

        conn.set_session(isolation_level=isolationLevel, autocommit=False)
        for func in funcs:
            func(conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



