

class simple_mysql():
    """
    用于简单的拼接mysql语句的
    适用于单个表的删增改查

    """

    def __init__(self):
        self.my_table = ''  #表的名称
        self.my_column_name='' #列名　
        self.my_type=''  # sql操作类型  有  select  updata
        self.my_sql_statement='' #完整的sql语句

    def my_print(self):
        print(self.my_sql_statement)
        print(self.my_table)
        print(self.my_column_name)
    def table(self, *args):
        table_list = []
        for x in args:
            table_list.append(x)
        self.my_table = str(table_list)[1:-1].replace('\'', '')
        return self
    def order_by(self, *args):
        column = ' GROUP BY  '
        condition = ''
        for x in args:
            condition = condition + ', ' + str(x)
        self.my_sql_statement = str(self.my_sql_statement) + column + condition[1:]
        return self
    def select(self,*args,isdistinct=True,**kwargs):
        column_conditions = ''
        for x in args:
            column_conditions = column_conditions + str(x) + ','
        search_criteria = ''
        for y in kwargs:
            if  type(kwargs[y]) is list:
                for z in kwargs[y]:
                    search_criteria = search_criteria + str(y) + '.' + str(z) + ','
            else:
                search_criteria = search_criteria + str(y) + '.' + str(kwargs[y]) + ','
        self.my_column_name=column_conditions+search_criteria
        if isdistinct:
            self.my_type = ' select  distinct   '
        else:
            self.my_type = ' select  '
        if self.my_column_name:
            self.my_sql_statement=  self.my_type +   self.my_column_name + ' from   '+ self.my_table
        return self
    def where(self,*args,**kwargs):

        self.my_sql_statement = self.my_sql_statement+' where  '
        return self
    def subconditions(self,symbol=' = ',relation=' AND ' ,**kwargs ):
        for x in  kwargs.items():
            clause= '  '+str(x[0])+symbol+str(x[1])+relation
            self.my_sql_statement=self.my_sql_statement+clause
        return self









if __name__ == '__main__':
    a=simple_mysql()
  #  a.table('user','classes').select('user_uuid',user='wwww',classes='222222',AA=[22,33,55,1,77,8]).where(a='<__44444__OR',b='222',c='<=__ee').order_by()
     #SELECT * FROM user_classes_checkin WHERE classes_id=56634
   # a.table('user','classes').select(11,user='ee',classes='ww',AA=[22,33,55,1,77,8]).where()
 #   a.where(a='<__44444__OR',b='222',c='<=__ee',d=('<','ddd','or'))
    a.table('user').select('user_uuid').where().subconditions(id=111,cd=1234,symbol='<').subconditions(ss=22)
    print(a.my_sql_statement)
