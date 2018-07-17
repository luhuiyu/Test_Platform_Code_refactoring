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
    def __init__(self):
        self.API_name =  私教课体测or专业课体测
        self.orm = orm_to_mysql(my_sql_link())
        Basics_case.__init__(self)  # 子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用
    @get_error
    def test_case(self):  # 对比和 web_platform_pad_pesourcelist 保存的数据是否一致
          heard = self.login()
          error_list = []
          sgin = True
          all_case_json = self.orm.table('web_platform_comparison_library').select(api_name=self.API_name).all()
          if len(all_case_json)==0:return {"result": -1, "error_info": 'not case'}
          for x in all_case_json:
              start_time=time.time()
              rult = {'id': x['id']}
              case_rult = self.client.post(url=self.API_url(), json=eval(x['send_json']), headers=heard)
              try:
                  if not case_rult.status_code == int(x['status_code']):
                      rult["error_info"] =  str('status_code  : ')+str(case_rult.status_code)
                      rult['result'] = '0'
                      sgin = False
                  if eval(x['receive_json'])== {}:
                      pass
                  else:
                      if not case_rult.json()['userCode']== eval(x['receive_json'])['userCode']:
                          logging.info(str(case_rult.json()))
                          rult["error_info"] = "JSON contrast failure"
                          rult['result'] = '0'
                          sgin = False
              except  :
                  rult["error_info"] = "JSON  is not in  "
                  rult['result'] = '0'
                  sgin = False
              if 'result'  in rult.keys(): error_list.append(rult)
              end_time=time.time()
              self.logger.info(end_time-start_time)
          self.orm.close()
          if sgin: return {"result": 1}
          else:return {"result": 0, "error_info": error_list}

if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
