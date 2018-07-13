import  os,re
from my_python_code.mysql.Basic_information import my_sql_link

'''
本文件用于获取获取机器当前的设备连接情况
用于本机的，只是用于测试

'''
def get_devices_info_Android():
    i=0
    a = my_sql_link()
    db = a.db
    cursor = a.cursor
    device_list = []
    platformName='Android'
    a = os.popen('adb devices')
    for line in list(a.readlines()):
        device_one = {}
        if 'devices attached' not in line:
            if 'device' in line or 'offline' in line:
                if 'device' in line:
                    line = re.sub("device", "", line)
                    line = re.sub(r"\t\n", "", line)
                    device_one['deviceName'] = line
                    deviceName=line
                    deviceAndroidVersion = os.popen('adb -s ' + line + '  shell getprop ro.build.version.release')
                    version = re.sub(r"\n", "", deviceAndroidVersion.read())
                    device_one['platformVersion'] = version
                    device_one['state'] = 'device'
                    device_one['id'] = i
                    device_one['platformName']='Android'
                    i=i+1
                    sql='REPLACE INTO web_platform_devices_phone (id,deviceName,platformName,platformVersion,state,used )VALUES (\''+str(i)+ '\',\''+str(deviceName)+'\',\''+platformName+'\',\''+ version+'\',\'devices\',\'0\')'
                    cursor.execute(sql)
                    db.commit()
                    device_list.append(device_one)

                elif 'offline' in line:
                    line = re.sub("offline", "", line)
                    line = re.sub(r"\t\n", "", line)
                    device_one['deviceName'] = line
                    deviceName=line
                    deviceAndroidVersion = os.popen('adb -s ' + line + '  shell getprop ro.build.version.release')
                    version = re.sub(r"\n", "", deviceAndroidVersion.read())
                    if not version:
                        version = 'unknown '
                    device_one['platformVersion'] = version
                    device_one['state'] = 'offline'
                    device_one['id'] = i
                    device_one['platformName']='Android'
                    sql = 'REPLACE INTO web_platform_devices_phone (id,deviceName,platformName,platformVersion,state,used )VALUES (\'' + str(
                        i) + '\',\'' + str(deviceName) + '\',\'' + platformName + '\',\'' + version + '\',\'offline\',\'0\')'
                    cursor.execute(sql)
                    db.commit()
                    device_list.append(device_one)
                    i = i + 1
    return device_list

if __name__=='__main__':
    print(get_devices_info_Android())