#!/usr/bin/env python
#coding=utf-8
from  my_python_code.myCase.api_case.快快教瘦.PadGetUserCorrectWeightV2.weight_interface.function import weight_testCase,weight_case_class
from my_python_code.basic_configuration.configuration_file import *
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case

logging.basicConfig(level=logging.INFO)
class API_case(weight_case_class):
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name = my_python_code.myCase.api_case.interface.接口记录.登录
    def test_case(self):
        reload(my_python_code.myCase.api_case.interface.login_args)
        try:
                db=self.db
                cursor=self.cursor
                old_fatRate_list = [25, 25, 25]  # 创造在数据库里面已经有的体脂率的数据，int类型或是str
                corr_time_list = [3456000, 3330000, 30000000]  # 数据创建的时间 int类型
                fatRate = 20  # 称重得到的体脂率  int类型
                corr_Fatrate = 20  # 被修改后的体脂率   int类型

                case_Result=self.weight_testCase(self.client,db,cursor,user_uuid,old_fatRate_list,fatRate,corr_Fatrate,corr_time_list,self.my_db_lock)
                return case_Result
        except Exception as e:
                 return {"result":-1,"error_info": '\''+str(e)+'\''}













if __name__=='__main__':

    #print(testCase_login())

    example=API_case()

    print(example.test_case())































