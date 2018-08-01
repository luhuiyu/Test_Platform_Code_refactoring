import pandas as pd
from pymysqlpool import ConnectionPool

config = {
    'pool_name': 'test',
    'host': '192.168.41.27',
    'port': 33061,
    'user': 'root',
    'password': '123456',
    'database': 'test_platform'
}
def connection_pool():
    # Return a connection pool instance
    pool = ConnectionPool(**config)
    return pool

with ConnectionPool(**config).cursor() as cursor:
    cursor.execute(' select name from web_platform_course  ')
    print(cursor.fetchall())

#print(connection_pool().cursor().execute(' select name from web_platform_course  ').fetchall())