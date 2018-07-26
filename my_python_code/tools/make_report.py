#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests,hashlib,pymysql,json,time
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link,my_sql_link_buz
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.myCase.api_case.interface.login_args import headers
from my_python_code.tools.add_class import add_class
from my_python_code.basic_configuration.configuration_file import *
from imp import reload
def make_report(buz_class_id,course_code,subject_show_id,user_uuid_list=0,user_number=12,classes_checkin_number=12,dict_index='3',user='15600905550',password='123456'):

    client = requests.session()
    if user_uuid_list :
        class_id=add_class(time.time(), 'A店', str(user_number), str(classes_checkin_number), course_code, subject_show_id,user_uuid_list=user_uuid_list)
    else:
        class_id=add_class(time.time(), 'A店', str(user_number), str(classes_checkin_number), course_code, subject_show_id,dict_index=dict_index)
    headers1 = headers(client, user, password)
    login_pad = client.post(url='http://test.kuaikuaikeji.com/kcas/PadCoachLoginV2', headers=headers1)
    home = orm_to_mysql(my_sql_link())
    kk_buz=orm_to_mysql(my_sql_link_buz())
    kk_test=orm_to_mysql(my_sql_link_test())
    data_uuid=kk_buz.table("user_class_data").select("data_uuid",class_id=buz_class_id).one()['data_uuid']
    if data_uuid == None:
        return {'classReportList':[{'reportUrl':'没有这个classid，看看是不是现网的'}]}
    user_class_data=requests.get(url=oss_url+data_uuid+'.txt').content
    data=eval(user_class_data)
    if user_uuid_list == False:
        uuid_list =uuid_idct[dict_index]
    else:
        uuid_list=user_uuid_list
    for x in range(len(data['classDataList'])):
            uuid = data['classDataList'][x]['userUuid']
            data['classDataList'][x]['userUuid'] = uuid_list[x]
           # kk_test.table('user_daily_weight').delete(user_uuid=uuid_idct[dict_index][x])
          #  get_weight_data=kk_buz.table("user_daily_weight ").select( 'MAX(id)','weight','fat_rate','water_rate','musle_rate','user_bmr',user_uuid= str(uuid) ,pad_weight_source_type=3,).one()
           # if get_weight_data['fat_rate'] != None:
           #     data['classDataList'][x]["weightData"] = {
            #        "dataSourceType": 1,
             #       "entrailsFat": 9,
             #       "fatRate": get_weight_data['fat_rate'],
             #       "musleRate": get_weight_data['musle_rate'],
              #      "skeletonRate": 3.7,
              #      "userBmr": get_weight_data['user_bmr'],
               #     "waterRate": get_weight_data['water_rate'],
             #       "weight": get_weight_data['weight']
           #     }
        #    else:

            #data['classDataList'][x]["weightData"] = {
           #     "dataSourceType": 1,
         #       "entrailsFat": 9,
        #        "fatRate": 30,
         #       "musleRate": 54.9,
        #        "skeletonRate": 3.7,
         #       "userBmr": 1888,
        #        "waterRate": 43.3,
        #        "weight": 100
        #    }
       #     print( data['classDataList'][x]["weightData"])
    for x in range(0,13):
        try:
            data['classDataList'][x]['classesId'] = class_id
            data['classDataList'][x]['courseCode']=course_code
        except:
            pass
    start_time=time.time()
    updata=client.post(url='http://test.kuaikuaikeji.com/kcas/PadUploadAllClassDataV2', json=data)
    end_time=time.time()
  #  print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
  #  print(end_time-start_time)

    json = {"classesId": class_id, "subjectId": 1441109786806272}
    PadGetClassReportList = client.post(url='http://test.kuaikuaikeji.com/kcas/PadGetClassReportListV2', json=json,headers=headers1)  # 获取报告
    home.close()
    kk_buz.close()
    kk_test.close()
   # print(class_id)
  #  print(PadGetClassReportList.json())
    if PadGetClassReportList.json():
         return PadGetClassReportList.json()
    else:
        return {'classReportList':[{'reportUrl':'没有这个classid，看看是不是现网的'}]}

if __name__ == '__main__':
    #kk_test = orm_to_mysql(my_sql_link_test())
    user_uuid = ['05ddaf38-d946-4649-b06d-36c02fed1e69']
    for x in range(1):
        make_report(buz_class_id=331096, course_code='JZX2.0.3.1', subject_show_id='1',user_uuid_list=user_uuid,user_number=1, classes_checkin_number=1)

    #  make_report(buz_class_id=218604,course_code='JZX2.0.4.1',subject_show_id='1',dict_index='4')
    # for  x in  range(1):
     #  #  kk_test.table('user_daily_weight').updata({'weight':x},id=)
      #   make_report(buz_class_id=331096, course_code='JZX2.0.2.5', subject_show_id='1', dict_index='4')
