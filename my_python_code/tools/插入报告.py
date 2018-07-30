import  pymongo
from my_python_code.tools.make_report  import make_report
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link_buz
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from sshtunnel import SSHTunnelForwarder
from my_python_code.mysql.my_mogodb_aliyun import get_aliyun_mongo_client
from django.utils import timezone
import requests
from my_python_code.basic_configuration.configuration_file import *
import time

def up_report_to_test(user_uuid,test_db,mongo_client,buz_mysql,tset_mysql):
    test_db_coll = test_db["user_report_plus"]
    test_db_coll.delete_many({'user_uuid': user_uuid})
    tset_mysql.table('user_report').delete(user_uuid=user_uuid)
    tset_mysql.table('user_daily_weight').delete(user_uuid=user_uuid)
    user_daily_weight_data = buz_mysql.table('user_daily_weight').select(user_uuid=user_uuid).all()
    user_data = buz_mysql.table('user').select(uuid=user_uuid).one()
    tset_mysql.table('user').insert(user_data)
    # user_report=buz_mysql.table('user_report').select(subject_show_id=1,user_uuid=user_uuid,VERSION=3).limit(0,99).all()
    user_report = buz_mysql.my_sql('SELECT * FROM user_report WHERE user_uuid= ' + '\'' + str(user_uuid) + '\'' + ' AND  (subject_show_id=1 OR  subject_show_id=0) AND VERSION=3 LIMIT 0,99')
    for x in user_daily_weight_data:
        tset_mysql.table('user_daily_weight').insert(x)
    today_weight= tset_mysql.table('user_daily_weight').select('id',user_uuid=user_uuid).order_by('id').limit(1).one()
 #   tset_mysql.table('user_daily_weight').updata({'create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))},id=today_weight['id'])
    for x in user_report:
        tset_mysql.table('user_report').insert(x)
        buz_class_id = buz_mysql.table('classes').select(id=x['classes_id']).one()
        tset_mysql.table('classes').insert(buz_class_id)
        buz_user_classes_id=buz_mysql.table('user_classes').select(classes_id=x['classes_id']).one()
        tset_mysql.table('user_classes').insert(buz_user_classes_id)
        report_data2 = mongo_client["kk_buz"]["user_report_plus"].find({'uuid': x['uuid']})
        i = 0
        for y in report_data2:
            test_db_coll.insert(y)
            i = i + 1
    return

if __name__ == '__main__':
    buz_mysql = orm_to_mysql(my_sql_link_buz())
    tset_mysql = orm_to_mysql(my_sql_link_test())
    user_list=['0ab00aef-0692-4269-ae27-849e9dd75163','0d406f44-df35-44c5-9b8b-2239f8b1cf85']
    test_client = pymongo.MongoClient("192.168.40.207:27017")
    test_db = test_client["kk_buz"]
    test_db.authenticate("root", "Kuaimongodb001Kuai")
    mongo_client = get_aliyun_mongo_client()
   # user_list=buz_mysql.my_sql( 'SELECT user_uuid FROM user_report  WHERE (subject_show_id=1 OR subject_show_id=0 ) AND VERSION=3 GROUP BY user_uuid HAVING COUNT(user_uuid) > 99;')
    client = requests.session()
    user_list=[{'user_uuid': 'dbf8dffc-8675-4daa-aa74-eadc5ae34c08'}, ]

    for user_uuid in user_list:
        user_uuid=user_uuid['user_uuid']
        up_report_to_test(user_uuid,test_db,mongo_client,buz_mysql,tset_mysql)
       # my_url=make_report(buz_class_id=331096, course_code='JZX2.0.2.5', subject_show_id='1',user_uuid_list=[user_uuid],user_number=1, classes_checkin_number=1)
       # print(my_url)
       # time.sleep(3)
        print(user_uuid)









        # json_url=str(my_url['classReportList'][1]['reportUrl']).replace('http://test.kuaikuaikeji.com/kas/movereport/?i=','http://192.168.41.41/KKNewReport/PadGetUUIDUserReportV3?i=')

        #        json_data=client.get(url=json_url ).json()
     #   json_list=[]
      #  for x in    json_data['strengthAvgs']['strengthHundred']:
      #      json_list.append(x['totalStrength'])
      #  print(json_list)
     #A   with open('json.txt', 'a') as f:
     #       f.write(str(json_list)+',')