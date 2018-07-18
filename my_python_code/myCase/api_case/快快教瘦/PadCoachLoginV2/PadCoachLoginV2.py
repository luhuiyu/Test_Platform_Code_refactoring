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
            self.logger.info("测试正确的手机号，正确的密码")
            user_phone = '15600905550'
            password = '123456'
            result=self.Case_login(client, user_phone, password)
            if result == 200:
                return [1]
            else:
                return [0,result]
        except Exception as e:
            return [-1, e]

        return list_login




if __name__=='__main__':
    #print(testCase_login())
    example=API_case()
    print(example.test_case())


'''

self.logger.info("测试错误的手机号")
        user_phone = '156009055'
        password = '123456'
        if self.Case_login(client, user_phone, password) == 403:
            list_login.append(1)
        else:
            list_login.append(0)
        self.logger.info("不填手机号")
        user_phone = ''
        password = '123456'
        if self.Case_login(client, user_phone, password) == 403:
            list_login.append(1)
        else:
            list_login.append(0)
        user_phone = '15600905550'
        password = ''
        if self.Case_login(client, user_phone, password) == 403:
            list_login.append(1)
        else:
            list_login.append(0)
        self.logger.info("正确的手机号和正确的密码")
        user_phone = '15000000000000000000000600905550'
        password = '123456'
        if self.Case_login(client, user_phone, password) == 403:
            list_login.append(1)
        else:
            list_login.append(0)
        user_phone = '1'
        password = '123456'
        if self.Case_login(client, user_phone, password) == 403:
            list_login.append(1)
        else:
            list_login.append(0)
        if self.Case_login(client) == 200:
            list_login.append(1)
        else:
            list_login.append(0)
'''