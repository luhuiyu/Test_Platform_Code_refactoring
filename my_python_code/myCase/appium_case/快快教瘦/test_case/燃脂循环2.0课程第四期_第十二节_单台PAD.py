#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.api_case.interface.Basics_class import get_error
from  my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import *
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link
from my_python_code.tools.虚拟臂带 import fictitious_bind
from multiprocessing import Process,Lock
from multiprocessing import Queue
import sys
import os,time
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info(str(os.path.basename(sys.argv[0]).split(".")[0] ))
rult_list=[]
def  appium_data(context,Q,course,x):
    global rult_list
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    use_mysql = pad_mysql(phone)
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    driver = appium(platformVersion, driverName, url)
    operate = user_information(driver, phone, system, driverName)
    use_mysql.clear_classes()
    use_mysql.add_class(add_time=1000, store_name=None, user_number='12', classes_checkin_number='12',
                        course_code=course['course_code'] + str(x), subject_show_id=str(course['subject_show_id']),
                        dict_index=str(int(int(PORT) - 4910)))
    operate.login_pad()
    Q.put(1)
    time.sleep(5)
    driver.find_elements_by_id(课程标题)[0].click()
    driver.find_element_by_id(弹窗_确认).click()
    for x in driver.find_elements_by_id(称重按钮)[0:6]:
        x.click()
        operate.inspect_weight()
    operate.binding_arm(driverName)
    Q.put(1)
    while driver.find_elements_by_id(同步电视):
        operate.wipe_down()
    operate.just_in_time_switch_unit()
    operate.end_courses()
    c = driver.find_elements_by_id('com.kk.coachpad:id/tv_look_report')
    assert len(c) == 9, '生成报告成功'
    rult_list.append({'course_code': course['course_code'] + str(x), "result": 1, })
    logger.info(str({'course_code': course['course_code'] + str(x), "result": 1, }))
    return


def test_case(context):
    L=Lock()
    phone = context['phone']
    my_db = orm_to_mysql(my_sql_link())
    course=my_db.table('web_platform_course').select(name__LIKE='燃脂循环2.0课程第四期').one()
    global rult_list
    sigu=False
    Q = Queue()
    Q_pid = Queue()
    L.acquire()
    p1 = Process(target=appium_data, args=(context,Q,course,12)) #第四个参数是上课的节数
    p2 = Process(target=fictitious_bind, args=(False,32,1,Q_pid,))
    p1.start()
    Q.get()
    p2.start()
    p1.join()
    pid_list=Q_pid.get()
    for y in pid_list:
        os.popen('taskkill.exe /pid:' + str(y) + '   -t -f ')
    time.sleep(5)
    Q.get()
    L.release()
    if sigu:
        logger.info(str({"result": -1, "error_info": '\'' + str( rult_list ) + '\''}))
        return {"result": -1, "error_info": '\'' + str( rult_list ) + '\''}
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