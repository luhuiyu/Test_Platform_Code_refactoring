import threading
import pymysql,os,time
from my_python_code.mysql.Singleton  import  Singleton
from pymysqlpool import ConnectionPool


class my_sql_link(Singleton):
    def __init__(self):
        self.db = pymysql.connect("192.168.41.27", "root", "123456", "test_platform", 33061, charset='utf8')  # 连接数据库
        #         self.db = pymysql.connect("127.0.0.1", "root", "admin", "test_platform", 3306, charset='utf8')  # 连接数据库
        self.cursor = self.db.cursor()
        self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        # print('test_platform',id(self))

    def close(self):
        self.db.close()
class my_sql_link_test(Singleton):
    def __init__(self):
        # self.db = pymysql.connect("47.93.124.146", "kas", "kuaikuaikas", "kk_test", 33061, charset='utf8')  # 连接数据库
        try:
            # self.db = pymysql.connect("127.0.0.1", "root", "admin", "test_platform", 3306, charset='utf8')  # 连接数据库
            self.db = pymysql.connect("192.168.41.20", "kms", "kuaikuaikms", "kk_test", 33061, charset='utf8')  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print('test', id(self))
        except:
            print('连接数据库失败')
            return
class my_sql_link_buz(Singleton):
    def __init__(self):
        try:
            self.db = pymysql.connect("101.201.142.45", "look", "LookForDev", "kk_buz", 33061, charset="utf8")  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print('buz', id(self))
        except:
            print('连接数据库失败')
            return
class my_sql_link_stage(Singleton):
    def __init__(self):
        try:
            self.db = pymysql.connect("47.93.124.146", "kas", "kuaikuaikas", "kk_test", 33061, charset='utf8')  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print('stage', id(self))
        except:
            print('连接数据库失败')
            return
def my_sql_link_pool():
    config = {
        'pool_name': 'local',
        'host': '192.168.41.27',
        'port': 33061,
        'user': 'root',
        'password': '123456',
        'database': 'test_platform'}
    pool = ConnectionPool(**config)
    return pool
def my_sql_link_test_pool():
    #self.db = pymysql.connect("192.168.41.20", "kms", "kuaikuaikms", "kk_test", 33061, charset='utf8')  # 连接数据库
    config = {
        'pool_name': 'test',
        'host': '192.168.41.20',
        'port': 33061,
        'user': 'kms',
        'password': 'kuaikuaikms',
        'database': 'kk_test'}
    pool = ConnectionPool(**config)
    return pool
def my_sql_link_buz_pool():
    # self.db = pymysql.connect("101.201.142.45", "look", "LookForDev", "kk_buz", 33061, charset="utf8")  # 连接数据库
    config = {
        'pool_name': 'buz',
        'host': '101.201.142.45',
        'port': 33061,
        'user': 'look',
        'password': 'LookForDev',
        'database': 'kk_buz'}
    pool = ConnectionPool(**config)
    return pool
def my_sql_link_stage_pool():
       # self.db = pymysql.connect("47.93.124.146", "kas", "kuaikuaikas", "kk_test", 33061, charset='utf8')  # 连接数据库
       config = {
           'pool_name': 'stage',
           'host': '47.93.124.146',
           'port': 33061,
           'user': 'kas',
           'password': 'kuaikuaikas',
           'database': 'kk_test'
       }
       pool = ConnectionPool(**config)
       return pool





if __name__ == '__main__':
    a=my_sql_link()
    b=my_sql_link()
    c=my_sql_link()