#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging
import json,pymysql
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case, get_error
import my_python_code.myCase.api_case.interface.Basic_information
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link

class API_case(Basics_case):
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name =  获取当前班级的学员信息

   # @get_error
    def test_case(self):
        list_code = [ 246777,246778,246778,246779,246781,246782,246784,246785,246786,246787,246788


        ]
        heard = self.login()
        for  x  in  list_code:
            #basics_json = {"courseCode": x}  # 7 14
            basics_json = {"classesId": x}
            course = self.client.post(url=self.API_url(), json=basics_json, headers=heard)
            print(basics_json)
            print(self.API_url())
            print(course.json())
            if course.json():
                json_data = pymysql.escape_string(json.dumps(course.json(), ensure_ascii=False))
                print(type(json))
                a = orm_to_mysql(my_sql_link())
                a.table("web_platform_comparison_library").insert(
                    send_json=pymysql.escape_string(json.dumps(basics_json, ensure_ascii=False)),
                    receive_json=json_data, api_name=获取当前课程的小节信息)
                # return {"result": 0, "error_info": '返回的信息：' + str(result) + '期望结果 ：' + '404'}


if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
