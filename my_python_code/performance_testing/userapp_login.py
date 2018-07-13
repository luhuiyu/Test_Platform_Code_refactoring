import sys
import hashlib
import base64
import gzip
sys.path.append( 'F:\Test_Platform')
from locust import HttpLocust, TaskSet, task
from my_python_code.performance_testing.class_data import class_data
import requests,base64,gzip,hashlib
import ssl
import json
from multiprocessing import  Process, Pool,Queue,Manager

ssl._create_default_https_context = ssl._create_unverified_context
def make_password(aa='123456'):
    return hashlib.md5(aa.encode('utf-8')).hexdigest()
def headers(client, user_name, password='123456',
            url_login="https://ts.kuaikuaikeji.com/kas/ulogin"):  # 登录后返回headers
    password = make_password(password)
    headers = {"Content-Type": "application/octet-stream", "Connection": "keep-alive", "Content-Encoding": "gzip",
               "Accept-encoding": "gzip"}
    login = client.post(url=url_login, headers=headers)
    try:
        nonce = login.headers["Www-Authenticate"]  # 通过这样的方式可以获取到headers的各种东西
    except:
        pass
    password = str(base64.b64encode(password.encode(encoding="utf-8")))[2:-1]  # 密码转为base64编码，同时转换成字符串
    toMd5 = (nonce + user_name + password).replace("\n", "")
    md5 = hashlib.md5(toMd5.encode("utf-8")).hexdigest()  # toMd5转换成MD5 16进制
    temp = str(base64.b64encode(md5.encode(encoding="utf-8")))[2:-1]
    Authorization = "user=\"" + user_name + "\",response=\"" + temp + "\""
    headers = {

        "Connection": "keep-alive",
        "Authorization": Authorization,
    }
    return headers


class UserBehavior(TaskSet):


    @task(1)
    def PadGetResourceListV2(self):
        user = '15600905521'
        password = '123456'
        client =self.client  # 定义一个长链接
        headers1 = headers(client, user, password)
        login = client.post(url='https://ts.kuaikuaikeji.com/kas/ulogin', headers=headers1)
        print(login.status_code)
        data = {'classes_id': '246785', 'user_subject_uuid': '92bb167a-7f82-453e-b6c1-48c47a14245f'}
        headers1['Content-Type'] = "application/x-www-form-urlencoded"
        BB = client.post(url='https://ts.kuaikuaikeji.com/kas/reserveclasses', headers=headers1, data=data)
        print(11111111111111,BB.status_code)
        return headers1


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10  #最小等待 ms
    max_wait = 50
    stop_timeout = 10
    weight = 1   #权重
    host = "https://ts.kuaikuaikeji.com/kas/"


if __name__ == "__main__":
    a=UserBehavior()
    a.PadGetResourceListV2()