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
logger.info('正常上课')
@get_error
def wait_unit(driver,index):
    for i in range(index):
        print(i)
        time.sleep(1)
        driver.find_element_by_id(连接臂带)

      #  logger.info('上课_等待1秒' )

def test_case(context):
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    my_db = orm_to_mysql(my_sql_link())
    course_list=my_db.table('web_platform_course').select(name__LIKE='防暴课').all()
    rult_list=[]
    sigu=False
    for  course  in  course_list:
        for  x  in range(1,int(course['subject_total'])):
         # try:
            driver = appium(platformVersion, driverName, url)
            use_mysql = pad_mysql(phone)
            operate = user_information(driver, phone, system,driverName)
            print('课程' + str(x), driverName)
            use_mysql.clear_classes()
            use_mysql.add_class(add_time=1,store_name=None, user_number='12',classes_checkin_number='12',course_code=course['course_code']+str(x),subject_show_id=str(course['subject_show_id']),dict_index=str(int(PORT)-4910))
            operate.login_pad()
            driver.find_elements_by_id(课程标题)[0].click()
            driver.find_element_by_id(弹窗_确认).click()
            operate.configure_instructor()
            operate.check_element('id','unit_duration')
            b = driver.find_elements_by_id('unit_duration')
            i=0

            while  i<5000:
                b[1].click()
                driver.find_element_by_id(弹窗_确认).click()
                b[0].click()
                i=i+1
            operate.end_courses()
            c=driver.find_elements_by_id('com.kk.coachpad:id/tv_look_report')
            assert len(c)==9,'生成报告成功'
            rult_list.append({'course_code':course['course_code']+str(x),"result": 1, })
         # except Exception as e:
         #     sigu=True
         #     rult_list.append({'course_code': course['course_code'] + str(x), "result": -1, "error_info": '\'' + str(e) + '\'' })
    if sigu:
        return {"result": -1, "error_info": '\'' + str( rult_list ) + '\''}
    else:
        return {'driverName': str(driverName), "result": 1, }



              #


if __name__ == '__main__':
    context = {}
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对 6.0
    driverName = '192.168.8.153:5555'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905551'
    context['platformName'] = system
    context['platformVersion'] = platformVersion
    context['deviceName'] = driverName
    context['PORT'] = PORT
    context['phone'] = phone
    print(test_case(context))