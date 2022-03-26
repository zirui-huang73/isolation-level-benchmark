from psycopg2 import *
from .transaction import Transaction

def run(conn):
    transaction_1 = ['select cash from count where id = 1', 'update count set cash = 50 where id = 1']
    transaction_2 = ['select cash from count where id = 1', 'update count set cash = 80 where id = 1']
    transaction = Transaction(conn=conn, transaction_1=transaction_1, transaction_2=transaction_2)
    result = transaction.exec()
    print(result)
