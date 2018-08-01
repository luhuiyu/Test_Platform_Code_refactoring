#!/usr/bin/env python
from appium import webdriver
import time,os,re
import pymysql
from my_python_code.myCase.appium_case.appium_coachPad.interface.add_class  import addclasses
import logging
from my_python_code.mysql.Basic_information import my_sql_link_test
from  my_python_code.myCase.appium_case.appium_coachPad.interface.Bascic_appid_name import  *
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('mod_class')

def appium(platformVersion, driverName,url):
    '''
    PATH = lambda p: os.path.abspath(
        os.path.join
        (os.path.dirname(__file__),
         p))
    '''
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    #desired_caps['app'] ='http://kuaikuai.oss-cn-beijing.aliyuncs.com/apps/kkcoach_active_3.4_183_20180110-0214_kktest.apk'
    #desired_caps['autoLaunch'] = 'true' #是否自启动
    desired_caps['noReset'] = 'true'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = driverName
    desired_caps['udid'] = driverName  #如果连接多台手机就激活这个
    desired_caps['appPackage'] = 'com.kk.coachpad'
    desired_caps['appActivity'] = 'com.kk.coachpad.ui.activity.LoginActivity'
    desired_caps['resetKeyboard'] = 'true'
    desired_caps['unicodeKeyboard'] = 'true'
   # desired_caps['exported'] ='true'
    desired_caps['automationName'] ='appium' #使用的引擎
    desired_caps['resetKeyboard'] = 'true'
    desired_caps['newCommandTimeout']='30' #最大无响应时间
    driver = webdriver.Remote(url, desired_caps)
    driver.implicitly_wait(10)
    return driver
class user_information ():
    def __init__(self,driver,phone,system):
        self.driver=driver
        self.phone=phone
        self.system=system
        self.w = driver.get_window_size()['width']
        self.h = driver.get_window_size()['height']
    def only_number(self,subject_id):
        subject_id=str(subject_id)
        subject_id=re.sub("\D", "",subject_id)   #去除非数字
        return subject_id
    def wipe_up(self):#上滑
        driver=self.driver
        w= self.w
        h= self.h
        x1=0.5*w
        y1=0.1*h
        y2=0.4*h
        driver.swipe(int(x1),int(y2),int(x1),int(y1),500)
        time.sleep(2)
    def wipe_down(self):#下滑
        driver=self.driver
        w= self.w
        h= self.h
        x1=0.5*w
        y1=0.4*h
        y2=0.9*h
        print(int(x1),int(y1),int(x1),int(y2))
        time.sleep(1)
        driver.swipe(int(x1),int(y1),int(x1),int(y2),1000)
        time.sleep(1)
    def wipe_left(self): #左滑
        driver=self.driver
        w= self.w
        h= self.h
        x1=0.2*w
        y1=0.5*h
        x2=0.6*w
        driver.swipe(int(x2),int(y1),int(x1),int(y1),1000)
        time.sleep(2)
    def wipe_right(self): #右滑
        driver=self.driver
        w= self.w
        h= self.h
        x1=0.6*w
        y1=0.5*h
        x2=0.4*w
        driver.swipe(int(x2),int(y1),int(x1),int(y1),1000)
        time.sleep(2)
    def click(self,x,y):#点击屏幕,x,y是相对坐标
        driver=self.driver
        w = self.w
        h = self.h
        time.sleep(3)
        driver.tap([(int(x*w),int(y*h))], 1)
       # driver.swipe(int(x), int(y), int(x), int(y), 10)
    def ac_click(self,x,y,driverName):
        driver = self.driver
        time.sleep(1)
        print(x,y)
