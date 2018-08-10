from my_python_code.mysql.simple_mysql import *
from  my_python_code.mysql.Basic_information import *

import records

example = simple_mysql(my_sql_link_buz_pool())
new_user_data=example.EXECUTE_ALL('SELECT user_report.user_uuid,user_report.score,user_report.train_calorie,user.sex FROM user_report,user WHERE user_report.create_time>\'2018-05-07\' AND user_report.user_uuid=user.uuid')
results = records.RecordCollection(iter(new_user_data))
with open('demo3.xlsx', 'wb') as f:
    f.write(results.export('xlsx'))



