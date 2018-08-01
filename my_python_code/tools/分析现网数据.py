import matplotlib.pyplot as plt
import requests
from my_python_code.mysql.Basic_information import *
from my_python_code.mysql.ORM_of_mysql import *

def report_data(x):
     url = "http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/"+x+".txt"
     print(url)
     user_class_data = requests.get(url).content
     user_class_data=eval(user_class_data)
     scopeX_all_user=[]
     heartbeats_all_user=[]
     my_bind_list=[]
     for x in user_class_data['classDataList']:
         try:
             print(x['userUuid'],x['padId'],x['bondDeviceId'])
             heartbeats = ''
             scopeX = ''
             scopeY = ''
             scopeZ = ''
             for y in x['unitDataList']:
                if  'scopeX' not in y:
                    continue
                if y['scopeX']=='':
                    pass
                else:
                     print(len(eval('['+str(y['heartbeats'])+']')))
                     heartbeats=heartbeats+y['heartbeats']+','
                     scopeX=scopeX+y['scopeX']+','
                     scopeY=scopeY+y['scopeY']+','
                     scopeZ=scopeZ+y['scopeZ']+','
             heartbeats =  eval('['+heartbeats+']')
             scopeX = eval('['+scopeX+']')
             scopeY = eval('['+scopeY+']')
             scopeZ = eval('['+scopeZ+']')
             scopeX_all_user.append(scopeX)
             heartbeats_all_user.append(heartbeats)
             print('平均',sum(heartbeats)/len(heartbeats))
             print('心率长度：'+str(len(heartbeats)))
             print('scopeX长度:'+str(len(scopeX)))
             print('scopeY长度:'+str(len(scopeY)))
             print('scopeZ长度:'+str(len(scopeZ)))

             try:
                 plt.figure(x['userUuid'] + '臂带  ' + x['bondDeviceId'])
                 my_bind_list.append( x['bondDeviceId'])
             except:
                 plt.figure('没有臂带')
                 my_bind_list.append( '没有臂带')
             plt.ylim((0, 60000))
             plt.ylabel('Scaled values', fontsize=16)
             plt.subplot(411)
             plt.plot(range(len(scopeX)),scopeX)
             plt.ylim((0, 60000))
             plt.subplot(412)
             plt.plot(range(len(scopeY)),scopeY)
             plt.ylim((0, 60000))
             plt.subplot(413)
             plt.plot(range(len(scopeZ)),scopeZ)
             plt.ylim((0, 60000))
             plt.subplot(414)
             plt.ylim((0, 300))
             plt.plot(range(len(heartbeats)),heartbeats)
         except:
             pass
     print(my_bind_list)
     plt.show()
     i=1
     for k in heartbeats_all_user:
         plt.ylim((0, 300))
         staer=str(len(heartbeats_all_user))+str(1)+str(i)
         plt.subplot(len(heartbeats_all_user),1,i)
         plt.plot(range(len(k)), k)
         i=i+1
   #  plt.show()
     i = 1
     for k in scopeX_all_user:
        plt.ylabel(my_bind_list[i-1])
        plt.subplot(len(scopeX_all_user), 1, i)
        plt.plot(range(len(k)), k)
        i = i + 1
     plt.show()


if __name__=='__main__':
    my_db = orm_to_mysql(my_sql_link_buz_pool())
   # my_db = orm_to_mysql(my_sql_link_test())
    data_uuid=my_db.table('user_class_data').select('data_uuid',class_id=320626).one()
    if data_uuid:
        report_data(data_uuid['data_uuid'])
    else:
        print('没有数据')