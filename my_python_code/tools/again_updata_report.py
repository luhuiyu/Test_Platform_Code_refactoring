from my_python_code.myCase.api_case.interface.login_args import headers
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link_buz
import hashlib
import base64
import gzip
import requests

def up_report_data(coach_phone,password,class_id,sign=False):
    client = requests.session()
    coach_phone=str(coach_phone)
    password=str(password)
    if sign:
        my_db = orm_to_mysql(my_sql_link_buz())
        url_main = 'http://c.kuaikuaikeji.com/kcas/'
    else:
        my_db = orm_to_mysql(my_sql_link_test())
        url_main = 'http://test.kuaikuaikeji.com/kcas/'
    class_data_uuid=my_db.table('user_class_data').select('data_uuid',class_id=class_id).one()
    data=client.get(url='http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/'+str(class_data_uuid['data_uuid'])+'.txt')
    headers1 = headers(client, user_name=coach_phone, password=password, url_login=url_main + "PadCoachLoginV2")
    print('登录状态' + str(client.post(url=url_main + 'PadCoachLoginV2', headers=headers1).status_code))
    print('报告上传状态' + str(client.post(url=url_main + 'PadUploadAllClassDataV2',data=data).status_code))






if __name__ == '__main__':
    up_report_data(class_id=59030,coach_phone=13691421359,password=123456,sign=False)