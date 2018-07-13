import socket,time,os
import random
from multiprocessing import Process
from multiprocessing import Queue
from my_python_code.mysql.Basic_information import my_sql_link
#from my_python_code.mysql.ORM_of_mysql import orm_to_mysql

'''
虚拟臂带，之前大部分都用的list，导致有很多bug。现在都改为dict
参数设置    total 臂带总数，最大值255
            time_delay   发送udp包的时间间隔，浮点数字

队列
put_user_data =  Queue() #发送用户绑定数据
my_pid =  Queue()  #  传递当前进程的pid

'''
def get_UDP_data(put_user_data,put_user_data2,my_pid):
    '''
    :param get_pad_to_bind_data: 传递pad发送给臂带的udp包
    :param my_pid:传递当前进程的pid
    :param put_user_data:发送当前的已绑定的用户信息
    :return:
     用于接收pad发给臂带的udp包，然后根据 0x24 0x25 协议删增已绑定用户列表
    '''
    my_pid.put(os.getpid())
    get_ueserinfo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    get_ueserinfo.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    get_ueserinfo.setblocking(1)
    get_ueserinfo.bind(('', 8001))
    user_data = {}  # user_data 保存用户的userid和臂带编号，已{userid:bindcode}形式保存
    bind_index=0  #臂带的编号最后一位，为的是避免编号重复，每调用一次应该+1
    while True:
        data, addr = get_ueserinfo.recvfrom(1024)
        data=list(data)
        if data[0] == 36:
            print(data)
            '''
            udp编号:0x24
            教练Pad通过UDP:8001端口向臂带反馈用户佩戴臂带确认连接的协议，
            包括下发对应用户信息，臂带完成配置后，
            通过UDP:8003端口向教练Pad反馈配置结果。
            通过0x24获取User ID
            '''
            if str(data[2:6]) not in user_data.keys():
               user_data[str(data[2:6])]=bind_index
               bind_index=bind_index+1
               put_user_data.put(user_data)
               put_user_data2.put(user_data) # 给unbind_code的
               print(user_data)
        elif data[0]==37:
            '''
            Pad通过UDP:8001端口向设备反馈课程结束信息，臂带重新进入到发送连接请求阶段。
            臂带存储当前用户的运动步数和消耗卡路里的数据到历史数据中，但是界面显示清零。
            通过通过UDP:8003端口反馈结果。
            用于切换臂带或者结束课程
            '''
            if str(data[2:6])  in user_data.keys():
                user_data.pop(str(data[2:6]))
                put_user_data.put(user_data)
def binded_user_data(put_user_data,put_udp_data,interval,my_pid):
   '''
    生成已经绑定用户的udp包数据,把生成的数据传递到下一个函数
   :param put_user_data: 传递绑定用户的数据
   :param put_udp_data:  传递需要发送的udp包数据
   :param interval: 发送udp包的间隔
   :param my_pid:  传递进程的pid
   :return:
   '''
   user_cord_data={}
   original_data = [33, 1, 5, 245, 225, 0, 0, 0, 0, 0, 0, 99, 127, 218, 128, 12, 128, 0, 127, 14, 12, 111, 211,
           0, 127, 142, 128, 12, 154, 0, 127, 218, 128, 12, 128, 0, 127, 218, 128, 11, 128, 0, 127, 143,
           128, 11, 155, 222, 143, 142, 143, 11, 128, 0, 127, 218, 128, 12, 127, 255, 127, 218, 128, 12,
           127, 255, 0, 0, 0, 0, 0, 0, 166, 136, 22, 201, 143, 95, 127, 141, 134, 198, 143, 99, 127, 141,
           134, 198, 143, 98, 33, 33, 33, 33, 33, 33, 127, 142, 33, 200, 143, 97, 127, 134, 134, 191, 143,
           95, 127, 134, 134, 191, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 0, 0, 0, 0, 0,
           0, 0, 0, 66]
   kcal_c = 0   #卡路里 低位 最大值  256
   kcal_h = 0  #卡路里 高位  最大值  256
   while True:
       time.sleep(float(interval))
       try:
           user_cord_data =  put_user_data.get(False)
           #如果用户状态被更新就获取数据
       except:
           pass
       if kcal_c == 254:#用于进位
           kcal_c = 0
           kcal_h = kcal_h + 1
       else:
           kcal_c = kcal_c + 1
       if user_cord_data :
           print('binded_user_data',user_cord_data)
           for user_cord in user_cord_data:
               '''
               对udp包做处理，使其复合要求
               '''
               data=original_data
               data[6:10] = eval(user_cord)  #用户id
               data[5] = int(user_cord_data[user_cord])  #臂带编号
               data[10] = random.randint(1, 255)  # 心率
               data[12] = kcal_c  # 卡路里
               data[11] = kcal_h  # 卡路里
               # data[10] =  100+    int(all_bind_list[x])      # 心率
               for z in range(15, 120):
                   #xyz数据随机填充
                   data[z] = random.randint(0, 255)
               time.sleep(0.01)
              # print(data)
               put_udp_data.put(data)

