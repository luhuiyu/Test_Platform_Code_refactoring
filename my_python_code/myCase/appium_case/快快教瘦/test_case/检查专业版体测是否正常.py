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
#@get_error
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
    driver.find_element_by_id(专业版体测).click()
    ##专业版的页面
    # 检查页面是否完整
    # 第一页
    assert driver.find_element_by_id('com.kk.coachpad:id/title_name').text == '快快身体测评 1/4','快快身体测评 1/4'
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_hand_code').text == '手动输入','手动输入'
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_scan_code').text == '点击扫描二维码','点击扫描二维码'
    driver.find_element_by_id('com.kk.coachpad:id/tv_scan_code').click()
    time.sleep(1)
    assert driver.find_element_by_id('com.kk.coachpad:id/viewfinder_view')
    driver.back()
    driver.find_element_by_id('com.kk.coachpad:id/tv_hand_code').click()
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_title').text=='请输入用户ID','请输入用户ID'
    driver.find_element_by_id('com.kk.coachpad:id/et_hurt_position').send_keys('1')
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    #assert operate.find_toast('查不到该用户！')
    driver.find_element_by_id('com.kk.coachpad:id/tv_hand_code').click()
    driver.find_element_by_id('com.kk.coachpad:id/et_hurt_position').send_keys('100230')
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    ##第二页
    a=driver.find_elements_by_id('com.kk.coachpad:id/tv_name')
    name_list=[]
    old_name_list=['姓名:', '身高:', '年龄:', '胸围:', '腰围:', '臀围:', '大臂围(左):', '大臂围(右):', '大腿围(左):', '大腿围(右):', '深蹲个数:', '躬身个数:']
    for x in a:
        name_list.append(x.text)
    assert  name_list ==old_name_list
    #体成分分析
    assert driver.find_element_by_id('com.kk.coachpad:id/weight_info_title').text=='体重','体重'
    assert driver.find_element_by_id('com.kk.coachpad:id/fat_info_title').text=='脂肪含量','脂肪含量'
    assert driver.find_element_by_id('com.kk.coachpad:id/fatpercent_info_title').text=='脂肪百分比','脂肪百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/bmr_info_title').text=='基础代谢','基础代谢'
    assert driver.find_element_by_id('com.kk.coachpad:id/water_info_title').text=='含水量','含水量'
    assert driver.find_element_by_id('com.kk.coachpad:id/waterpercent_info_title').text=='含水量百分比','含水量百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/bmi_info_title').text=='BMI','BMI'
    assert driver.find_element_by_id('com.kk.coachpad:id/bone_info_title').text=='骨骼含量','骨骼含量'
    assert driver.find_element_by_id('com.kk.coachpad:id/bonepercent_info_title').text=='骨骼含量百分比','骨骼含量百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/muscle_info_title').text=='肌肉含量','肌肉含量'
    assert driver.find_element_by_id('com.kk.coachpad:id/musclepercent_info_title').text=='肌肉含量百分比','肌肉含量百分比'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_left').text=='首次配对','首次配对'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_middle').text=='开始称重','开始称重'
    assert driver.find_element_by_id('com.kk.coachpad:id/bt_right').text=='下一题','下一题'
    driver.find_element_by_id('com.kk.coachpad:id/bt_left').click()
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_title').text=='搜索蓝牙秤','搜索蓝牙秤'
    time.sleep(15)
    assert driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').text == '我知道了', '我知道了'
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    return   {'driverName':str(driverName),"result":1,}


if __name__ == '__main__':
    context = {}
    case_address = r'F:/Test_Platform' + '/my_python_code/myCase/appium_case/快快教瘦/test_case/遍历pad的所有功能'
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对 6.0
    driverName = '192.168.21.135:5555'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905521'
    context['platformName'] = system
    context['platformVersion'] = platformVersion
    context['deviceName'] = driverName
    context['PORT'] = PORT
    context['phone'] = '15600905550'
    print(test_case(context))



