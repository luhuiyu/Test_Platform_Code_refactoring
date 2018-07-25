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
    A = driver.find_elements_by_id('com.kk.coachpad:id/edit_text')
    driver.find_element_by_id(称重_性别男).click()
    driver.find_element_by_id('com.kk.coachpad:id/tv_weight_delta').click()
    print(          driver.find_element_by_id('android:id/numberpicker_input').location())
    print(driver.find_element_by_id('android:id/numberpicker_input').get_attribute(),

          )
    driver.find_element_by_id(弹窗_确认).click()
    A[1].clear()
    A[1].set_value('27') #年龄
    A[2].clear()
    A[2].set_value('188') #身高
    A[3].clear()
    A[3].set_value('70') #心率
    A[4].clear()
    A[4].set_value('100')#腰围
    A[5].clear()
    A[5].set_value('90')#腹围
    A[6].clear()
    A[6].set_value('120')#臀围
    A[7].clear()
    A[7].set_value('90')#左大腿
    A[8].clear()
    A[8].set_value('50')#左小腿
    A[9].clear()
    A[9].set_value('90')#右大腿
    A[10].clear()
    A[10].set_value('60')#右小腿

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


