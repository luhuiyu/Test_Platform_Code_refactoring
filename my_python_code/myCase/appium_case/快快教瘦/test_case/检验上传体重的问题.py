#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.api_case.interface.Basics_class import get_error
from  my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import *
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.simple_mysql import *
from my_python_code.basic_configuration.configuration_file import *

from my_python_code.mysql.Basic_information import *
import os,time
import logging
import requests
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info('正常上课')


def test_case(context):
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    rult_list=[]
    sigu=False
    course_code = 'JZX2.0.4.1'
    driver = appium(platformVersion, driverName, url)
    use_mysql = pad_mysql(phone)
    operate = user_information(driver, phone, system,driverName)
    operate.login_pad()
    test_db = simple_mysql(my_sql_link_test_pool())
    buz_db = simple_mysql(my_sql_link_buz_pool())
    my_db = orm_to_mysql(my_sql_link_test_pool())
    upweigt={'dataSourceType': 1, 'entrailsFat': 2, 'fatRate': 26.6, 'macAddress': '18:93:D7:00:55:7A', 'musleRate': 69.2, 'skeletonRate': 4.2, 'userBmr': 1432, 'waterRate': 49.4, 'weight': 52.8}
    for i  in range(1000):
        use_mysql.clear_classes()
        class_id=use_mysql.add_class(add_time=300, store_name=None, user_number='12', classes_checkin_number='12',
                            course_code=course_code, subject_show_id='1', dict_index=str(int(PORT) - 4910))
        operate.wipe_down()
        operate.wipe_down()
        driver.find_elements_by_id(课程标题)[0].click()
        driver.find_element_by_id(弹窗_确认).click()
        operate.check_element('id',绑定臂带)
        for x in driver.find_elements_by_id(称重按钮)[0:12]:
            x.click()
            driver.find_element_by_id(称重_性别男).click()
            driver.find_element_by_id(称重_开始称重).click()
            time.sleep(5)
            driver.find_element_by_id(称重_保存).click()
            if driver.find_elements_by_id(称重_年龄):
                if driver.find_element_by_id(称重_年龄).text == '必填*':
                    driver.find_element_by_id(称重_年龄).clear()
                    driver.find_element_by_id(称重_年龄).set_value('25')
                if driver.find_element_by_id(称重_安静心率).text == '必填*':
                    driver.find_element_by_id(称重_安静心率).clear()
                    driver.find_element_by_id(称重_安静心率).set_value('75')
                if driver.find_element_by_id(称重_姓名).text == '必填*':
                    driver.find_element_by_id(称重_姓名).clear()
                    driver.find_element_by_id(称重_姓名).set_value('25')
                if driver.find_element_by_id(称重_身高).text == '必填*':
                    driver.find_element_by_id(称重_身高).clear()
                    driver.find_element_by_id(称重_身高).set_value('175')
                driver.find_element_by_id(称重_开始称重).click()
                time.sleep(5)
                driver.find_element_by_id(称重_保存).click()
        while driver.find_elements_by_id(同步电视):
            operate.wipe_down()
        b = driver.find_elements_by_id('unit_duration')
        logging.info('第一单元')
        b[1].click()
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(8)
        b[2].click()
        logging.info('第二单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(8)
        b[3].click()
        logging.info('第三单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(8)
        b[4].click()
        logging.info('第四单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(8)
        b[5].click()
        logging.info('第五单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(10)
        operate.end_courses()
        c=driver.find_elements_by_id('com.kk.coachpad:id/tv_look_report')
        assert len(c)==9,'生成报告成功'
        data_uuid = my_db.table('user_class_data').select('data_uuid', class_id=class_id).one()
        url = "http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/"+data_uuid['data_uuid']+".txt"
        user_class_data = requests.get(url).content
        user_class_data = eval(user_class_data)
        for user_data in user_class_data['classDataList']:
            try:
                if  user_data['weightData'] ==upweigt:
                    logger.info(str(user_data['userUuid'] )+'验证有weightData')
                    pass
                else:
                    logger.info('出现问题,json不匹配' + str(class_id)+str('          ')+str(user_data['weightData'] ))
                    pass
            except KeyError as e :
                logger.info('出现问题,没有weigh' + str(class_id) + str('          ') + str(e))
        A = buz_db.TABLE('user_daily_weight').SELECT().WHERE(
            user_uuid='a21573c6-d4dd-466b-8fee-af1b2095cf6f'
        ).AND(id__LT=1103345, ).EXECUTE_ALL()
        for y in uuid_idct[str(int(PORT) - 4910)]:
            test_db.TABLE('user_daily_weight').DELETE().WHERE(user_uuid=y).EXECUTE_ALL()
            for z in A:
                z['user_uuid'] = y
                z['id'] = 'None'
                test_db.TABLE('user_daily_weight').INSERT(z).EXECUTE_ALL()
        driver.back()

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