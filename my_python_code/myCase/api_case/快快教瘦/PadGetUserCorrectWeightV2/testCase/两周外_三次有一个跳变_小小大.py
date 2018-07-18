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
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name = my_python_code.myCase.api_case.interface.接口记录.登录




    def test_case(self):

        reload(my_python_code.myCase.api_case.interface.login_args)

        try:

                db=self.db

                cursor=self.cursor

                old_fatRate_list = [22, 22]
                corr_time_list = [1582400, 1382400]
                fatRate = 18  # 称重得到的体脂率
                corr_Fatrate = 18  # 被修改后的体脂率

                case_Result=weight_testCase(self.client,db, cursor, user_uuid,old_fatRate_list,fatRate,corr_Fatrate,corr_time_list,self.my_db_lock)

                return case_Result

        except Exception as e:

                 return {"result":-1,"error_info": '\''+str(e)+'\''}













if __name__=='__main__':

    #print(testCase_login())

    example=API_case()

    print(example.test_case())































