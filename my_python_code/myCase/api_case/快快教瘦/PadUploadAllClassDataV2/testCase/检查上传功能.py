#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.api_case.interface.login_args import login
from imp import reload
import logging,json
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case,get_error
import my_python_code.myCase.api_case.interface.Basic_information
import  my_python_code.myCase.api_case.interface.接口记录
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link

class API_case(Basics_case):
  def __init__(self):
    self.API_name =my_python_code.myCase.api_case.interface.接口记录.上传学员运动数据
    Basics_case.__init__(self)  #子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用
  @get_error
  def test_case(self):
      login_heard=login( self.client)
      a=orm_to_mysql(my_sql_link_test())
      old_class_data=self.client.get("http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/f7af6d77-1750-49b5-99b6-a0f5246061ba.txt")
      class_id=old_class_data.json()['classDataList'][0]['classesId']
      old_user_class_data_id=a.table('user_class_data').select('MAX(id)',class_id=class_id).one()['MAX(id)']
      old_report_uuid=a.table('user_report').select(classes_id=class_id).one()['uuid']
      assert  old_class_data.status_code == 200 ,"获取class_data出错"
      up_new_report=self.client.post(url=self.API_url(),data=old_class_data,headers=login_heard)
      assert  up_new_report.status_code == 200 ,"上传报告出错"
      new_user_class_data_id=a.table('user_class_data').select('MAX(id)',class_id=class_id).one()['MAX(id)']
      new_report_uuid=a.table('user_report').select(classes_id=class_id).one()['uuid']
      assert int(old_user_class_data_id) < int(new_user_class_data_id),'上传报告出错'
      assert old_report_uuid != new_report_uuid ,'报告保存到数据库出错'
      return {"result":1}
if __name__=='__main__':
    example=API_case()
    print(example.test_case())
