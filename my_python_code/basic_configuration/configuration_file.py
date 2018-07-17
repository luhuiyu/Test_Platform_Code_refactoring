import requests
from my_python_code.mysql.Basic_information import *


MY_PYTHON_CODE_PATH=r'F:\Test_Platform_Code_refactoring'
MY_PYTHON_CODE_NAME=r'my_python_code'
MY_APICASE_PATH=r'myCase\api_case'
MY_API_CASE_LOG=r'F:\Test_Platform\my_log\my_api_case_log.txt'
my_api_case_log=MY_API_CASE_LOG


client = requests.session()  # requests 长链接
kk_test=my_sql_link_test() #连接kk的测试库
user_uuid = '4be9950e-cb60-4d0d-8861-f22debd00210' #用于测试的用户
web_user_name='luhuiyu'
oss_url='http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/'