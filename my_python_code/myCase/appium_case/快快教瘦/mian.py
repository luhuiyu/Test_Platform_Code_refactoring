import time
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import appium_coachPad.test_case.正常上课
from appium_coachPad.interface.Basic_setting import UID_ALL,PORT
from multiprocessing import  Process, pool,Queue
class NoDaemonProcess(Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)
class MyPool(pool.Pool):
    Process = NoDaemonProcess
def star_appium(PORT,UID,q):
    url= 'appium -a 127.0.0.1   -bp 4739  -p '+PORT  #+ ' -U '+str(UID)
    pid=os.getpid()
    q.put(pid)
    a=os.system(url)
def run_testcase(driverName,platformVersion,port,q,phone = '15600905550'):
    pid=q.get(True)
    rust=[]
    if pid:
        time.sleep(10)
    try:
        system = 'Andriod'  # 手机系统
        url = 'http://127.0.0.1:'+port+'/wd/hub'
        appium_coachPad.test_case.正常上课.test_case(system, platformVersion, driverName, url, phone)
        return rust
    finally:
        os.popen('taskkill.exe  /F /pid:' + str(pid))
        return rust



def run_test(PORT,UID):  #一台手机一个线程
        PORT=str(PORT)
        platformVersion=UID[1]
        phone=UID[2]
        UID=UID[0]
        q=Queue()
        appiun_process = Process(target=star_appium, args=(PORT, UID,q,))
        time.sleep(4)
        test_process = Process(target=run_testcase, args=(UID,platformVersion, PORT,q,phone,))
        appiun_process.start()
        test_process.start()


if __name__ == '__main__':

        p = MyPool(4)
        for UID in UID_ALL:
            p.apply(run_test, args=(PORT, UID,))
            time.sleep(3)
            PORT=PORT+1
        p.close()
        p.join()











