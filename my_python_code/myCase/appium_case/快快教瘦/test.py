#coding=utf-8
from appium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium_coachPad.interface.mod_class import appium
from appium_coachPad.interface.mod_class import user_information
from appium_coachPad.interface.mod_class import pad_mysql
import os,time
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.info('正常上课')

class ToastTests(unittest.TestCase):

    def test_case(self):
        system = 'Andriod'  # 手机系统
        platformVersion = '5.1.1'  # 版本号 一定要填对
        driverName = 'YVF4C15821002877'  # 手机的
        url = 'http://127.0.0.1:4723/wd/hub'
        phone = '15600905521'
        driver = appium(platformVersion, driverName, url)
        use_mysql = pad_mysql(phone)
        use_mysql.clear_classes()
        use_mysql.add_class(1)
        operate = user_information(driver, phone, system)
        operate.login_pad()
        driver.find_element_by_id('com.kk.coachpad:id/course_title').click()  # 选择第一节课
        while not driver.find_elements_by_id('com.kk.coachpad:id/btn_confirm'):
            try:
                driver.find_element_by_id('com.kk.coachpad:id/course_title').click()
            except:
                pass
        driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
        while not driver.find_elements_by_id('tv_bind'):
            logger.info('tv_bind' + driverName)
            time.sleep(1)
        a = driver.find_elements_by_id('tv_bind')
        i = 0
        for x in a:
            try:
                x.click()
                if i < 6:
                    a[i].click()
                else:
                    pass
                driver.back()
                driver.find_element_by_id('iv_play').click()
                logger.info('iv_play' + str(x))
                time.sleep(1)
                driver.find_element_by_id('tv_clear').click()
                logger.info('tv_clear')
                time.sleep(1)
                driver.find_element_by_id('ll_next_action').click()
                logger.info('ll_next_action')
                driver.back()
                i = i + 1
            except:
                pass
        time.sleep(3)
        print(driver.find_elements_by_id('unit_duration'))
        while not driver.find_elements_by_id('unit_duration'):
            driver.back()
            time.sleep(1)
        b = driver.find_elements_by_id('unit_duration')
        print('b=', b)
        i = 55
        while i < 50:
            print(driverName, i)
            for y in [1, 2, 3, 4, 5]:
                operate.ac_click(266, 813, driverName)
                while not driver.find_elements_by_id('com.kk.coachpad:id/btn_confirm'):
                    try:
                        b[y].click()
                        logger.info('unit_duration' + str(y))
                    except:
                        operate.ac_click(266, 813, driverName)
                        time.sleep(5)
                        pass
                driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
            for y in [4, 3, 2, 1, 0]:
                operate.ac_click(266, 813, driverName)
                while not driver.find_elements_by_id('com.kk.coachpad:id/btn_confirm'):
                    try:
                        b[y].click()
                        logger.info('unit_duration' + str(y))
                    except:
                        operate.ac_click(266, 813, driverName)
                        pass
                driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
            i = i + 1
        for y in [1, 2, 3, 4, 5]:
            b[y].click()
            time.sleep(1)
            logger.info('unit_duration' + str(y))
            driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
        key = driver.find_elements_by_id('com.kk.coachpad:id/unit_image')
        #  print(key)
        key[6].click()
        driver.find_element_by_id('com.kk.coachpad:id/tv_finish').click()
        activity = driver.current_activity
        print(activity)
        while not driver.find_elements_by_id('com.kk.coachpad:id/title_name'):
            time.sleep(1)
        if len(driver.find_elements_by_id('com.kk.coachpad:id/tv_look_report')) == 9:
            return 1
        else:
            return 0


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(suite)