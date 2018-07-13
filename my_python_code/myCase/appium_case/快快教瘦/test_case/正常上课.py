#!/usr/bin/env python
#coding=utf-8
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import appium
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import user_information
from my_python_code.myCase.appium_case.快快教瘦.interface.mod_class import pad_mysql
import os,time
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info('正常上课')
def test_case(system,platformVersion,driverName,url,phone):
    try:
        url='http://127.0.0.1:'+url+'/wd/hub'
        driver = appium(platformVersion, driverName,url)
        use_mysql = pad_mysql(phone)
        #use_mysql.clear_classes()
       # use_mysql.add_class(1)
        operate=user_information(driver,phone,system)
        operate.login_pad()
        time.sleep(20)
        return {'driverName':str(driverName),"result":1,"img":"XXXXXX"}
    except Exception as e:
        return  {'driverName':str(driverName),"result":-1,"error_info": '\''+str(e)+'\''}

if __name__ == '__main__':
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对
    driverName = 'YVF6R15A29000229'  # 手机的
    url = 'http://127.0.0.1:4910/wd/hub'
    phone = '15600905521'
    test_case(system,platformVersion,driverName,url,phone)