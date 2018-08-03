import  pymongo
from my_python_code.tools.make_report  import make_report
from my_python_code.mysql.Basic_information import my_sql_link_test_pool
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from sshtunnel import SSHTunnelForwarder
from my_python_code.mysql.my_mogodb_aliyun import get_aliyun_mongo_client
from django.utils import timezone
import requests
from my_python_code.basic_configuration.configuration_file import *
import time,logging
logging.basicConfig(level=logging.ERROR)

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
    tset_mysql.table('user_daily_weight').updata({'create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))},id=today_weight['id'])
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
    buz_mysql = orm_to_mysql(my_sql_link_buz_pool())
    tset_mysql = orm_to_mysql(my_sql_link_test_pool())
    test_client = pymongo.MongoClient("192.168.40.207:27017")
    test_db = test_client["kk_buz"]
    test_db.authenticate("root", "Kuaimongodb001Kuai")
    mongo_client = get_aliyun_mongo_client()
   # user_list=buz_mysql.my_sql( 'SELECT user_uuid FROM user_report  WHERE (subject_show_id=1 OR subject_show_id=0 ) AND VERSION=3 GROUP BY user_uuid HAVING COUNT(user_uuid) > 99;')
    client = requests.session()
    user_list=[     {'user_uuid': '4a536634-83a9-4b30-9449-6eda3456a55f'}, {'user_uuid': '4ac8b3c6-dc60-4cfb-bb39-4740bb0e65fd'}, {'user_uuid': '4b04d281-f8e6-4da0-bbd1-76ede2185327'}, {'user_uuid': '4d2eb940-d4ea-4f51-abc6-df8186565449'}, {'user_uuid': '4f0a9643-9dc1-4e3b-8591-d85dca0e9c3e'}, {'user_uuid': '4f9e97a3-48f2-4ded-a0b0-e47ace13c173'}, {'user_uuid': '53d04072-60a2-4015-9d8d-08983919113b'},  {'user_uuid': '54046b0b-5150-4095-993d-1840e679474e'}, {'user_uuid': '56a9cc4a-ca89-4375-90de-1b828b5ef562'}, {'user_uuid': '5ca6fa37-38a4-4b89-a847-014acab7e3fb'}, {'user_uuid': '655be69b-6a3c-41dd-b557-4fc840d65de9'}, {'user_uuid': '657579b0-bd06-4980-a075-a30cb7d97765'}, {'user_uuid': '685f8eef-b2d2-4707-990c-b7702769957b'}, {'user_uuid': '697364c3-967f-448c-8f64-aeeee487d123'}, {'user_uuid': '7315d949-83ae-4bb4-9ec8-0251753edd0f'},  {'user_uuid': '752730d0-e752-4a13-b3be-6fc3d32220df'}, {'user_uuid': '754d7092-eca3-4d41-8b18-33875727da17'}, {'user_uuid': '7a332b96-1d6d-40ee-a05d-eb90c2ce9f02'}, {'user_uuid': '8088bc4d-933d-4b83-b046-1972c95d841a'}, {'user_uuid': '836a90cc-57ad-4b96-aa7e-3adac0af1f93'}, {'user_uuid': '85ba0331-febd-4e80-8187-5a031f487ffe'}, {'user_uuid': '8eea4577-e15f-4a08-925f-b619d13159ca'}, {'user_uuid': '9209aee5-71c7-4b84-a071-e7fa1737d365'}, {'user_uuid': '93d3be4b-5ccf-4ed6-9947-6d87298e9cd2'}, {'user_uuid': '944d808b-fe5f-4415-9269-fabc09ed9fe1'}, {'user_uuid': '98e1158a-46ba-42ae-a45e-ff177011fb23'}, {'user_uuid': '9db9311d-5ba2-465f-8ef7-373a2407b653'}, {'user_uuid': '9e6b74e9-8c0f-4778-b3fe-feaa7459c2c8'}, {'user_uuid': 'a413d156-5647-4ff7-956c-5e63543263da'}, {'user_uuid': 'a4f1d5e3-f47b-476f-919a-b1a854c4d06f'}, {'user_uuid': 'a50077a5-c9d9-4b17-b4e1-743ab998059c'}, {'user_uuid': 'a7a06ac3-e3f2-464b-aa13-5600cf13950c'}, {'user_uuid': 'ae442a94-e24c-43d0-a1ae-ec95a6e73be9'}, {'user_uuid': 'af20b081-019d-4f9e-8845-20b88af73781'}, {'user_uuid': 'af7fc7fb-8a88-4bc7-be15-064e21ab7959'}, {'user_uuid': 'b19869a8-952e-4a70-a95a-d804b898f0eb'}, {'user_uuid': 'b2c51218-264d-4796-b4cf-cc4217b3a262'}, {'user_uuid': 'b5fa9c61-7533-4b4a-a573-59212905d85a'}, {'user_uuid': 'b8cc5bb2-3bcb-4bd5-b606-d435492ee3f4'}, {'user_uuid': 'ba3e6046-f5d4-4c7b-8d86-16d6e0c4b6ba'}, {'user_uuid': 'bc1df051-eda1-4f8c-b86f-f964f676fc56'}, {'user_uuid': 'bc8c045d-fd12-406b-a080-f41380dd9a23'}, {'user_uuid': 'c8d58e16-73d8-4fdd-baa4-24682c594bb6'}, {'user_uuid': 'c8f51593-a716-42c4-bdb3-42f6d34b0e72'}, {'user_uuid': 'd0a0b64e-9b1d-4313-a6a7-c9f053368c93'}, {'user_uuid': 'd67ab23f-9191-4d00-83e5-fd751c9b04f2'}, {'user_uuid': 'd7a89032-37d0-46b6-bcf2-b3c4c3fd32a7'}, {'user_uuid': 'd8aed8f3-2837-462e-950e-dc19eef282a1'}, {'user_uuid': 'd9c29e90-80cb-47d7-bf16-5def20e8367f'}, {'user_uuid': 'daf554df-b15f-491b-87c6-b22ff81551eb'}, {'user_uuid': 'db99ca1a-7637-44db-945f-c3d400b03733'}, {'user_uuid': 'dbca07d2-f9fb-42ca-a181-d065c065bab6'},{'user_uuid': 'dd8b5214-8048-4781-a70f-8cea3de2490c'}, {'user_uuid': 'e18a1be9-4e54-4d35-b2c2-5bb4edae8654'},    {'user_uuid': 'e63a3bf6-5c49-4a5b-8372-8385da27a831'}, {'user_uuid': 'e7354493-fe36-4613-8336-7db2bfb0eb2e'}, {'user_uuid': 'ea3adf9f-bdb3-422d-b096-058dc1080bf6'}, {'user_uuid': 'ec1a2df3-27f4-4379-b468-37e8d213a6bc'}, {'user_uuid': 'eda06ba4-71e4-46e0-b8a9-9aaae5ab1cb8'}, {'user_uuid': 'f0e08ca0-6531-4a9a-97d2-5ba5ee0f3447'}, {'user_uuid': 'f1d21905-38e3-4102-b8a3-46d83931736b'}, {'user_uuid': 'f1e2038f-9c33-494d-bf5e-e3616544b716'}, {'user_uuid': 'f3afb3cb-a835-4be4-a302-bf2222307669'}, {'user_uuid': 'f876f02e-ab6a-4bbb-8dc2-7bbdeed73d9a'}, {'user_uuid': 'fb135c89-aca4-4136-acdf-94fae71e513a'}, {'user_uuid': 'fda78e97-681b-410c-928b-9df3b2a8ae34'}, {'user_uuid': 'fde86918-bfe0-4254-b76c-8945b53b456d'}]
    for user_uuid in user_list:
        user_uuid=user_uuid['user_uuid']
        up_report_to_test(user_uuid,test_db,mongo_client,buz_mysql,tset_mysql)
        my_url=make_report(buz_class_id=331096, course_code='JZX2.0.2.5', subject_show_id='1',user_uuid_list=[user_uuid],user_number=1, classes_checkin_number=1)
        print(my_url)
        time.sleep(5)
        print(user_uuid)









        # json_url=str(my_url['classReportList'][1]['reportUrl']).replace('http://test.kuaikuaikeji.com/kas/movereport/?i=','http://192.168.41.41/KKNewReport/PadGetUUIDUserReportV3?i=')

        #        json_data=client.get(url=json_url ).json()
     #   json_list=[]
      #  for x in    json_data['strengthAvgs']['strengthHundred']:
      #      json_list.append(x['totalStrength'])
      #  print(json_list)
     #A   with open('json.txt', 'a') as f:
     #       f.write(str(json_list)+',')