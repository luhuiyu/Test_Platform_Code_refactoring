#!/usr/bin/env python

#coding=utf-8

from  my_python_code.myCase.api_case.快快教瘦.PadGetUserCorrectWeightV2.weight_interface.function import weight_testCase

from my_python_code.basic_configuration.configuration_file import *

import my_python_code.myCase.api_case.interface.login_args

from imp import reload

import logging
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case
class API_case(Basics_case):
    def __init__(self):
        self.API_name = my_python_code.myCase.api_case.interface.接口记录.登录
        Basics_case.__init__(self)  #子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用

    '''
    3. 学员在第4次及以后测量时，依赖最后2次数据，按照以下限制：
    3.1 如果本次测试距离最新一次测量小于一周：体脂率上下变动需要小于2%；
    3.2 如果本次测试距离最新一次测量大于一周，小于一个月：体脂率上下变动需要小于3.5%；
    3.3 如果本次测试距离最新一次测量大于一个月：体脂率上下变动不做限制；
    '''
    def test_case(self):
        reload(my_python_code.myCase.api_case.interface.login_args)
        try:
                db=self.db
                cursor=self.cursor
                old_fatRate_list = [20, 20, 20]
                corr_time_list = [3600000, 3500000, 3024006]
                fatRate = 30  # 称重得到的体脂率
                corr_Fatrate = 30  # 被修改后的体脂率
                case_Result=weight_testCase(self.client,db, cursor, user_uuid,old_fatRate_list,fatRate,corr_Fatrate,corr_time_list)
                return case_Result
        except Exception as e:

                 return {"result":-1,"error_info": '\''+str(e)+'\''}













if __name__=='__main__':

    #print(testCase_login())

    example=API_case()

    print(example.test_case())































