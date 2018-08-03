import socket,time,os
import random
from multiprocessing import Process
from multiprocessing import Queue
from my_python_code.mysql.Basic_information import my_sql_link_pool
from my_python_code.mysql.ORM_of_mysql import orm_to_mysql
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
user_coad=[]
time_delay1=1
def get_UDP_data(UDP_data,my_pid):#用于接收pad发过来的数据
    my_pid.put(os.getpid())
    get_ueserinfo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    get_ueserinfo.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    get_ueserinfo.setblocking(1)
    get_ueserinfo.bind(('', 8001))
    while 1:
        user_id, addr = get_ueserinfo.recvfrom(1024)
        UDP_data.put(user_id)
        A=list(user_id)
       # if A[0]==34:
        #    print(A)
def read_UDP_data(UDP_data,user_cord,bind_list,bind_list_1,my_pid):#分析发送过来的数据
    my_pid.put(os.getpid())
    user_cord_list=[]
    bind_id_list=[]
    bing_id_2=[]
    id=0
    while 1:
        user_id=list(UDP_data.get())
        if user_id[0] == 36:
            if list(user_id)[2:6] not in user_cord_list:
                    user_cord_list.append(list(user_id)[2:6])
                    bind_id_list.append(id)
                    id=id+1
                    bing_id_2.append(id)
                    user_cord.put(user_cord_list)
                    bind_list.put(bind_id_list)
                    bind_list_1.put(bing_id_2)
        elif user_id[0]==37:
            if list(user_id)[2:6]  in user_cord_list:
                b=list(user_id)[2:6]
                index=user_cord_list.index(b)
                user_cord_list.remove(b)
                bind_id_list.pop(index)
                user_cord.put(user_cord_list)
                bind_list.put(bind_id_list)
        else:
            if user_id[0] != 34 and  user_id[0] != 50:
                    print(user_id)
       # print(user_cord_list)
        #print(bind_id_list)
def UDP_data_out(user_cord,put_data,bind_list,my_pid):
    my_pid.put(os.getpid())
    global  time_delay1
    user_cord_list=[]
    all_bind_list=[]
    kcal_c=0
    kcal_h=0
    while 1:
        time.sleep(time_delay1)
        try:
            user_cord_list=user_cord.get(False)
            all_bind_list=bind_list.get(False)
        except :
            pass
       # print('all_bind_list', all_bind_list)
       # print('user_cord_list', user_cord_list)
        if kcal_c==254:
                kcal_c=0
                kcal_h=kcal_h+1
        else:
             kcal_c=kcal_c+1
        if user_cord_list and  all_bind_list :
            for x in range(len(all_bind_list)):
                try:
                    data = [33, 1, 5 , 245 , 225 , 0, 0, 0, 0, 88, 00, 99, 127, 218, 128, 12, 128, 0, 127, 14, 12, 111, 211,
                            0, 127, 142, 128, 12, 154, 0, 127, 218, 128, 12, 128, 0, 127, 218, 128, 11, 128, 0, 127, 143,
                            128, 11, 155, 222, 143, 142, 143, 11, 128, 0, 127, 218, 128, 12, 127, 255, 127, 218, 128, 12,
                            127, 255, 0, 0, 0, 0, 0, 0, 166, 136, 22, 201, 143, 95, 127, 141, 134, 198, 143, 99, 127, 141,
                            134, 198, 143, 98, 33, 33, 33, 33, 33, 33, 127, 142, 33, 200, 143, 97, 127, 134, 134, 191, 143,
                            95, 127, 134, 134, 191, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 0, 0, 0, 0, 0,
                            0, 0, 0,66]
                    data[6:10] = user_cord_list[x]
                    data[5]=all_bind_list[x]
                    data[10] = random.randint(90, 180)  #心率
                    data[12]= kcal_c  #卡路里
                    data[11] = kcal_h  # 卡路里
                    #data[10] =  100+    int(all_bind_list[x])      # 心率
                    for z in range(15, 120):
                        data[z] = random.randint(0, 255)
                    put_data.put(data)
                   # print(data)
                except:
                    pass
