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
logger.info('下课提醒')
@get_error
def wait_unit(driver,index):
    for i in range(index):
        time.sleep(1)
        driver.find_elements_by_id(单元小节图片)
      #  logger.info('上课_等待1秒' )

def test_case(context):
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    my_db = orm_to_mysql(my_sql_link())
    driver = appium(platformVersion, driverName, url)
    operate = user_information(driver, phone, system)
    use_mysql = pad_mysql(phone)
    use_mysql.clear_classes()
    course=my_db.table('web_platform_course').select(name__LIKE='燃脂循环').one()
    use_mysql.add_class(add_time=1,end_time=800, store_name=None, user_number='12', classes_checkin_number='10',
                        course_code=course['course_code'] + str(1), subject_show_id=str(course['subject_show_id']),
                        dict_index='3')
    operate.login_pad()
    driver.find_elements_by_id(课程标题)[0].click()
    driver.find_element_by_id(弹窗_确认).click()
    i=0
    operate.check_element('id',课程结束提醒,600)
    print(driver.find_element_by_id(课程结束提醒))
    assert driver.find_element_by_id(课程结束提醒).text=='距离下课时间还剩10分钟!'
    operate.ac_click(1730,800,driverName)
    time.sleep(1)
    operate.check_element('id',课程结束提醒,600)
    assert driver.find_element_by_id(课程结束提醒).text=='距离下课时间还剩5分钟!'
    operate.ac_click(1730,800,driverName)
    time.sleep(1)
    operate.check_element('id', 课程结束提醒, 600)
    assert driver.find_element_by_id(课程结束提醒).text=='距离下课时间还剩10秒钟!'
   # driver.close()



              #


if __name__ == '__main__':
    context = {}
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对 6.0
    driverName = '192.168.8.116:5555'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905521'
    context['platformName'] = system
    context['platformVersion'] = platformVersion
    context['deviceName'] = driverName
    context['PORT'] = PORT
    context['phone'] = phone
    print(test_case(context))