#        driver.tap([(x, y)], 1000)
        l='adb  -s  '+ str(driverName)+' shell input tap  '+str(x)+' '+str(y)
        os.popen(l)
        time.sleep(3)
    def check_element(self,id_type,id,time_out=5):
        driver = self.driver
        i=0
        l = 'driver.find_elements_by_'+str(id_type) +'(\'' + id + '\')'
        while  i < time_out:
            i = i + 1
            if eval(l) != None:
                return 1
            if i==time_out:
                raise AssertionError
            time.sleep(1)
    def find_toast(self, message):  # 验证toast
        driver = self.driver
        message = '//*[@text=\'{}\']'.format(message)
        try:
            element = WebDriverWait(driver, 5, 0.1).until(
                expected_conditions.presence_of_element_located((By.XPATH, message)))
            return 1
        except:
            return 0
    def login_pad(self):
        driver=self.driver
        driver.start_activity(教练pad, 登录页面的Activity)
        logger.info( 登录页面的Activity)
        #driver.save_screenshot(r'F:\automatedTests_of_coachPadApp\phone\1.png')
        if driver.find_elements_by_id(安卓6请求权限的弹窗):
            driver.find_element_by_id(安卓6请求权限的弹窗).click()
        driver.activate_ime_engine(APPIUM输入法)
        driver.find_element_by_id(登录_账号).clear()
        driver.find_element_by_id(登录_账号).set_value(self.phone)
        logger.info(self.phone)
        driver.find_element_by_id(登录_密码).set_value('123456')
        driver.find_element_by_id(登录按钮).click()
        logger.info(登录按钮)
        if driver.find_elements_by_id(安卓6请求权限的弹窗):
            driver.find_element_by_id(安卓6请求权限的弹窗).click()
            driver.find_element_by_id(安卓6请求权限的弹窗).click()
        time.sleep(1)
        while not driver.find_elements_by_id('body_ms'):
            logger.info('body_ms')
            if driver.find_elements_by_id('bt_ok'):
                driver.find_element_by_id('bt_cancel').click()
            if driver.find_elements_by_id(登录_密码):
                driver.find_element_by_id(登录_账号).clear()
                driver.find_element_by_id(登录_账号).set_value(self.phone)
                driver.find_element_by_id(登录_密码).clear()
                driver.find_element_by_id(登录_密码).set_value('123456')
                driver.find_element_by_id(登录按钮).click()
            time.sleep(5)
    def binding_arm(self,index_bind):
        driver = self.driver
        user_bind_list = driver.find_elements_by_id(连接臂带)
        if user_bind_list[index_bind]:
            user_bind_list[index_bind].click()
            bind_list_in_popup=driver.find_elements_by_id(绑定臂带)
            for x in bind_list_in_popup:
                if x.is_enabled()==False:
                    x.click()
                    break
                else:
                    pass
    def  un_bind(self):
        driver = self.driver
    def choice_of_courses(self,index_cures):
        driver=self.driver
        courses_list= driver.find_elements_by_id(课程标题)
        courses_list[index_cures].click()
        while not driver.find_elements_by_id(弹窗_确认):
            i=0
            try:
                if i< 10:
                    courses_list[index_cures].click()

                else:
                    break
            except:
                pass
        driver.find_element_by_id(弹窗_确认).click()
    def  Switching_unit(self,Repetitions):
        driver=self.driver
        b = driver.find_elements_by_id('unit_duration')
        i = 0
        while i < Repetitions:
            for y in [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]:
                while not driver.find_elements_by_id(弹窗_确认):
                    try:
                        b[y].click()
                        logger.info('unit_duration' + str(y))
                    except:
                        operate.ac_click(266, 813, driverName)
                        time.sleep(5)
                        pass
                driver.find_element_by_id(弹窗_确认).click()
            i=i+1
    def end_courses(self):
        driver = self.driver
        b = driver.find_elements_by_id('unit_duration')
        for y in range(1,5):
            b[y].click()
            time.sleep(1)
            logger.info('unit_duration' + str(y))
            driver.find_element_by_id(弹窗_确认).click()
        key = driver.find_elements_by_id(单元小节图片)
        key[6].click()
        while not driver.find_elements_by_id(报告页标题):
            try:
                if driver.find_elements_by_id(弹窗_取消):
                    driver.find_element_by_id(弹窗_取消).click()
                elif driver.find_elements_by_id(弹窗_确认):
                    driver.find_element_by_id(弹窗_确认).click()
            except:
                pass
class  pad_mysql():
    def __init__(self,phone):
        a = my_sql_link_test()
        self.db = a.db
        self.cursor = self.db.cursor()
        self.phone=phone

    def get_gymId(self):
        cursor = self.cursor
        gym_Id = 'SELECT gym_id FROM coach WHERE TEL= '+str(self.phone)
        cursor.execute(gym_Id)
        gym_Id = cursor.fetchone()
        gym_Id = str(gym_Id)
        gym_Id = gym_Id[1:-2]
        self.db.commit()
        return gym_Id


    def clear_classes(self):
        sql_1 = 'DELETE  FROM   classes WHERE gym_id=  ' + self.get_gymId() + ' AND  start_time >\'' + time.strftime('%Y-%m-%d',time.localtime(time.time()))+' 00:00:00' + '\''
        self.cursor.execute(sql_1)
        self.db.commit()
    def add_class(self,add_time=1):
        user=self.phone
        user_uuid = [
            "f9c0d7800f53403eb7fef9b855830fbe",
            "1d119864-e71e-4784-a245-7c6545e87541",
            "824ebb1842094354890c77ce014b6915",
            "f7eeb5e1-4ac1-48fd-ba09-02999d053cb3",
            "49876c6a-0d51-4441-832e-168977bed031",
            "d40e05da-ca42-4218-9eee-d57b3f299002",
            "55119bbb-496c-4e66-bba7-3b0bf6e2f332",
            "5c39596c-9f7d-457d-a2ea-246a1994b4c5",
            '6ad1cf58-4b6a-4a24-8ec4-2b828b07a7f9'
        ]
        class_id = addclasses(user, user_uuid,add_time=add_time)
        return  class_id






if __name__ == '__main__':
    system = 'Andriod'  # 手机系统
    platformVersion = '5.1.1'  # 版本号 一定要填对
    driverName = 'YVF4C15821002901'  # 手机的
    url='http://127.0.0.1:4910/wd/hub'
    driver = appium(platformVersion, driverName,url)
    phone='15600905521'
    a=user_information(driver,phone,system)
    a.login_pad()