def unbind_code(put_user_data2,put_udp_data,total,interval,my_pid):
    user_cord_data = {}
    original_data = [33, 1, 5, 245, 225, 0, 0, 0, 0, 0, 0, 99, 127, 218, 128, 12, 128, 0, 127, 14, 12, 111, 211,
                     0, 127, 142, 128, 12, 154, 0, 127, 218, 128, 12, 128, 0, 127, 218, 128, 11, 128, 0, 127, 143,
                     128, 11, 155, 222, 143, 142, 143, 11, 128, 0, 127, 218, 128, 12, 127, 255, 127, 218, 128, 12,
                     127, 255, 0, 0, 0, 0, 0, 0, 166, 136, 22, 201, 143, 95, 127, 141, 134, 198, 143, 99, 127, 141,
                     134, 198, 143, 98, 33, 33, 33, 33, 33, 33, 127, 142, 33, 200, 143, 97, 127, 134, 134, 191, 143,
                     95, 127, 134, 134, 191, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 0, 0, 0, 0, 0,
                     0, 0, 0, 66]
    while True :

        try:
            user_cord_data = put_user_data2.get(False)
            # 如果用户状态被更新就获取数据
        except:
            pass
        if    user_cord_data:
        #    print('unbind_code',user_cord_data)
            time.sleep(10*float(interval))
            for unbind in range(0,int(total)):
                if unbind not in user_cord_data.values():
                    data=original_data
                    data[5]=unbind
                    put_udp_data.put(data)
        else:
            for unbind in range(0, int(total)):
                data = original_data
                data[5] = unbind
                time.sleep(0.01)
                put_udp_data.put(data)
def UDP_put(put_udp_data,my_pid):#用于发送给pad数据
    '''
    用于广播数据
    :param put_udp_data:
    :param my_pid:
    :return:
    '''
    my_pid.put(os.getpid())
    send_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        data=put_udp_data.get()
        time.sleep(0.01)
 #       print(data)
        send_1.sendto(bytes(data), ('192.168.8.255', 8003))



if __name__=='__main__':
    #get_UDP_data(put_user_data,my_pid)
    #binded_user_data(put_user_data, put_udp_data, interval, my_pid)
    #unbind_code(put_user_data,put_udp_data,total,interval,my_pid)
    #UDP_put(put_udp_data,my_pid)
    put_user_data =  Queue()
    put_user_data2 =  Queue()
    my_pid =  Queue()
    put_udp_data =  Queue()
    total = 32
    interval = 1

    p1 = Process(target=get_UDP_data, args=(put_user_data,put_user_data2,my_pid,))
    p2 = Process(target=binded_user_data, args=(put_user_data, put_udp_data, interval, my_pid,))
    p3 = Process(target=unbind_code,args=(put_user_data2,put_udp_data,total,interval,my_pid,))
    p4 = Process(target=UDP_put, args=(put_udp_data,my_pid,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    my_pid_list = []
    for x in range(5):
        my_pid_list.append(my_pid.get())
    #my_db.table('web_platform_phone').updata({'phone_code': str(my_pid_list)}, id=101)
    p1.join()