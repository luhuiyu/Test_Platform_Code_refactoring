#!/usr/bin/env python
#coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging
logging.basicConfig(level=logging.INFO)
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case,get_error
import my_python_code.myCase.api_case.interface.Basic_information
from  my_python_code.myCase.api_case.interface.接口记录 import *
class API_case(Basics_case):
  def __init__(self):
    self.API_name = 上传学员运动数据
    Basics_case.__init__(self)  #子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用

  @get_error
  def test_case(self):

    return {"result": 0, "error_info": '返回的信息：' + str(result) + '期望结果 ：' + '404'}



if __name__=='__main__':
    example=API_case()
    print(example.test_case())