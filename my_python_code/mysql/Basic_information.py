import threading
import pymysql,os,time
Lock = threading.Lock()
from my_python_code.mysql.Singleton  import  Singleton


class my_sql_link(Singleton):
     def __init__(self):
         self.db=pymysql.connect("192.168.41.27", "root", "123456", "test_platform", 33061, charset='utf8')  # 连接数据库
#         self.db = pymysql.connect("127.0.0.1", "root", "admin", "test_platform", 3306, charset='utf8')  # 连接数据库
         self.cursor=self.db.cursor()
         self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        # print('test_platform',id(self))

     def close(self):
         self.db.close()


class my_sql_link_test(Singleton):
    def __init__(self):
        # self.db = pymysql.connect("47.93.124.146", "kas", "kuaikuaikas", "kk_test", 33061, charset='utf8')  # 连接数据库
      #  try:
           # self.db = pymysql.connect("127.0.0.1", "root", "admin", "test_platform", 3306, charset='utf8')  # 连接数据库
            self.db = pymysql.connect("192.168.41.20", "kms", "kuaikuaikms", "kk_test", 33061, charset='utf8')  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
       #     print('test',id(self))
      #  except:
        #     print('连接数据库失败')
       #      return

class my_sql_link_buz(Singleton):
    def __init__(self):
        try:
            self.db = pymysql.connect("101.201.142.45", "look", "LookForDev", "kk_buz", 33061, charset="utf8")  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print('buz',id(self))
        except:
             print('连接数据库失败')
             return



class my_sql_link_stage(Singleton):


    def __init__(self):
        try:
            self.db = pymysql.connect("47.93.124.146", "kas", "kuaikuaikas", "kk_test", 33061, charset='utf8')  # 连接数据库
            self.cursor = self.db.cursor()
            self.cursor_dict = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print('stage',id(self))
        except:
             print('连接数据库失败')
             return





if __name__ == '__main__':
    a=my_sql_link()
    b=my_sql_link()
    c=my_sql_link()