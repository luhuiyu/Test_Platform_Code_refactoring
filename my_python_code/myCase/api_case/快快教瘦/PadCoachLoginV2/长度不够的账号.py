#!/usr/bin/env python
#coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case
class API_case(Basics_case):
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self,my_db_lock = kwargs['my_db_lock'])
        self.API_name = my_python_code.myCase.api_case.interface.接口记录.登录

    def Case_login(self,client,user_phone='15600905550',password='123456'):
        headers=my_python_code.myCase.api_case.interface.login_args.headers(client,user_phone,password)
        self.logger.info(headers)
        login_pad=client.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2',headers=headers)
        self.logger.info(login_pad.status_code)
        reload(my_python_code.myCase.api_case.interface.login_args)
        return login_pad.status_code

    def test_case(self):
        try:
            reload(my_python_code.myCase.api_case.interface.login_args)
            client = self.client
            user_phone = '1560090555'
            password = '123456'
            result=self.Case_login(client, user_phone, password)
            if result == 410:
                return {"result": 1}
            else:
                return {"result": 0, "error_info": '返回的信息：' + str(result) + '期望结果 ：' + '410'}
        except Exception as e:
            return {"result": -1, "error_info": '\'' + str(e) + '\''}




if __name__=='__main__':
    #print(testCase_login())
    example=API_case()
    print(example.test_case())
