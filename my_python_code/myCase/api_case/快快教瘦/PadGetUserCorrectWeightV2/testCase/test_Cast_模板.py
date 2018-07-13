#!/usr/bin/env python
#coding=utf-8
import pymysql
import requests

from  weight_interface.function import weight_testCase


def test_Case(client,db, cursor, user_uuid ):
        old_fatRate_list = [int,int]  #创造在数据库里面已经有的体脂率的数据，int类型或是str
        corr_time_list = [int,int]# 数据创建的时间 int类型
        fatRate = int  # 称重得到的体脂率  int类型
        corr_Fatrate = int # 被修改后的体脂率   int类型
        case_Result=weight_testCase(client,db, cursor, user_uuid,old_fatRate_list,fatRate,corr_Fatrate,corr_time_list)
        if case_Result==0:
            print('-出现错误')
        return case_Result






if __name__ == '__main__':
    client = requests.session()  # requests 长链接
    db = pymysql.connect("192.168.41.20", "kms", "kuaikuaikms", "kk_test", 33061, charset='utf8')  # 连接数据库
    cursor = db.cursor()
    user_uuid = '4be9950e-cb60-4d0d-8861-f22debd00210'
    print(test_Case(client,db, cursor, user_uuid))