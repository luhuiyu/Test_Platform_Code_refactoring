#!/usr/bin/env python
#coding=utf-8
from copy import deepcopy
import requests,time
import pymysql
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case

def clean_user_daily_weight(db,cursor,user_uuid):#这个函数是为了清空测试账号的称重信息
    sql = 'DELETE  FROM user_daily_weight WHERE user_uuid=\''+user_uuid+'\''
    cursor.execute(sql)
    db.commit()
def make_user_daily_weight(db,cursor,create_time,fat_rate,user_uuid):# n 代表造几条称重数据
    fat_rate=str(fat_rate)
    sql= 'INSERT  INTO user_daily_weight(user_uuid, create_time, fat_rate, weight, water_rate,entrails_fat,TYPE,musle_rate)VALUES(\''+user_uuid+'\', \''+create_time+'\', \''+fat_rate+'\', \'80\', \'50\', \'5\', \'1\', \'60\')'
    cursor.execute(sql)
    #print(sql)
    db.commit()
def get_weight_json():
    json = {
        "initWeightData": {
            "dataSourceType": 1,
            "entrailsFat": 5,  # 内脏脂肪
            "fatRate": 10,  # 脂肪率
            "macAddress": "E8:9D:DD:8C:08:D1",
            "musleRate": 68.5,  # 肌肉率
            "resistance": 463.29998779296875,  # 电阻
            "skeletonRate": 4.6,  # 骨骼率
            "userBmr": 1547,  # 用户bmr
            "waterRate": 51.1,  # 水分率
            "weight": 64.2  # 体重
        },
        "userUuid": 'XXX'
    }
    return json

def get_error(test_case):
    def wrapper(*args, **kw):
        try :
             return  test_case(*args, **kw)
        except  Exception as e :
            return {"result":-1,"error_info": '\''+str(e)+'\''}
    return wrapper


def weight_testCase(client,db, cursor, user_uuid,old_fatRate_list,fatRate,corr_Fatrate,corr_time):#测试用的方法，用例都要先调用这个
    try:
        fatRate=str(fatRate)
        clean_user_daily_weight(db, cursor, user_uuid)  # 为了清空测试账号的称重信息
        i=0
        for x in old_fatRate_list:
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - corr_time[i]))
            i = i + 1
            make_user_daily_weight(db, cursor, create_time, x, user_uuid)  #
        weight_json=get_weight_json()
        weight_json["initWeightData"]["fatRate"] = fatRate  ## 脂肪率
        weight_json["userUuid"] = user_uuid
        corr_weigt = client.post(url='http://test.kuaikuaikeji.com/kcas/PadGetUserCorrectWeightV2', json=weight_json)
        print(corr_weigt.json()["corrWeightData"] )
        #print(str(corr_weigt.json()["corrWeightData"]["fatRate"]))
        if float(corr_weigt.json()["corrWeightData"]["fatRate"])==float(corr_Fatrate):
            return {"result":1}
        else:
            return   {"result":0,"error_info": str(corr_weigt.json())}
    except Exception as e:
            return {"result":-1,"error_info": '\''+str(e)+'\''}


class weight_case_class(Basics_case):
    def clean_user_daily_weight(self,db, cursor, user_uuid):  # 这个函数是为了清空测试账号的称重信息
        sql = 'DELETE  FROM user_daily_weight WHERE user_uuid=\'' + user_uuid + '\''
        cursor.execute(sql)
        db.commit()
    def make_user_daily_weight(self,db, cursor, create_time, fat_rate, user_uuid):  # n 代表造几条称重数据
        fat_rate = str(fat_rate)
        sql = 'INSERT  INTO user_daily_weight(user_uuid, create_time, fat_rate, weight, water_rate,entrails_fat,TYPE,musle_rate)VALUES(\'' + user_uuid + '\', \'' + create_time + '\', \'' + fat_rate + '\', \'80\', \'50\', \'5\', \'1\', \'60\')'
        cursor.execute(sql)
        # print(sql)
        db.commit()
    def get_weight_json(self):
        json = {
            "initWeightData": {
                "dataSourceType": 1,
                "entrailsFat": 5,  # 内脏脂肪
                "fatRate": 10,  # 脂肪率
                "macAddress": "E8:9D:DD:8C:08:D1",
                "musleRate": 68.5,  # 肌肉率
                "resistance": 463.29998779296875,  # 电阻
                "skeletonRate": 4.6,  # 骨骼率
                "userBmr": 1547,  # 用户bmr
                "waterRate": 51.1,  # 水分率
                "weight": 64.2  # 体重
            },
            "userUuid": 'XXX'
        }
        return json
    def get_error(self,test_case):
        def wrapper(*args, **kw):
            try:
                return test_case(*args, **kw)
            except  Exception as e:
                return {"result": -1, "error_info": '\'' + str(e) + '\''}

        return wrapper
    def weight_testCase(self,client, db, cursor, user_uuid, old_fatRate_list, fatRate, corr_Fatrate,
                        corr_time):  # 测试用的方法，用例都要先调用这个
        try:
            fatRate = str(fatRate)
            self.clean_user_daily_weight(db, cursor, user_uuid)  # 为了清空测试账号的称重信息
            i = 0
            for x in old_fatRate_list:
                create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - corr_time[i]))
                i = i + 1
                self.make_user_daily_weight(db, cursor, create_time, x, user_uuid)  #
            weight_json = self.get_weight_json()
            weight_json["initWeightData"]["fatRate"] = fatRate  ## 脂肪率
            weight_json["userUuid"] = user_uuid
            corr_weigt = client.post(url='http://test.kuaikuaikeji.com/kcas/PadGetUserCorrectWeightV2',
                                     json=weight_json)
            print(corr_weigt.json()["corrWeightData"])
            # print(str(corr_weigt.json()["corrWeightData"]["fatRate"]))
            if float(corr_weigt.json()["corrWeightData"]["fatRate"]) == float(corr_Fatrate):
                return {"result": 1}
            else:
                return {"result": 0, "error_info": str(corr_weigt.json())}
        except Exception as e:
            return {"result": -1, "error_info": '\'' + str(e) + '\''}


if __name__ == '__main__':
    client = requests.session()  # requests 长链接
    db = pymysql.connect("192.168.41.20", "kms", "kuaikuaikms", "kk_test", 33061, charset='utf8')  # 连接数据库
    cursor = db.cursor()
    user_uuid = '4be9950e-cb60-4d0d-8861-f22debd00210'
    result = []
    old_fatRate_list = ['22', '22']  # 用于构建原有的数据，参数是体脂率
    corr_time_list = [87600, 150000]  # 86400一天，这个是控制制造的称重数据是在哪一天的
    fatRate = '24.1'  # 称重得到的体脂率
    corr_Fatrate = '22'  # 被修改后的体脂率
    result.append(weight_testCase(db, cursor, user_uuid, old_fatRate_list, fatRate, corr_Fatrate, corr_time_list))
    print(result)


