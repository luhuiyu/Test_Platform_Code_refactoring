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
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name =  获取课程列表
        self.standard_json=eval(self.orm.table('web_platform_my_json_format').select(api_name=self.API_name).one()['json_format'])

   # @get_error
if __name__ == '__main__':
    example = API_case()
    logger.info(example.test_case())
