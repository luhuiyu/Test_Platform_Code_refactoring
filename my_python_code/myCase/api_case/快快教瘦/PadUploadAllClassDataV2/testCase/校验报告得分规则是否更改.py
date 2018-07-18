#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging,time
import json,pymysql
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case, get_error,my_lock
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
from  my_python_code.tools.make_report import make_report
from my_python_code.myCase.api_case.interface.login_args import login
from multiprocessing import Process,Queue,Pool,Lock

true=True
false=False
class API_case(Basics_case):
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name =  上传学员运动数据
    @get_error
    @my_lock
    def test_case(self):  #case  上传同一份classdata,对比除了repor uuid之外的数据检查得分在否和数据库的数据相匹配
        login_heard = login(self.client)
        a = orm_to_mysql(my_sql_link_test())
        all_case_json = self.orm.table('web_platform_comparison_library').select(api_name=self.API_name).all()
        rult_list=[]
        for x in all_case_json:
            old_class_data = self.client.get(x['send_json'])
            get_report_list = self.client.post(url=self.API_url(), data=old_class_data,headers=login_heard)
            class_id=old_class_data.json()['classDataList'][0]['classesId']
            old_report_list=eval(x['receive_json'])
            case_rult = self.client.post(url=self.url + 获取当前课程的报告列表, json={"classesId": class_id,"subjectId": 1441109786806272}, headers=login_heard)
            new_report_list=case_rult.json()

            self.logger.info(new_report_list)
            old_report_list['classReportList'][0]['reportUrl']=1
            new_report_list['classReportList'][0]['reportUrl']=1
            if  old_report_list==new_report_list:
                rult_list.append({'case_name':str(x['remarks']),'result':1})
            else:
                rult_list.append({'case_name': str(x['remarks']), 'result': 0,})
        self.logger.info(rult_list)
        return {"result": 1}
if __name__ == '__main__':
    example = API_case(Lock())
    print(example.test_case())
