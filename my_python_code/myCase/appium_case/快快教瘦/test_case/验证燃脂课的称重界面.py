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
    use_mysql.add_class(add_time=3600, store_name=None, user_number='12', classes_checkin_number='12',
                    course_code='JZX2.0.4.1', subject_show_id=str(1),
                    dict_index=str(int(PORT) - 4910))
    operate.login_pad()
    driver.find_elements_by_id(课程标题)[0].click()
    driver.find_element_by_id(弹窗_确认).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    # 正常的流程
    operate.inspect_weight()
    assert  driver.find_elements_by_id(称重按钮)[0].text == '65.0KG'
    #验证用户没有数据的时候的显示
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_年龄).clear()
    driver.find_element_by_id(称重_安静心率).clear()
    driver.find_element_by_id(称重_姓名).clear()
    driver.find_element_by_id(称重_身高).clear()
    assert  driver.find_element_by_id(称重_年龄).text == '必填*'
    assert  driver.find_element_by_id(称重_安静心率).text == '必填*'
    assert  driver.find_element_by_id(称重_姓名).text == '必填*'
    assert  driver.find_element_by_id(称重_身高).text == '必填*'
    #先填入基础数据；正确的数据
    driver.find_element_by_id(称重_年龄).set_value('25')
    driver.find_element_by_id(称重_安静心率).set_value('65')
    driver.find_element_by_id(称重_姓名).set_value('appium_test')
    driver.find_element_by_id(称重_身高).set_value('165')
    #验证 年龄的范围 6-60
    driver.find_element_by_id(称重_年龄).clear()
    driver.find_element_by_id(称重_年龄).set_value('5')
    driver.find_element_by_id(称重_保存).click()
#    assert operate.find_toast('年龄异常,建议年龄范围是6-60!!!')
    driver.find_element_by_id(称重_年龄).clear()
    driver.find_element_by_id(称重_年龄).set_value('61')
    driver.find_element_by_id(称重_保存).click()
 #   assert operate.find_toast('年龄异常,建议年龄范围是6-60!!!')
    driver.find_element_by_id(称重_年龄).clear()
    driver.find_element_by_id(称重_年龄).set_value('59')
    driver.find_element_by_id(称重_保存).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_年龄).clear()
    driver.find_element_by_id(称重_年龄).set_value('6')
    driver.find_element_by_id(称重_保存).click()
    #安静心跳
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_安静心率).clear()
    driver.find_element_by_id(称重_安静心率).set_value(49)
    driver.find_element_by_id(称重_保存).click()
  #  assert operate.find_toast('安静心跳异常,建议安静心跳的范围是50-80')
    driver.find_element_by_id(称重_安静心率).clear()
    driver.find_element_by_id(称重_安静心率).set_value(81)
    driver.find_element_by_id(称重_保存).click()
 #   assert operate.find_toast('安静心跳异常,建议安静心跳的范围是50-80')
    driver.find_element_by_id(称重_安静心率).clear()
    driver.find_element_by_id(称重_安静心率).set_value(80)
    driver.find_element_by_id(称重_保存).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_安静心率).clear()
    driver.find_element_by_id(称重_安静心率).set_value(50)
    driver.find_element_by_id(称重_保存).click()
    #身高，
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_身高).clear()
    driver.find_element_by_id(称重_身高).set_value(49)
    driver.find_element_by_id(称重_保存).click()
    driver.find_element_by_id(称重_身高).clear()
    driver.find_element_by_id(称重_身高).set_value(251)
    driver.find_element_by_id(称重_保存).click()
    driver.find_element_by_id(称重_身高).clear()
    driver.find_element_by_id(称重_身高).set_value(50)
    driver.find_element_by_id(称重_保存).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_身高).clear()
    driver.find_element_by_id(称重_身高).set_value(249)
    driver.find_element_by_id(称重_保存).click()
    driver.find_elements_by_id(称重按钮)[0].click()
    driver.find_element_by_id(称重_首次配对).click()
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_title').text == '搜索蓝牙秤'
    time.sleep(5)
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_tip_content').text == '没有找到蓝牙秤，请重试！'
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    driver.find_element_by_id(称重_开始称重).click()
    assert driver.find_element_by_id('com.kk.coachpad:id/tv_tip_content').text == '请先首次配对'
    driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    assert driver.find_element_by_id(称重_体重).text == '--'



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


