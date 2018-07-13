import  requests
import gzip
import os
import json
import time
from my_python_code.myCase.api_case.interface.login_args import headers
def print_now(node):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        return node
@print_now
def up_report_data(**kwargs):  #xianwang c
    data = gzip.compress(str(data).encode('utf-8'))
    headers1=headers(client,coach_phone,url_login=url_main+"PadCoachLoginV2")
    print('登录状态'+str(client.post(url=url_main+'PadCoachLoginV2', headers=headers1).status_code))
    headers1["Content-Encoding"] = "gzip"
    print('报告上传状态'+str(client.post(url=url_main+'PadUploadAllClassDataV2',data=data,headers=headers1).status_code))
if __name__ == '__main__':
    client = requests.session()
    coach_phone='13691421359'
    for root, dirs, files in os.walk('现网数据', topdown=False):
        for txt in files:
             up_report_data(client=client,
                           coach_phone=coach_phone,
                           data=json.loads(open(('现网数据\\' + str(txt)), encoding='utf-8').read())
                           )


   #