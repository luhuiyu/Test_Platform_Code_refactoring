uuid_idct=[


]

from my_python_code.mysql.Basic_information import my_sql_link_test
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql

my_db = orm_to_mysql(my_sql_link_test())

for x in uuid_idct:

    print( my_db.table('user').select('name',uuid=x).one(),x)