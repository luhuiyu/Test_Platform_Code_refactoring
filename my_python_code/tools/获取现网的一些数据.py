from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_buz
import time

my_db=orm_to_mysql(my_sql_link_buz())
all_gym_data=my_db.table('gym').select('id','name','start_date',status=1,start_date__GT='2015-12-10').all()
for gym_data in all_gym_data:
    timestamp = time.mktime(time.strptime(gym_data['start_date'], "%Y-%m-%d"))
    endtime = time.strftime('%Y-%m-%d', time.localtime(timestamp + 30 * 24 * 3600))
    user_uuid_list=my_db.table('orders').select('user_uuid',create_time__GT=gym_data['start_date'],create_time__LT=endtime,deal_price__GT=100,status=1,gym_id=gym_data['id'],GROUP_BY='user_uuid').all()
    for user_uuid in user_uuid_list:
        user_uuid = user_uuid['user_uuid']
        user_code = my_db.table('user').select('user_code', uuid=user_uuid).one()['user_code']
        fat_rate_list = my_db.table('user_daily_weight').select('fat_rate', 'weight', fat_rate__GT=0,user_uuid=user_uuid).all()
        all_str =  str(gym_data['name'])+ ','+str(user_code)+ ','
        if fat_rate_list:
            all_str = all_str + str(fat_rate_list[0]['fat_rate']) + ','
            all_str = all_str + str(fat_rate_list[-1]['fat_rate']) + ','
            all_str = all_str + str(fat_rate_list[0]['weight']) + ','
            all_str = all_str + str(fat_rate_list[-1]['weight']) + ','
        all_str = all_str + '\r'
        f = open('test.txt', 'a')
        f.write(str(all_str))
