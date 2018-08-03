#!/usr/bin/env python
from appium import webdriver
import time,os,re
import pymysql
from  my_python_code.tools.add_class import add_class
import logging
from my_python_code.mysql.Basic_information import my_sql_link_test_pool
from  my_python_code.myCase.appium_case.快快教瘦.interface.Bascic_appid_name import  *
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('mod_class')
from PIL import Image
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
import random

def get_error(test_case):  # 装饰器，
    def wrapper(*args, **kw):
        try:
            return test_case(*args, **kw)
        except  Exception as e:
          #  print(args)
            return {'driverName':  args[0]['deviceName'], "result": -1, "error_info": '\'' + str(e) + '\''}
    return wrapper


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
    desired_caps['unicodeKeyboard'] = 'true'
   # desired_caps['exported'] ='true'
    desired_caps['automationName'] ='appium' #使用的引擎
 #   desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['resetKeyboard'] = 'true'
    desired_caps['newCommandTimeout']='30' #最大无响应时间
    driver = webdriver.Remote(url, desired_caps)
    driver.implicitly_wait(10)
    return driver
class user_information ():
    def __init__(self,driver=None,phone=None,system=None,driverName=None):
        self.driver=driver
        self.phone=phone
        self.system=system
        self.driverName=driverName
        self.w = driver.get_window_size()['width']
        self.h = driver.get_window_size()['height']
    def configure_instructor(self):
        driver=self.driver
        assert driver.find_element_by_id('com.kk.coachpad:id/et_assistant_phone_num').text == '请输入辅导员的手机号'
        assert driver.find_element_by_id('com.kk.coachpad:id/tv_assistant_name').text == '无'
        driver.find_element_by_id('com.kk.coachpad:id/et_assistant_phone_num').send_keys('15600905550')
        driver.find_element_by_id('com.kk.coachpad:id/btn_add_modify_assistant').click()
        time.sleep(3)
        assert driver.find_element_by_id('com.kk.coachpad:id/tv_assistant_name').text == '测试教练_5550'
        time.sleep(3)
        driver.find_element_by_id('com.kk.coachpad:id/btn_confirm').click()
    def wait_unit(self):
        i = 0
        while i <   60:
            if self.driver.find_elements_by_id(课程剩余时间):
                start_time= self.driver.find_element_by_id(课程剩余时间).text
                logger.info('start_time:'+str(start_time))
                return
            else:
                start_time=False
            i=i+1
        assert start_time
        time_total=int(start_time[0:2])*60+int(start_time[3:5])
        while i < time_total:
            try:
                subject_time=self.driver.find_elements_by_id(课程剩余时间)
                if subject_time:
                    logger.info(str('课程剩余时间：'+str(subject_time[0].text)))
                    if self.driver.find_element_by_id(课程剩余时间).text == '00:00':
                        return
                else:
                    logger.info(str('点击 ：'+'1730, 800'))
                    self.ac_click(1730, 800, self.driverName)
            except:
                i = i + 1
                logger.info('查询失败 '+str('点击 ：' + '1730, 800'))
                self.ac_click(1730, 800, self.driverName)





                #else:
                 #   print(self.driver.find_element_by_id(课程剩余时间).text )
    def get_screenshot_by_element(self, element,TEMP_FILE):  #第一个参数  driver.find_element_by_id(登录页面_快快身体评测)  第二个是保存的地址
        # 先截取整个屏幕，存储至系统临时目录下
        self.driver.get_screenshot_as_file(TEMP_FILE)
        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
        # 截取图片
        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)
        return self
    def only_number(self,subject_id):
        subject_id=str(subject_id)
        subject_id=re.sub("\D", "",subject_id)   #去除非数字
        return subject_id
    def wipe_up(self,element=False):#上滑
        driver=self.driver
        logging.info('wipe_up')
        if element:
            location = element.location
            x = location['x']
            y = location['y']
            driver.swipe(int(x), int(y), int(x), int(y+300), 1000)
        else:
            w= self.w
            h= self.h
            x1=0.5*w
            y1=0.5*h
            y2=0.7*h
            driver.swipe(int(x1),int(y2),int(x1),int(y1),500)
        time.sleep(2)
    def wipe_down(self,element=False):#下滑
        logging.info('wipe_down')
        driver=self.driver
        if element:
            location = element.location
            x = location['x']
            y = location['y']
            driver.swipe(int(x), int(y), int(x), int(y - 300), 1000)
        else:
            w= self.w
            h= self.h
            x1=0.5*w
            y1=0.4*h
            y2=0.9*h
            time.sleep(1)
            driver.swipe(int(x1),int(y1),int(x1),int(y2),1000)
        time.sleep(3)
    def wipe_left(self): #左滑
        driver = self.driver
        if element:
            location = element.location
            x = location['x']
            y = location['y']
            driver.swipe(int(x), int(y), int(x - 300), int(y), 1000)
        else:
            w= self.w
            h= self.h
            x1=0.2*w
            y1=0.5*h
            x2=0.6*w
            driver.swipe(int(x2),int(y1),int(x1),int(y1),1000)
        time.sleep(2)
    def wipe_right(self,element=False): #右滑
        driver = self.driver
        if  element:
            location = element.location
            x=location['x']
            y=location['y']
            driver.swipe(int(x), int(y), int(x+300), int(y), 1000)
        else:
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
        #print(x,y)
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
            if eval(l) != []:
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
            return True
        except:
            return False
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
        logon_index=0
        while not driver.find_elements_by_id('body_ms')  and logon_index<5  :
            logger.info('进入登录重试循环，次数为 ： '+str(logon_index))
            if driver.find_elements_by_id('bt_ok'):
                driver.find_element_by_id('bt_cancel').click()
            if driver.find_elements_by_id(登录_密码):
                driver.find_element_by_id(登录_账号).clear()
                driver.find_element_by_id(登录_账号).set_value(self.phone)
                driver.find_element_by_id(登录_密码).clear()
                driver.find_element_by_id(登录_密码).set_value('123456')
                driver.find_element_by_id(登录按钮).click()
            time.sleep(5)
            logon_index=logon_index+1
    def binding_arm(self,driverName=None,arm_times=6):
        if driverName == None:
            driverName=self.driverName
        for i in range(arm_times):
            driver = self.driver
            user_bind_list = driver.find_elements_by_id(连接臂带)
            logger.info(str(driverName)+'  user_bind_list   '+str(len(user_bind_list)))
            if len(user_bind_list)>0:
                user_bind_list[random.randint(0,len(user_bind_list)-1)].click()
                bind_list_in_popup=driver.find_elements_by_id(绑定臂带)
                void_bind_list=[]
                for x in bind_list_in_popup:
                    if x.is_enabled()==False:
                        void_bind_list.append(x)
                if void_bind_list:
                    void_bind_list[random.randint(0,len(void_bind_list)-1)].click()
                    self.ac_click(1730, 800, driverName)
                else:
                    self.wipe_up()
                    self.wipe_up()
                    self.wipe_up()
                    void_bind_list_down = []
                    bind_list_down = driver.find_elements_by_id(绑定臂带)
                    for x in bind_list_down:
                        if x.is_enabled() == False:
                            void_bind_list_down.append(x)
                    if  void_bind_list_down:
                        void_bind_list_down[random.randint(0,len(void_bind_list_down)-1)].click()
            self.ac_click(1730, 800, driverName)
    def  just_in_time_switch_unit(self):#准时的切换单元
        b = self.driver.find_elements_by_id('unit_duration')
        driver=self.driver
        self.wait_unit()
        logging.info('第一单元')
        b[1].click()
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(4)
        self.wait_unit()
        b[2].click()
        logging.info('第二单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(4)
        self.wait_unit()
        b[3].click()
        logging.info('第三单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(4)
        self.wait_unit()
        b[4].click()
        logging.info('第四单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(4)
        self.wait_unit()
        b[5].click()
        logging.info('第五单元')
        driver.find_element_by_id(弹窗_确认).click()
        time.sleep(4)
        self.wait_unit()
    def end_courses(self):
        driver = self.driver
        driver.find_elements_by_id(单元小节图片)[6].click()
        i = 0
        while not driver.find_elements_by_id(报告页标题) and i < 5:
            logging.info('结束课程  尝试 第 '+str(i)+ '次')
            try:
                if driver.find_elements_by_id(弹窗_取消):
                    driver.find_element_by_id(弹窗_取消).click()
                elif driver.find_elements_by_id(弹窗_确认):
                    driver.find_element_by_id(弹窗_确认).click()
                i = i + 1
            except:
                i = i + 1
                if i>5:
                    return
    def inspect_weight(self):
        driver = self.driver
        driver.find_element_by_id(称重_性别男).click()
        driver.find_element_by_id(称重_年龄).clear()
        driver.find_element_by_id(称重_年龄).set_value('25')
        driver.find_element_by_id(称重_安静心率).clear()
        driver.find_element_by_id(称重_安静心率).set_value('65')
        driver.find_element_by_id(称重_姓名).clear()
        driver.find_element_by_id(称重_姓名).set_value('appium_test')
        driver.find_element_by_id(称重_身高).clear()
        driver.find_element_by_id(称重_身高).set_value('165')
        driver.find_element_by_id(称重_体重).click()
        driver.find_element_by_id(弹窗_确认).click()
        driver.find_element_by_id(称重_保存).click()
    def inspect_weight_JXSXBJ(self):
        driver = self.driver
        A=driver.find_elements_by_id('com.kk.coachpad:id/edit_text')
        driver.find_element_by_id(称重_性别男).click()
        driver.find_element_by_id('com.kk.coachpad:id/tv_weight_delta').click()
        driver.find_element_by_id(弹窗_确认).click()
        #姓名
       # A[0].clear()
      #  A[0].set_value('塑性防爆搏击')
        A[1].clear()
        A[1].set_value('27')
        A[2].clear()
        A[2].set_value('188')
        A[3].clear()
        A[3].set_value('70')
        A[4].clear()
        A[4].set_value('100')
        A[5].clear()
        A[5].set_value('90')
        A[6].clear()
        A[6].set_value('95')
        A[7].clear()
        A[7].set_value('40')
        A[8].clear()
        A[8].set_value('2')
        A[9].clear()
        A[9].set_value('40')
        A[10].clear()
        A[10].set_value('2')
        driver.find_element_by_id(称重_保存).click()
    def inspect_weight_SX(self):
            pass
class  pad_mysql(orm_to_mysql):

    def __init__(self,phone):
        a = my_sql_link_test_pool()
        self.db = a.db
        self.cursor = a.cursor_dict
        self.phone=phone

    def get_gymId(self):
        cursor = self.cursor
        gym_Id = 'SELECT gym_id FROM coach WHERE TEL= '+str(self.phone)
        cursor.execute(gym_Id)
        gym_Id = cursor.fetchone()
        if  gym_Id :
            gym_Id = str(gym_Id['gym_id'])
            self.db.commit()
            return gym_Id
        else:
            return 'tel 错误'



    def clear_classes(self):
        sql_1 = 'DELETE  FROM   classes WHERE gym_id=  ' + self.get_gymId() + ' AND  start_time >\'' + time.strftime('%Y-%m-%d',time.localtime(time.time()))+' 00:00:00' + '\''
        self.cursor.execute(sql_1)
        self.db.commit()


    def add_class(self,add_time=1,store_name=None, user_number='12',classes_checkin_number='10',course_code='FB.1.0.1.1',subject_show_id=4,dict_index='2',end_time=10800):
        coach_phone=self.phone
        star_time=time.time()+add_time
        class_id =add_class(star_time=star_time,store_name=store_name,user_number=user_number,classes_checkin_number=classes_checkin_number,course_code=course_code,subject_show_id=subject_show_id,dict_index=dict_index,coach_phone=coach_phone,end_time=end_time)
       # print(class_id)

        return  class_id






if __name__ == '__main__':
    use_mysql = pad_mysql('15600905521')
   # use_mysql.clear_classes()
   # use_mysql.add_class(1)
   # print(use_mysql.table("user").select(id=79).one())




