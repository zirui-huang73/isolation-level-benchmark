import sys
import psycopg2
from init import config
from src import lost_update
import random

"""
@:param1: Anomaly Type
    Lost-Update
    ...
@:param2: Isolation Level
    RC: read committed
    RR: repeatable read
    S:  serializable
"""
if __name__ == '__main__':

    TYPE = sys.argv[1]
    IL = sys.argv[2]
    # print(TYPE)
    # print(IL)
    conn = None

    try:
        params = config()

        conn = psycopg2.connect(**params)

        if IL == 'RC':
            conn.set_session(isolation_level='READ COMMITTED', autocommit=False)
        elif IL == 'RR':
            conn.set_session(isolation_level='REPEATABLE READ', autocommit=False)
        elif IL == 'S':
            conn.set_session(isolation_level='SERIALIZABLE', autocommit=False)
        else:
            raise Exception('Isolation level {0} not known'.format(IL))

        if TYPE == 'Lost-Update':
            lost_update.run(conn)
        else:
            raise Exception('Anomaly type {0} not known'.format(TYPE))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



