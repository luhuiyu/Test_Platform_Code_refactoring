#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging,time
import json,pymysql
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case, get_error
import my_python_code.myCase.api_case.interface.Basic_information
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
logging.basicConfig(level=logging.INFO)
class API_case(Basics_case):
    def __init__(self):
        self.API_name =  获取资源列表
        Basics_case.__init__(self)
if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
