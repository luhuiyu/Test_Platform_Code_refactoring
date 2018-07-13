#!/usr/bin/env python
#coding=utf-8

import hashlib
import base64,requests
def headers(client,user_name,password='123456',url_login="http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2"):  #登录后返回headers
        password = make_password(password)
        headers = {"Content-Type": "application/octet-stream","Connection": "keep-alive","Content-Encoding": "gzip", "Accept-encoding": "gzip"}
        login=client.post(url=url_login,headers=headers)
        try:
                nonce1=login.headers["Www-Authenticate"] # 通过这样的方式可以获取到headers的各种东西
        except:
               return  False
        password=str(base64.b64encode(password.encode(encoding="utf-8") ))[2:-1] #密码转为base64编码，同时转换成字符串
        toMd5=(nonce1+user_name+password).replace("\n", "")
        md5=hashlib.md5(toMd5.encode("utf-8")).hexdigest()  #toMd5转换成MD5 16进制
        temp=str(base64.b64encode(md5.encode(encoding="utf-8")))[2:-1]
        Authorization="user=\""+user_name+"\",response=\""+temp+"\""
        headers = {

            "Connection":"keep-alive",
           "Authorization":Authorization,
        }
        return headers

def make_password(aa='123456'):
    return hashlib.md5(aa.encode('utf-8')).hexdigest()

def  login(client,user='15600905550',password='123456'):
        headers1 = headers(client, user, password)
        login_pad = client.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2', headers=headers1)

        return headers1

if __name__=='__main__':
        client = requests.session()  # 定义一个长链接
        user = '15600905550'
        password = '123456'

      #  headers = headers(client, user, password)
       # login_pad = client.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2', headers=headers)
        print(login(client,user,password))