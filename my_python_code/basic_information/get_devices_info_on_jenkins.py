import  os,re
import sys
sys.path.append('F:\Test_Platform')
from my_python_code.mysql.Basic_information import my_sql_link
def get_devices_info():
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
                    device_one['index'] = i
                    i=i+1
                    sql='REPLACE INTO web_platform_devices_phone (id,deviceName,platformName,platformVersion,state )VALUES (\''+str(i)+ '\',\''+str(deviceName)+'\',\''+platformName+'\',\''+ version+'\',\'devices\')'
                    cursor.execute(sql)
                    db.commit()
                    device_list.append(device_one)
                elif 'offline' in line:
                    line = re.sub("offline", "", line)
                    line = re.sub(r"\t\n", "", line)
                    device_one['deviceName'] = line
                    deviceAndroidVersion = os.popen('adb -s ' + line + '  shell getprop ro.build.version.release')
                    version = re.sub(r"\n", "", deviceAndroidVersion.read())
                    if not version:
                        version = 'unknown '
                    device_one['platformVersion'] = version
                    device_one['state'] = 'offline'
                    device_one['id'] = i
                    sql = 'REPLACE INTO web_platform_devices_phone (id,deviceName,platformName,platformVersion,state )VALUES (\'' + str(
                        i) + '\',\'' + str(deviceName) + '\',\'' + platformName + '\',\'' + version + '\',\'offline\')'
                    cursor.execute(sql)
                    db.commit()
                    i = i + 1
                    device_list.append(device_one)
    return device_list

if __name__=='__main__':
    print(get_devices_info())