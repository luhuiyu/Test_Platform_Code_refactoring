import pandas as pd
from pymysqlpool import ConnectionPool


def local_mysql():
    config = {
        'pool_name': 'test',
        'host': '192.168.41.27',
        'port': 33061,
        'user': 'root',
        'password': '123456',
        'database': 'test_platform'}
    pool = ConnectionPool(**config)
    return pool
if __name__=='__main__':

    with local_mysql().cursor() as cursor:
        cursor.execute(' select name from web_platform_course  ')
        print(cursor.fetchall())

#print(connection_pool().cursor().execute(' select name from web_platform_course  ').fetchall())