from my_python_code.myCase.api_case.interface.login_args import login
import my_python_code.myCase.api_case.interface.Basic_information
import  my_python_code.myCase.api_case.interface.接口记录
import requests
from my_python_code.myCase.api_case.interface.login_args import headers
import logging.handlers
import time
import os
from my_python_code.basic_configuration.configuration_file import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
#if not os.path.exists( 'log_Warehouse'):
    #    os.makedirs('log_Warehouse')

LOG_FILE=my_api_case_log
#LOG_FILE = 'log_Warehouse/'+time.strftime('%Y_%m_%d %H_%M_%S__',time.localtime(time.time()))+'testlog.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024 * 1024, backupCount=5)  # 实例化handler
fmt = '[ %(asctime)s - %(filename)s:%(lineno)s - %(levelname)s ] [%(funcName)s]   %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter
handler.setLevel(logging.INFO)
def put_log():
    global handler
    return handler


def get_error(test_case):  # 装饰器，
    def wrapper(*args, **kw):
        try:
            return test_case(*args, **kw)
        except  Exception as e:
            return {"result": -1, "error_info": '\'' + str(e) + '\''}

    return wrapper
class Basics_case():
  @get_error
  def __init__(self):  #基本设置
    self.url = my_python_code.myCase.api_case.interface.Basic_information.main_url  # 主地址，可以切换现网 测试网或者不同app的
    self.client = requests.session()    #定义一个长链接
    self.db=kk_test.db  #赋值数据库
    self.cursor=kk_test.cursor
    #self.logger = logging.getLogger('Basics_case')  #不填就捕获所有的log
    self.logger = logging.getLogger()
    self.logger.addHandler(handler)  # 为logger添加handler
    self.logger.setLevel(logging.INFO)
    self.orm = orm_to_mysql(my_sql_link())
    #  self.logger.info(id(self.logger))
    try:    #如果有给json就使用给的json，没有就给一个默认的
         if  standard_json :
             pass
    except NameError:
        try:
            exec('import my_python_code.myCase.api_case.API_json_format.'+self.API_name)
            self.standard_json=eval('my_python_code.myCase.api_case.API_json_format.'+self.API_name+'.standard_json')  # 获取最新的json格式
        except:
            pass
  @get_error
  def API_url(self,api_name=None):   # 拼接完整的url
    if api_name:
        API_url = self.url + api_name
    else:
        API_url  = self.url +self.API_name
    return API_url
  def login(self, user='15600905550', password='123456'):
      headers1 = headers(self.client, user, password)
      login_pad = client.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2', headers=headers1)
      self.login_headers=headers1
      return headers1
  @get_error
  def test_case(self):  # 对比和 web_platform_pad_pesourcelist 保存的数据是否一致
      heard = self.login()
      error_list = []
      sgin = True
      all_case_json = self.orm.table('web_platform_comparison_library').select(api_name=self.API_name).all()
      if len(all_case_json)==0:return {"result": -1, "error_info": 'not case'}
      for x in all_case_json:
          start_time=time.time()
          rult = {'id': x['id']}
          case_rult = self.client.post(url=self.API_url(), json=eval(x['send_json']), headers=heard)
          try:
              if not case_rult.status_code == int(x['status_code']):
                  rult["error_info"] =  str('status_code  : ')+str(case_rult.status_code)
                  rult['result'] = '0'
                  sgin = False
              if eval(x['receive_json'])== {}:
                  pass
              else:
                  if not case_rult.json() == eval(x['receive_json']):
                      logging.info(str(case_rult.json()))
                      rult["error_info"] = "JSON contrast failure"
                      rult['result'] = '0'
                      sgin = False
          except  :
              rult["error_info"] = "JSON  is not in  "
              rult['result'] = '0'
              sgin = False
          if 'result'  in rult.keys(): error_list.append(rult)
          end_time=time.time()
          self.logger.info(end_time-start_time)
      self.orm.close()
      if sgin: return {"result": 1}
      else:return {"result": 0, "error_info": error_list}
  @get_error
  def compare(self,expected_result,json=None):  #对比结果 统一调用获取最后结果的时候都用他
      operation_resultself=self.test_case(self,json)
      if operation_resultself.status_code==expected_result:
          return 1
      else:
        return 0

  def contrast_json(self,*args):
      dict_rult = {}
      dict_repeat = {}
      if len(args) == 0:
          return
      for x in range(len(args)):
          assert isinstance(args[x], dict), '输入的不为dict类型'
          dict_rult = dict(dict_rult, **args[x])
      for y in range(1, len(args)):
          for i in args[y].items():
              if i[0] in dict_rult.keys():
                  if dict_rult[i[0]] == i[1]:
                      dict_rult.pop(i[0])
                  elif dict_rult[i[0]] != i[1]:
                      if i[0] in dict_repeat.keys():
                          dict_repeat[i[0]] = str(dict_repeat[i[0]]) + str(i[1])
                          dict_rult.pop(i[0])
                      else:
                          dict_repeat[i[0]] = i[1]
                          dict_rult.pop(i[0])
                          #  self.logger.info(dict_rult)
                          #    self.logger.info(dict_repeat)
      return dict_repeat


if __name__=='__main__':
    example=Basics_case()
    self.logger.info(example.test_case())