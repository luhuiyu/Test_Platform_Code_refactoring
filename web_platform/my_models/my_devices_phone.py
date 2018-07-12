#在数据库里面获取当前在线的机子
from web_platform.models import devices_phone
import  os,re
from web_platform.models import devices_phone

def get_devices_info(platform_name):
    a = devices_phone.objects.filter(platformName=platform_name)
    phone_list=[]
    for x in a:
        device_one = {}
        device_one['id']=x.id
        device_one['deviceName']=x.deviceName
        device_one['platformName']=x.platformName
        device_one['platformVersion']=x.platformVersion
        device_one['state']=x.state
        device_one['used']=x.used
        phone_list.append(device_one)
    return phone_list





def get_devices_info_Android():
    '''
    用于获取获取机器当前的设备连接情况
    用于本机的，只是用于测试

    '''
    i=0
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
                    devices_phone(id=device_one['id'],
                                  deviceName=deviceName,
                                  platformName=device_one['platformName'],
                                  platformVersion=device_one['platformVersion'],
                                  state = device_one['state'],
                                  used=0
                                  ).save()
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
                    devices_phone(id=device_one['id'],
                                  deviceName=deviceName,
                                  platformName=device_one['platformName'],
                                  platformVersion=device_one['platformVersion'],
                                  state=device_one['state'],
                                  used=0
                                  ).save()
                    device_list.append(device_one)
                    i = i + 1
    return device_list