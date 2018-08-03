# -*-coding: utf-8-*-

import logging
from my_python_code.mysql.Basic_information import *
logging.basicConfig(level=logging.INFO)

class simple_mysql():
    """
    用于简单的拼接mysql语句的
    适用于单个表的删增改查

    """
    def __init__(self,mysql_link):
        self.my_table = ''  #表的名称
        self.my_column_name='' #列名　
        self.my_type=''  # sql操作类型  有  select  updata
        self.link = mysql_link
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
    def LIMIT(self, *args,**kw):
        column = ' limit '
        if len(args) == 1:
            self.my_sql_statement = str(self.my_sql_statement) + column + str(args[0])
        else:
            self.my_sql_statement = str(self.my_sql_statement) + column + str(args[0]) + ',' + str(args[1])
        return self
    def IN (self,*args,**kwargs):
        '''
        SELECT column_name(s)
        FROM table_name
        WHERE column_name IN (value1,value2,...)
        :param args:
        :param kw:
        :return:
        '''
        sc = ''
        for x in kwargs.items():
            key = x[0]
            operator = ' IN '
            column = str(key)
            condition =  str(x[1])
            sc = column + operator + condition
        if self.my_sql_statement[-6:]=='WHERE ':
            self.my_sql_statement = self.my_sql_statement+   sc
        else:
            self.my_sql_statement = self.my_sql_statement + ' AND ' + sc
    def SELECT(self,*args,isdistinct=False,**kwargs):
        '''
        select  phone_code from   web_platform_phone WHERE id =  '3'
        TABLE('web_platform_phone').SELECT('phone_code').WHERE(id=3).EXECUTE_ALL()
        select   * from   web_platform_phone WHERE id =  '3'
        TABLE('web_platform_phone').SELECT().WHERE(id=3).EXECUTE_ALL()
        :param args:
        :param isdistinct:
        :param kwargs:
        :return:
        '''
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
        self.my_sql_statement = self.my_sql_statement+' WHERE ' + sc
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
        if self.my_sql_statement[-6:]=='WHERE ':
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
        if self.my_sql_statement[-6:]=='WHERE ':
            self.my_sql_statement = self.my_sql_statement + search_criteria[4:]
        else:
            self.my_sql_statement = self.my_sql_statement+   search_criteria
        return self
    def INSERT(self, *args,**kw):
        '''
        原sql ：
            REPLACE INTO web_platform_my_img (id,img_data,uuid,remarks,create_time) VALUES ('100','11eeeeee111','adadaAFAFA','1','2010-02-22 10:00:00')
        对应的：
            TABLE('web_platform_my_img').INSERT_IGNORE(id=100,img_data='11111',uuid='adadaAFAFA',remarks=1,create_time='2010-02-22 00:00:00').EXECUTE_ONE()
            TABLE('web_platform_my_img').REPLACE_INTO( {'id':101,'img_data':'11eeeeee111','uuid':'2222ada','remarks':2,'create_time':'2010-02-22 10:00:00'}).EXECUTE_ONE()
        :param args:
        :param kw:
        :return:
        '''
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
    def REPLACE_INTO(self, *args, **kw):
        column = r''
        condition = r''
        for x in kw.items():
            column = column + str(x[0]) + ','
            condition = condition + '\'' + str(x[1]) + '\','
        for y in range(0, len(args)):
            for x in args[y].items():
                if str(x[1]) == 'None':
                    pass
                else:
                    column = column + str(x[0]) + ','
                    condition = condition + '\'' + str(x[1]) + '\','
        self.my_sql_statement = ' REPLACE INTO ' + str(self.my_table) + ' (' + column[:-1] + ') VALUES (' + condition[:-1] + ')'
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
        '''
        DELETE FROM 表名称 WHERE 列名称 = 值
        :param args:
        :param kw:
        :return:
        '''
        self.my_sql_statement='DELETE FROM  ' + str(self.my_table )
        return self
    def EXECUTE_ALL(self,my_sql_statement=False):
        if my_sql_statement:
            with self.link.cursor() as cursor:
                logging.info('simple_mysql :' + str(my_sql_statement))
                cursor.execute(str(my_sql_statement))
                return cursor.fetchall()
        else:
            with self.link.cursor() as cursor:
                logging.info('simple_mysql :'+str(self.my_sql_statement))
                cursor.execute(str(self.my_sql_statement))
                return cursor.fetchall()
    def EXECUTE_ONE(self,my_sql_statement=False):
        if my_sql_statement:
            with self.link.cursor() as cursor:
                logging.info('simple_mysql :' + str(my_sql_statement))
                cursor.execute(str(my_sql_statement))
                return cursor.fetchone()
        else:
            with self.link.cursor() as cursor:
                logging.info('simple_mysql :'+ str(self.my_sql_statement))
                cursor.execute(str(self.my_sql_statement))
                return cursor.fetchone()

if __name__ == '__main__':
    a=simple_mysql(my_sql_link_pool())
   # A=a.TABLE('web_platform_my_img').REPLACE_INTO(id=100,img_data='11eeeeee111',uuid='adadaAFAFA',remarks=1,create_time='2010-02-22 10:00:00').EXECUTE_ONE()
    #A=a.TABLE('web_platform_my_img').REPLACE_INTO( {'id':101,'img_data':'11eeeeee111','uuid':'2222ada','remarks':2,'create_time':'2010-02-22 10:00:00'}).EXECUTE_ONE()
   # a.TABLE('web_platform_phone').UPDATA(id=10,phone_code='15900900000').WHERE(id=100).EXECUTE_ALL()
   # a.TABLE('web_platform_phone').UPDATA({'id':10,'phone_code':'1560090000'}).WHERE(id=100).EXECUTE_ALL()
 #   a.TABLE('web_platform_phone').UPDATA({'phone_code':1560090000},id=10).WHERE(id=100).EXECUTE_ALL()
    a.TABLE('web_platform_phone').DELETE().WHERE(id__GT=150,phoe__LT=100,name__LIKE='北京').EXECUTE_ALL()