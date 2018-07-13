#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging,time
import json,pymysql
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case, get_error
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
true=True
false=False
class API_case(Basics_case):
    def __init__(self):
        self.API_name =  获取学员信息
        self.orm = orm_to_mysql(my_sql_link())
        Basics_case.__init__(self)  # 子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用
if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
