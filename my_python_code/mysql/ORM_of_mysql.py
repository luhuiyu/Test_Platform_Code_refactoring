import  pymysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
import re

def count_sub(s):
    return len(re.findall(r',',s))

class orm_to_mysql():
   def __init__(self, mysql_link=my_sql_link()):
        self.link=mysql_link
        self.db = self.link.db
        self.cursor=self.link.cursor_dict
        self.my_table='111'
   def  table(self,*args):
           table_list=[]
           for x in args:
               table_list.append(x)
           self.my_table = str(table_list)[1:-1].replace('\'', '')
           return self

   def order_by(self, *args):
       column = ' GROUP BY  '
       condition=''
       for x in args:
           condition=condition+ ', '+ str(x)
       self.my_sql_statement = str(self.my_sql_statement) + column + condition[1:]
       return self
   def all(self):
     #  print(str(self.my_sql_statement))
       self.cursor.execute(str(self.my_sql_statement))
       self.db.commit()
       return self.cursor.fetchall()
   def limit(self,*args):
       column = 'limit '
       if len(args) == 1:
           self.my_sql_statement = str(self.my_sql_statement) + column +  str(args[0])
       else:
           self.my_sql_statement = str(self.my_sql_statement) + column + str(args[0])+','+ str(args[1])
   def one(self):
       self.cursor.execute(str(self.my_sql_statement))
       self.db.commit()
       return self.cursor.fetchone()

   def select(self, *args, **kw):
       column_conditions = ''
       for x in args:
           column_conditions = column_conditions + str(x) + ','
       search_criteria = ''
       for x in kw.items():
           if str(x[0])[-6:] == "__LIKE":
               column = str(x[0])[:-6]
               condition = '\'%' + str(x[1]) + '%\''
               operator = ' LIKE '
           elif str(x[0])[-4:] == "__GT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' > '
           elif str(x[0])[-4:] == "__LT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' < '
          # elif '__' in str(x[0]):
          #     raise NameError
           elif  str(x[0])=='GROUP_BY':
               search_criteria=search_criteria[:-4]
               column = 'GROUP BY'
               condition =    str(x[1])
               operator = ' '
           else:
               column = str(x[0])
               condition = '\'' + str(x[1]) + '\''
               operator = ' =  '
           if  '__' in str(x[0]):
               column=column.replace('__', '.')
           if count_sub(self.my_table)>1 and column in condition :
               if '.'in condition:
                   condition=condition[1:-1]
           sc = column + operator + condition + ' AND '
           search_criteria = search_criteria + sc
       if search_criteria:
           search_criteria = ' where ' + search_criteria[:-4]
       else:
           search_criteria = ''
       if args:
           sql = "select  " + column_conditions[:-1] + "  from  " + str(self.my_table) + search_criteria
       else:
           sql = "select  * " + "  from  " + str(self.my_table) + search_criteria
       self.my_sql_statement=str(sql)
       return self

   def insert(self, *args, **kw):
       column = r''
       condition = r''
       for x in kw.items():
           column = column + str(x[0]) + ','
           condition = condition + '\'' + str(x[1]) + '\','
       sql = 'INSERT IGNORE INTO ' + str(self.my_table) + ' (' + column[:-1] + ') VALUES (' + condition[:-1] + ')'
     #  print(sql)
       self.cursor.execute(str(sql))
       self.db.commit()
       return self

   def delete(self, *args, **kw):
       search_criteria = ''
       for x in kw.items():
           if str(x[0])[-6:] == "__LIKE":
               column = str(x[0])[:-6]
               condition = '\'%' + str(x[1]) + '%\''
               operator = ' LIKE '
           elif str(x[0])[-4:] == "__GT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' > '
           elif str(x[0])[-4:] == "__LT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' < '
           elif '__' in str(x[0]):
               raise NameError
           else:
               column = str(x[0])
               condition = '\'' + str(x[1]) + '\''
               operator = ' =  '

           sc = column + operator + condition + ' AND '
           search_criteria = search_criteria + sc
       sql = 'DELETE FROM  ' + str(self.my_table) + '  WHERE  ' + search_criteria[:-4]
       self.cursor.execute(str(sql))
       self.db.commit()
       return self

   def updata(self, *args, **kw):
       #        self.my_db.table('web_platform_phone').updata({'phone_code':self.fictitious_armband_pid},id=100)
       updata_data = ''
       search_criteria = ''
       updata_data_dict = args[0]
       for x in updata_data_dict.items():
           column = str(x[0])
           condition = '\'' + str(x[1]) + '\''
           operator = ' =  '
           sc = column + operator + condition + ','
           updata_data = updata_data + sc
       for x in kw.items():
           if str(x[0])[-6:] == "__LIKE":
               column = str(x[0])[:-6]
               condition = '\'%' + str(x[1]) + '%\''
               operator = ' LIKE '
           elif str(x[0])[-4:] == "__GT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' > '
           elif str(x[0])[-4:] == "__LT":
               column = str(x[0])[:-4]
               condition = '\'' + str(x[1]) + '\''
               operator = ' < '
           elif '__' in str(x[0]):
               raise NameError
           else:
               column = str(x[0])
               condition = '\'' + str(x[1]) + '\''
               operator = ' =  '
           sc = column + operator + condition + ' AND '
           search_criteria = search_criteria + sc

       sql = 'UPDATE ' + str(self.my_table) + ' SET ' + updata_data[:-1] + ' WHERE ' + search_criteria[:-4]
   #    print(sql)
       self.cursor.execute(str(sql))
       self.db.commit()
       return self

   def close(self):
       self.db.close()

   def sql(self, sql):
       self.cursor.execute(str(sql))
       self.db.commit()
       return self

if __name__ == '__main__':
    a=orm_to_mysql()
    #print(a.table('web_platform_my_case_of_text','web_platform_my_case_of_api').select('web_platform_my_case_of_api.api_name',web_platform_my_case_of_text__project_name='快快教瘦',web_platform_my_case_of_text__module_name='web_platform_my_case_of_api.module_name').all())
    print(a.table('web_platform_comparison_library').select('send_json',api_name='PadGetCoachClassListV2').order_by('id','status_code').all())