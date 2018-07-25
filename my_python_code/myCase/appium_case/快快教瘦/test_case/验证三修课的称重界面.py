#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.api_case.interface.Basics_class import get_error
from  my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import *
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link
import os,time
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info('验证燃脂课的称重界面')


def test_case(context):
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    rult_list=[]
    sigu=False
    driver = appium(platformVersion, driverName, url)
    use_mysql = pad_mysql(phone)
    operate = user_information(driver, phone, system, driverName)
    use_mysql.clear_classes()
    use_mysql.add_class(add_time=3600, store_name=None, user_number='6', classes_checkin_number='6',
                    course_code='SXTB.1.0.1.1', subject_show_id=str(13),
                    dict_index=str(int(PORT) - 4910))
    operate.login_pad()
    driver.find_elements_by_id(课程标题)[0].click()
    driver.find_element_by_id(弹窗_确认).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    # 正常的流程



    if sigu:
        logger.info(str({"result": -1, "error_info": '\'' + str(rult_list) + '\''}))
        return {"result": -1, "error_info": '\'' + str(rult_list) + '\''}
    else:
        logger.info(str({'driverName': str(driverName), "result": 1, }))
        return {'driverName': str(driverName), "result": 1, }
if __name__ == '__main__':
    context = {}
    system = 'Andriod'  # 手机系统
    platformVersion = '6.0'  # 版本号 一定要填对 6.0
    driverName = 'YVF6R15A29000229'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905551'
    context['platformName'] = system
    context['platformVersion'] = platformVersion
    context['deviceName'] = driverName
    context['PORT'] = PORT
    context['phone'] = phone

    print(test_case(context))


