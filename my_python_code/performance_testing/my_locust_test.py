import sys
import hashlib
import base64
import gzip
sys.path.append( 'E:\Test_Platform')
from locust import HttpLocust, TaskSet, task
from my_python_code.performance_testing.class_data import class_data


def login(client,user_name='15600905550', password='123456'):
    url_login = "http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2"
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    headers = {"Content-Type": "application/octet-stream", "Connection": "keep-alive", "Content-Encoding": "gzip",
               "Accept-encoding": "gzip"}
    login = client.post(url=url_login, headers=headers,catch_response=True)
    try:
        nonce = login.headers["Www-Authenticate"]  # 通过这样的方式可以获取到headers的各种东西
    except:
        return None
    password = str(base64.b64encode(password.encode(encoding="utf-8")))[2:-1]  # 密码转为base64编码，同时转换成字符串
    toMd5 = (nonce + user_name + password).replace("\n", "")
    md5 = hashlib.md5(toMd5.encode("utf-8")).hexdigest()  # toMd5转换成MD5 16进制
    temp = str(base64.b64encode(md5.encode(encoding="utf-8")))[2:-1]
    Authorization = "user=\"" + user_name + "\",response=\"" + temp + "\""
    headers111 = {

        "Connection": "keep-alive",
        "Authorization": Authorization,
    }
    return headers111
class UserBehavior(TaskSet):
    @task(1)
    def baidu(self):
        self.client.get("/")

    '''
    @task(6)
    def PadGetResourceListV2(self):
            url_login = "/PadCoachLoginV2"
            headers111 = login(self.client)
            self.client.post(url=url_login, headers=  headers111)
            self.client.post(url='/PadGetCourseDetailV2',json={"courseCode":"JZX2.0.4.1"},headers=headers111)

    '''



    @task(1)
    def PadGetCoachClassInfoV2(self):
        url_login = "/kcas/PadCoachLoginV2"
        headers111 = login(self.client)
        self.client.post(url=url_login, headers=headers111)
        self.client.post(url='/PadGetCoachClassInfoV2',json={"classesId":246800},headers=headers111)

    @task(2)
    def PadGetCoachClassListV2(self):
        url='/PadGetCoachClassListV2'
        url_login = "/PadCoachLoginV2"
        headers111 = login(self.client)
        self.client.post(url=url_login, headers=headers111)
        self.client.post(url=url,json='{"beginDate":1522319933345,"coachId":1429863157778432,"gymId":1383430562842624,"listRange":0,"listSort":0,"pageIndex":0,"pageSize":100}',headers=headers111)
'''
    @task(4)
    def PadSetCoachAssistantV2(self):
        url='/PadSetCoachAssistantV2'
        json_data={"classesId":248966,"coachAssistantTel":"15600905550"}
        url_login = "/PadCoachLoginV2"
        headers111 = login(self.client)
        self.client.post(url=url_login, headers=headers111)
        self.client.post(url=url,json=json_data,headers=headers111)

    @task(3)
    def PadGetCoachClassCheckinV2(self):
        url='/PadGetCoachClassCheckinV2'
        json_data = {"classesId":248966}
        url_login = "/PadCoachLoginV2"
        headers111 = login(self.client)
        self.client.post(url=url_login, headers=headers111)
        self.client.post(url=url, json=json_data, headers=headers111)

    '''
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100  #最小等待 ms
    max_wait = 100
    stop_timeout = 10
    #weight = 1   #权重
    host = "http://test.kuaikuaikeji.com/kcas"


if __name__ == "__main__":
    a=UserBehavior()
    a.PadGetResourceListV2()