def UDP_put(put_data,my_pid):#用于发送给pad数据
    my_pid.put(os.getpid())
    send_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while 1:
        data=put_data.get()
        send_1.sendto(bytes(data), ('192.168.8.255', 8003))
def put_null(put_data,bind_list_1,my_pid,sign=True,total=32):
    global  time_delay1
    my_pid.put(os.getpid())
    all_bind_list=[0]
    while 1:
        time.sleep(time_delay1)
        try:
            all_bind_list= bind_list_1.get(False)
        except:
           pass
        if  not all_bind_list:
            all_bind_list = [0]
        if all_bind_list[-1]<32 and sign == True:
            logging.info(str(sign)+'33333333')
            for bin in range(int(all_bind_list[-1]),int(total)):
                data = [33, 1, 5, 245, 225, bin, 0, 0, 0, 0, 0, 0, 10, 127, 218, 128, 12, 128, 0, 127, 14, 12, 111, 211,
                        0, 127, 142, 128, 12, 154, 0, 127, 218, 128, 12, 128, 0, 127, 218, 128, 11, 128, 0, 127, 143,
                        128, 11, 155, 222, 143, 142, 143, 11, 128, 0, 127, 218, 128, 12, 127, 255, 127, 218, 128, 12,
                        127, 255, 0, 0, 0, 0, 0, 0, 166, 136, 22, 201, 143, 95, 127, 141, 134, 198, 143, 99, 127, 141,
                        134, 198, 143, 98, 33, 33, 33, 33, 33, 33, 127, 142, 33, 200, 143, 97, 127, 134, 134, 191, 143,
                        95, 127, 134, 134, 191, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 0, 0, 0, 0, 0,
                        0, 0, 0,66]
                put_data.put(data)
        else:
          #  logging.info(str(sign)+'22222222222')
            data = [33, 1, 5, 245, 225, int(all_bind_list[-1]), 0, 0, 0, 0, 0, 0, 10, 127, 218, 128, 12, 128, 0, 127, 14, 12, 111, 211,
                    0, 127, 142, 128, 12, 154, 0, 127, 218, 128, 12, 128, 0, 127, 218, 128, 11, 128, 0, 127, 143,
                    128, 11, 155, 222, 143, 142, 143, 11, 128, 0, 127, 218, 128, 12, 127, 255, 127, 218, 128, 12,
                    127, 255, 0, 0, 0, 0, 0, 0, 166, 136, 22, 201, 143, 95, 127, 141, 134, 198, 143, 99, 127, 141,
                    134, 198, 143, 98, 33, 33, 33, 33, 33, 33, 127, 142, 33, 200, 143, 97, 127, 134, 134, 191, 143,
                    95, 127, 134, 134, 191, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 0, 0, 0, 0, 0,
                    0, 0, 0, 66]
            put_data.put(data)
def fictitious_bind(sign,total=32,time_delay=1,Q=False):
    global  time_delay1
    time_delay1=time_delay
    my_db = orm_to_mysql(my_sql_link_pool())
    my_db.table('web_platform_phone').updata({'phone_code': str(os.getpid())},id=101)
    UDP_data = Queue()  # 传接从pad收到包
    user_cord = Queue()  # 解析出来的用户数据
    bind_list = Queue()
    bind_list_1 = Queue()
    put_data = Queue()
    my_pid= Queue()
    p1 = Process(target=get_UDP_data, args=(UDP_data,my_pid,))
    p2 = Process(target=read_UDP_data, args=(UDP_data, user_cord, bind_list, bind_list_1,my_pid,))
    p3 = Process(target=UDP_data_out, args=(user_cord, put_data, bind_list,my_pid,))
    p4 = Process(target=UDP_put, args=(put_data,my_pid,))
    p5 = Process(target=put_null, args=(put_data, bind_list_1,my_pid,sign,total,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    my_pid_list=[]
    for x in range(5):
        my_pid_list.append(  my_pid.get())
    if Q :
        Q.put(my_pid_list)
    my_db.table('web_platform_phone').updata({'phone_code': str(my_pid_list)},id=101)
    p1.join()
if __name__=='__main__':
    fictitious_bind(sign=False,total=32,time_delay=1)
