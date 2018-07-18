#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging,time
import json,pymysql
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case,get_error,my_lock
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
from  my_python_code.tools.make_report import make_report
from my_python_code.myCase.api_case.interface.login_args import login

true=True
false=False
class API_case(Basics_case):
    def __init__(self, *args, **kwargs):
        Basics_case.__init__(self, my_db_lock=kwargs['my_db_lock'])
        self.API_name =  上传学员运动数据
    @my_lock
    def test_case(self):  #case  上传同一份classdata,对比除了repor uuid之外的数据检查得分在否和数据库的数据相匹配
        login_heard = self.login()
        my_json={
          "classDataList": [
            {
              "baseData": {
                "height": 188,
                "pulse": 65,
                "sex": 1,

              },
              "classesId": 250033,
              "courseCode": "JZX2.0.4.1",
              "endTime": 1522640940000,
              "padId": "867106020354632_241fa08b63f6",
              "startTime": 1522637340000,
              "subjectId": 1389166981187584,
              "unitDataList": [
                {
                  "heartbeats": "111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,",
                  "totalKCAL": "0,0,0",
                  "unitCode": "UNIT2.0.4.1.1",
                  "unitName": "基础热身"
                },
                {
                  "heartbeats": "111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,",
                  "totalKCAL": "0",
                  "unitCode": "UNIT2.0.4.1.2",
                  "unitName": "周身循环训练"
                },
                {
                  "heartbeats": "111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,",
                  "totalKCAL": "0,0",
                  "unitCode": "UNIT2.0.4.1.4",
                  "unitName": "小器械"
                },
                {
                  "heartbeats": "111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,",
                  "totalKCAL": "0",
                  "unitCode": "UNIT2.0.4.1.6",
                  "unitName": "基础伸展"
                }
              ],
              "userUuid": "4c73f62e-50df-4504-9a7a-925bcc2c7101",
              "weightData": {
        "dataSourceType": 1,
        "entrailsFat": 7,
        "fatRate": 37.5,
        "musleRate": 58.8,
        "skeletonRate": 3.8,
        "userBmr": 1581,
        "waterRate": 45.5,
        "weight": 70.9
      }
            }
          ],
          "uploadType": 1,
          "uploadVersion": 3
        }
        user_uuid=my_json['classDataList'][0]['userUuid']
        self.orm.table('user_report').delete(user_uuid=user_uuid)
        self.orm.table('user_daily_weight').delete(user_uuid=user_uuid)
        up_data=self.client.post(url=self.API_url(),json=my_json,headers=self.login_headers)
        assert up_data.status_code == 200, 'up_data.status_code'+str(up_data.status_code)
        get_report=self.client.post(url=self.API_url(获取当前课程的报告列表),json={"classesId":250033,"subjectId": 1441109786806272},headers=self.login_headers)
        print(get_report.json())

        return {"result": 1}
if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
