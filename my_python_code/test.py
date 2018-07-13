import socket
get_ueserinfo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
get_ueserinfo.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
get_ueserinfo.setblocking(1)
get_ueserinfo.bind(('', 8003))
while True:
    user_id, addr = get_ueserinfo.recvfrom(1024)
    A=list(user_id)
    if( A[0]==33 and len(A)==135 )or ( A[0]==33 and len(A)==136 and A[-1] == 9  ):
        bind = ''
        # print('udp编号'+str(l[1]))
        for x in A[2:6]:  # byte3-byte6  设备ID(Device ID
            x = str(hex(x))[2:]
            if len(x) == 1:
                x = '0' + x
            bind = bind + x
        bind_code = str(int(bind, 16))  # 臂带编号
    #    print('0x21数据正常',addr,bind_code)
    else:
         print('+++++++')
         print(list(user_id),addr,len(A))
         print('=========')