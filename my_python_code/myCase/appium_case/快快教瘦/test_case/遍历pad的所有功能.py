#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
from my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import *
import os,time,re
import logging
from PIL import Image,ImageDraw
from  my_python_code.picture_contrast.similarity import classfiy_histogram_with_split
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.info('正常上课')
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import get_error

class  appium_case(user_information):
        pass
@get_error
def test_case(context):
   #  print(os.getcwd())
     system=context['platformName']
     platformVersion=context['platformVersion']
     driverName=context['deviceName']
     PORT=context['PORT']
     phone=context['phone']
     case_address = context['case_address']
     case_address=case_address.replace('.','/')
  #   print(case_address)
     try:
        url='http://127.0.0.1:'+str(PORT)+'/wd/hub'
        driver = appium(platformVersion, driverName,url)
        use_mysql = pad_mysql(phone)  #pad_mysql是常用的pad上操作数据库的行为
        use_mysql.clear_classes()
        operate=user_information(driver,phone,system) #operate 是常用的操作
        driver.start_activity(教练pad, 登录页面的Activity)
        operate.check_element('id',登录_账号)
        driverName= re.sub("\W", "", driverName)
     #   print(case_address+r'/img/登录页面'+driverName+'.png')
        driver.get_screenshot_as_file(case_address+r'/img/登录页面'+driverName+'.png')
        logon_img_standard=Image.open(case_address+r'/img/登录页面.png')
        logon_img_new =Image.open(case_address+r'/img/登录页面'+driverName+'.png')
        assert classfiy_histogram_with_split(logon_img_standard,logon_img_new)>99,'登录页面 图片校验不通过'

        driver.find_element_by_id(登录页面_快快身体评测).click()
        operate.check_element('id',体验版体测)
        driver.get_screenshot_as_file(case_address+r'/img/快快身体评测_弹窗' + driverName + '.png')
        pc_img_standard=Image.open(case_address+r'/img/快快身体评测_弹窗.png')
        pc_img_new=Image.open(case_address+r'/img/快快身体评测_弹窗' + driverName + '.png')
        assert classfiy_histogram_with_split(pc_img_standard, pc_img_new) -99>0, '快快身体评测_弹窗 图片校验不通过'
        driver.find_element_by_id(体验版体测).click()
        operate.check_element('id','com.kk.coachpad:id/bt_measure')
        driver.get_screenshot_as_file(case_address+r'/img/体验版评测' + driverName + '.png')
        test_measure_img_standard=Image.open(case_address+r'/img/体验版评测.png')
        test_measure_img_new=Image.open(case_address+r'/img/体验版评测' + driverName + '.png')
        assert classfiy_histogram_with_split(test_measure_img_standard, test_measure_img_new) > 99, '体验版评测 图片校验不通过'
        driver.back()
        driver.find_element_by_id(登录页面_快快身体评测).click()
        driver.find_element_by_id(专业版体测).click()
        operate.check_element('id',专业版体测_手动输入)
        driver.get_screenshot_as_file(case_address+r'/img/专业版体测' + driverName + '.png')
        major_measure_img_new=Image.open(case_address+r'/img/专业版体测' + driverName + '.png')
        major_measure_img_standard=Image.open(case_address+r'/img/专业版评测.png')
        assert  classfiy_histogram_with_split(major_measure_img_new, major_measure_img_standard) > 99, '专业版评测 图片校验不通过'
        driver.find_element_by_id(专业版体测_手动输入).click()
        driver.find_element_by_id(专业版体测_输入用户id).send_keys('100230')
        driver.find_element_by_id(弹窗_确认).click()
        operate.check_element('id','com.kk.coachpad:id/bt_left')
        driver.get_screenshot_as_file(case_address+r'/img/专业版评测_输入用户id' + driverName + '.png')
        time.sleep(3)
        major_measure_img_new = Image.open(case_address+r'/img/专业版评测_输入用户id' + driverName + '.png')
        major_measure_img_standard = Image.open(case_address+r'/img/专业版评测_输入用户id.png')
        assert classfiy_histogram_with_split(major_measure_img_new, major_measure_img_standard) > 99, '专业版评测_输入用户id 图片校验不通过'
        driver.back()
        driver.find_element_by_id(弹窗_确认).click()
        driver.find_element_by_id(登录页面_快快身体评测).click()
        driver.find_element_by_id(私教版体测).click()
        operate.check_element('id',专业版体测_手动输入)
        driver.get_screenshot_as_file(case_address+r'/img/私教版评测' + driverName + '.png')
        time.sleep(3)
        major_measure_img_new = Image.open(case_address+r'/img/私教版评测' + driverName + '.png')
        major_measure_img_standard = Image.open(case_address+r'/img/私教版评测.png')
        assert classfiy_histogram_with_split(major_measure_img_new, major_measure_img_standard) > 99, '私教版评测_输入用户id 图片校验不通过'
        driver.find_element_by_id(专业版体测_手动输入).click()
        driver.find_element_by_id(专业版体测_输入用户id).send_keys('100230')
        driver.find_element_by_id(弹窗_确认).click()
        operate.check_element('id',首次配对)
        driver.get_screenshot_as_file(case_address+r'/img/私教版评测_评测项目' + driverName + '.png')
        time.sleep(3)
        major_measure_img_new = Image.open(case_address+r'/img/私教版评测_评测项目' + driverName + '.png')
        major_measure_img_standard = Image.open(case_address+r'/img/私教版评测_评测项目.png')
        assert classfiy_histogram_with_split(major_measure_img_new, major_measure_img_standard) > 99, '私教版评测_评测项目 图片校验不通过'
        driver.back()
        driver.find_element_by_id(弹窗_确认).click()
        driver.find_element_by_id(登录_账号).clear()
        driver.find_element_by_id(登录_账号).send_keys('15600905550')
        driver.find_element_by_id(登录_密码).send_keys('123456')
        driver.find_element_by_id(登录按钮).click()
        operate.check_element('id',课程标题)
        driver.find_element_by_id(课程列表_门店).click()
        gym_list=[]
        for x in driver.find_elements_by_id(门店列表):
            gym_list.append(x.text)
   #     print(gym_list)
        driver.find_elements_by_id(门店列表)[3].click()
        time.sleep(3)
        if driver.find_element_by_id(课程列表_当前门店).text == gym_list[3]:
       #         print('通过')
                    pass
        driver.find_element_by_id(课程列表_体测).click()
        assert driver.find_element_by_id(未上传体测).is_displayed(),'未上传体测'
        assert driver.find_element_by_id(专业版体测).is_displayed(),'专业版体测'
        assert driver.find_element_by_id(私教版体测).is_displayed(),'私教版体测'
        driver.back()
        driver.find_element_by_id(课程列表_设置).click()
        assert driver.find_element_by_id(设置页面_电话).text == str(phone),'phone'
        driver.find_element_by_id(设置页面_关闭)
        return {'driverName':str(driverName),"result":1,"img":"XXXXXX",}
     except Exception as e:
        return  {'driverName':str(driverName),"result":-1,"error_info": '\''+str(e)+'\''}


if __name__ == '__main__':
    context={}
    case_address=r'F:/Test_Platform'+ '/my_python_code/myCase/appium_case/快快教瘦/test_case/遍历pad的所有功能'
    system = 'Andriod'  # 手机系统
    platformVersion = '6.0'  # 版本号 一定要填对 6.0
    driverName = '192.168.8.102:5555'  # 手机的  TJF6R17116002939 YVF6R15A29000229 73e97641 MWUBB17907202712 YVF6R15A29000229
    PORT = '4910'
    phone = '15600905550'
    context['platformName']= system
    context['platformVersion']= platformVersion
    context['deviceName']=driverName
    context['PORT']=PORT
    context['phone']='15600905550'
    context['case_address'] = case_address
    print(test_case(context ))
