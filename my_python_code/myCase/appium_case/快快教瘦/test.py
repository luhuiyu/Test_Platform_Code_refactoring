from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import *
from my_python_code.basic_configuration.configuration_file import *
from my_python_code.mysql.simple_mysql import *
test_db=simple_mysql(my_sql_link_test_pool())
buz_db=simple_mysql(my_sql_link_buz_pool())
for x in uuid_idct:
    for y in uuid_idct[x]:
        test_db.TABLE('user_daily_weight').DELETE().WHERE(user_uuid=y).EXECUTE_ALL()
        A=buz_db.TABLE('user_daily_weight').SELECT().WHERE(
            user_uuid='a21573c6-d4dd-466b-8fee-af1b2095cf6f'
                                                       ).AND(id__LT=1103345,).EXECUTE_ALL()
        for z in A:
            z['user_uuid']=y
            z['id']='None'
            test_db.TABLE('user_daily_weight').INSERT(z).EXECUTE_ALL()