import sys
from multiprocessing import Queue
sys.path.append('F:/Test_Platform')
from my_python_code.mysql.Singleton  import  Singleton,SingletonType
import socket,time,os
from my_python_code.tools.虚拟臂带 import fictitious_bind
from my_python_code.mysql.Basic_information import my_sql_link
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class my_fictitious_armband(Singleton):
    def __init__(self):
        self.my_db=orm_to_mysql(my_sql_link())
        self.fictitious_armband_pid = self.my_db.table('web_platform_phone').select(id='100').one()['phone_code']

    def concurrency_armband(self, total=50,time_delay=1):
        self.kill()
        time_delay = float(time_delay)
        if int(self.fictitious_armband_pid )!= 0:
            os.popen('taskkill.exe /pid:' + str(self.fictitious_armband_pid)+'   /F')
        self.fictitious_armband_pid = os.getpid()
        self.my_db.table('web_platform_phone').updata({'phone_code':self.fictitious_armband_pid},id=100)
        fictitious_bind(sign=True,total=total,time_delay=time_delay)

    def sequential_armband(self):
        self.kill()
        if int(self.fictitious_armband_pid )!= 0:
            os.popen('taskkill.exe /pid:' + str(self.fictitious_armband_pid)+'   /F')
        self.fictitious_armband_pid = os.getpid()
        self.my_db.table('web_platform_phone').updata({'phone_code':self.fictitious_armband_pid},id=100)
        #print(self.fictitious_armband_pid)
        fictitious_bind(sign=False,total=45)
    def kill(self):
        if int(self.fictitious_armband_pid) != 0:
            os.popen('taskkill.exe /pid:' + str(self.fictitious_armband_pid)+'   /F')
            self.my_db.table('web_platform_phone').updata({'phone_code':0},id=100)
            pid_list = eval(self.my_db.table('web_platform_phone').select(id='101').one()['phone_code'])
            for x in  pid_list:
                os.popen('taskkill.exe /pid:' + str(x) + '   /F')

def start_app():

        a=my_fictitious_armband()
        if int(sys.argv[1]) == 1 : #虚拟臂带
            a.sequential_armband()
        elif  int(sys.argv[1]) == 2 : #虚拟臂带，提前准备n个
            a.concurrency_armband(total=sys.argv[2],time_delay = sys.argv[3])

        elif  int(sys.argv[1]) == 9 : #杀进程
            a.kill()

if __name__ == '__main__':

        start_app()



