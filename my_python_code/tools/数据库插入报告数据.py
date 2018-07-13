
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
import uuid

orm = orm_to_mysql(my_sql_link_test())

for x in range(99):
    orm.table('user_report').insert(subject_show_id=3,uuid=uuid.uuid4(),user_uuid= '20d7134c-d302-4187-bbf8-3e392c92a3d3',ranking=1,version=3,classes_id=249726,score=88,musle_rate='none',composite_rate='test',coordinate='test',report_data='test')

orm.close()


