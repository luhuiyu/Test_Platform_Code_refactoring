#!/usr/bin/env python

# coding=utf-8
from  my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import *
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
import os, time
import logging
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import get_error

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info('正常上课')
@get_error
def test_case(context):
    system = context['platformName']
    platformVersion = context['platformVersion']
    driverName = context['deviceName']
    PORT = context['PORT']
    phone = context['phone']
    url = 'http://127.0.0.1:' + PORT + '/wd/hub'
    driver = appium(platformVersion, driverName, url)
    use_mysql = pad_mysql(phone)
    use_mysql.clear_classes()
    use_mysql.add_class(1)
    operate = user_information(driver, phone, system)
    operate.login_pad()
    driver.find_element_by_id(课程列表_体测).click()
    assert driver.find_element_by_id(体验版体测)
    assert driver.find_element_by_id(专业版体测)
    assert driver.find_element_by_id(私教版体测)
    assert driver.find_element_by_id(未上传体测)
    driver.find_element_by_id(体验版体测).click()
    ##体验版的页面
    # 检查页面是否完整
    #左边
    assert driver.find_element_by_id('com.kk.coachpad:id/user_hight_input').text == '身高(cm)', '身高(cm)'
    assert driver.find_element_by_id('com.kk.coachpad:id/user_age_input').text == '年龄','年龄'
    assert driver.find_element_by_id('com.kk.coachpad:id/male_button').text == '男','男'
    assert driver.find_element_by_id('com.kk.coachpad:id/female_button').text == '女','女'
    assert driver.find_element_by_id('com.kk.coachpad:id/normalbody_button').text == '普通人','普通人'
    assert driver.find_element_by_id('com.kk.coachpad:id/amateurbody_button').text == '业余运动爱好者','业余运动爱好者'
    assert driver.find_element_by_id('com.kk.coachpad:id/probody_button').text == '专业运动员/教练' ,'专业运动员/教练'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_match').text == '首次配对','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_measure').text == '开始称重','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_exit').text == '返回','校验体验版'
    #右边
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_weight_info_number').text == '0.0公斤','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_bmi_info_number').text == '--','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/fat_info_title').text=='脂肪含量','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/fatpercent_info_title').text=='脂肪百分比','校验体验版'
    assert driver.find_element_by_id('com.kk.coachpad:id/water_info_title').text=='含水量','含水量'
    assert driver.find_element_by_id('com.kk.coachpad:id/waterpercent_info_title').text=='含水量百分比','含水量百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/bone_info_title').text=='骨骼含量','骨骼含量'
    assert driver.find_element_by_id('com.kk.coachpad:id/bonepercent_info_title').text=='骨骼含量百分比','骨骼含量百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/muscle_info_title').text=='肌肉含量','肌肉含量'
    assert driver.find_element_by_id('com.kk.coachpad:id/bmr_info_title').text == '基础代谢','基础代谢'
    ##验证功能
    driver.find_element_by_id('com.kk.coachpad:id/bt_match').click()
    time.sleep(1)
    assert  driver.find_element_by_id('com.kk.coachpad:id/tv_title').text=='搜索蓝牙秤','校验体验版'
    time.sleep(15)
    assert driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').text == '我知道了','校验体验版'
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    return   {'driverName':str(driverName),"result":1,}


if __name__ == '__main__':
    context = {}
    case_address = r'F:/Test_Platform' + '/my_python_code/myCase/appium_case/快快教瘦/test_case/遍历pad的所有功能'
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对 6.0
    driverName = 'YVF6R15A29000229'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905521'
    context['platformName'] = system
    context['platformVersion'] = platformVersion
    context['deviceName'] = driverName
    context['PORT'] = PORT
    context['phone'] = '15600905550'
    print(test_case(context))



