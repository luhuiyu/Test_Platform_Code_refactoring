

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
    def _my_print(self):
        print(self.my_sql_statement)
        print(self.my_table)
        print(self.my_column_name)
    def TABLE(self, *args):
        table_list = []
        for x in args:
            table_list.append(x)
        self.my_table = str(table_list)[1:-1].replace('\'', '')
        return self
    def ORDER_BY(self, *args):
        column = ' GROUP BY  '
        condition = ''
        for x in args:
            condition = condition + ', ' + str(x)
        self.my_sql_statement = str(self.my_sql_statement) + column + condition[1:]
        return self
    def SELECT(self,*args,isdistinct=False,**kwargs):

        if len(args) > 0 :
            column_conditions = ''
        else:
            column_conditions = ' * '
        for x in args:
            column_conditions = column_conditions + str(x) + ','
        self.my_column_name=column_conditions[:-1]
        if isdistinct:
            if column_conditions != ' * ':
                self.my_type = ' select  distinct   '
            else:
                self.my_type = ' select  '
        else:
            self.my_type = ' select  '
        if self.my_column_name:
            self.my_sql_statement=  self.my_type +   self.my_column_name + ' from   '+ self.my_table
        return self
    def WHERE(self,**kwargs):
        sc=''
        for x in kwargs.items():
            key = x[0]
            relationship = ' AND '
            if str(key)[-6:] == "__LIKE":
                column = str(key)[:-6]
                condition = '\'%' + str(x[1]) + '%\''
                operator = ' LIKE '
            elif str(key)[-4:] == "__GT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' > '
            elif str(key)[-4:] == "__LT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' < '
            else:
                column = str(key)
                condition = '\'' + str(x[1]) + '\''
                operator = ' =  '
            sc = column + operator + condition
        self.my_sql_statement = self.my_sql_statement+' where ' + sc
        return self
    def OR(self,**kwargs):
        search_criteria = ''
        for x in kwargs.items():
            key = x[0]
            relationship = ' AND '
            if str(key)[-6:] == "__LIKE":
                column = str(key)[:-6]
                condition = '\'%' + str(x[1]) + '%\''
                operator = ' LIKE '
            elif str(key)[-4:] == "__GT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' > '
            elif str(key)[-4:] == "__LT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' < '
            else:
                column = str(key)
                condition = '\'' + str(x[1]) + '\''
                operator = ' =  '
            sc = '  OR  ' + column + operator + condition
            search_criteria = search_criteria + sc
        if self.my_sql_statement[-6:]=='where ':
            self.my_sql_statement = self.my_sql_statement + search_criteria[4:]
        else:
            self.my_sql_statement = self.my_sql_statement+   search_criteria
        return self
    def AND(self,**kwargs):
        search_criteria = ''
        for x in kwargs.items():
            key = x[0]
            relationship = ' AND '
            if str(key)[-6:] == "__LIKE":
                column = str(key)[:-6]
                condition = '\'%' + str(x[1]) + '%\''
                operator = ' LIKE '
            elif str(key)[-4:] == "__GT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' > '
            elif str(key)[-4:] == "__LT":
                column = str(key)[:-4]
                condition = '\'' + str(x[1]) + '\''
                operator = ' < '
            else:
                column = str(key)
                condition = '\'' + str(x[1]) + '\''
                operator = ' =  '
            sc = ' AND ' + column + operator + condition
            search_criteria = search_criteria + sc
        if self.my_sql_statement[-6:]=='where ':
            self.my_sql_statement = self.my_sql_statement + search_criteria[4:]
        else:
            self.my_sql_statement = self.my_sql_statement+   search_criteria
        return self
    def INSERT(self, *args,**kw):
        column = r''
        condition = r''
        for x in kw.items():
            column = column + str(x[0]) + ','
            condition = condition + '\'' + str(x[1]) + '\','
        for y in range(0,len(args)):
            for x in args[y].items():
                if str(x[1]) == 'None':
                    pass
                else:
                    column = column + str(x[0]) + ','
                    condition = condition + '\'' + str(x[1]) + '\','
        self.my_sql_statement = 'INSERT IGNORE INTO ' + str(self.my_table) + ' (' + column[:-1] + ') VALUES (' + condition[:-1] + ')'
        return self
    def INSERT_IGNORE(self, *args,**kw):
        column = r''
        condition = r''
        for x in kw.items():
            column = column + str(x[0]) + ','
            condition = condition + '\'' + str(x[1]) + '\','
        for y in range(0,len(args)):
            for x in args[y].items():
                if str(x[1]) == 'None':
                    pass
                else:
                    column = column + str(x[0]) + ','
                    condition = condition + '\'' + str(x[1]) + '\','
        self.my_sql_statement = 'INSERT IGNORE INTO ' + str(self.my_table) + ' (' + column[:-1] + ') VALUES (' + condition[:-1] + ')'
        return self
    def UPDATA(self, *args, **kw):
        '''
        UPDATE 表名称 SET 列名称 = 新值
        :param args:
        :param kw:
        :return:
        '''
        updata_data = ''
        for y in range(0, len(args)):
            for x in args[y].items():
                column = str(x[0])
                condition = '\'' + str(x[1]) + '\''
                operator = ' =  '
                sc = column + operator + condition + ','
                updata_data = updata_data + sc
        for x in kw.items():
            column = str(x[0])
            condition = '\'' + str(x[1]) + '\''
            operator = ' =  '
            sc = column + operator + condition + ','
            updata_data = updata_data + sc
        self.my_sql_statement='UPDATE ' + str(self.my_table) + ' SET ' + updata_data[:-1]
        return self
    def DELETE(self, *args, **kw):
        pass
if __name__ == '__main__':
    a=simple_mysql()
     #SELECT * FROM user_classes_checkin WHERE classes_id=56634
    a.TABLE('AAAA').INSERT(aa=33)
    a.TABLE('AAAA').UPDATA({'11':'11'},{'22':'22'},AA='AA').WHERE().AND(id=33).OR(id=4)
    print(a.my_sql_statement)
