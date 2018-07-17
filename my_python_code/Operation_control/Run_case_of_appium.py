import os,time,uuid
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform.settings")  # NoQA
import django
django.setup()  # NoQA
from my_python_code.basic_configuration.configuration_file import *
from multiprocessing import  Process, Pool,Queue,Manager
from web_platform.models import task_management,my_case_of_UI,my_report,devices_phone,phone
from web_platform.my_models.get_task import get_task_queue_custom

def run_appium_case(rult,phone_list_one,case_address,PORT):
    try:
        context = {}
        exec('import  ' + case_address)
        context['PORT'] = str(PORT)
        context['deviceName'] = phone_list_one[1]
        context['platformName'] = phone_list_one[2]
        context['platformVersion'] = phone_list_one[3]
        context['phone'] = phone_list_one[6]
        context['case_address']=Complete_path+'/'+case_address
        print('context[case_address]',context['case_address'])
        print("jichen ")
        example = eval(case_address + '.test_case(context)')
        rult.put(example)
    except Exception as e:
        deviceName = phone_list_one[1]
        rult.put({'driverName':str(deviceName),"result":'-1',"error_info": 'run_appium_case  '+'\''+str(e)+'\''})










def run_testcase(rult,phone_list,case_address):
    '''
    p = Pool(5)
    PORT=4910
    for phone_list_one in phone_list:
        p.apply(run_appium_case, args=(rult,phone_list_one,case_address,PORT))
        PORT = PORT + 1
    p.close()
    #p.join()

     PORT = 4910
    for phone_list_one in phone_list:
        print(phone_list_one)
        p=Process(target=run_appium_case, args=(rult,phone_list_one,case_address,PORT,))
        p.start()

'''





    p = Pool(4)
    PORT = 4910
    for phone_list_one in phone_list:
        p.apply_async(run_appium_case, args=(rult, phone_list_one, case_address, PORT))
        PORT = PORT + 1
    p.close()
    p.join()
    print('进程结束')


def run_ui_case():
    context={}
    phone_queue=Manager().Queue()
    rult = Manager().Queue()
    get_phone_list=devices_phone.objects.filter(used=1)
    if not get_phone_list:
        print('没有手机，等待10秒')
        time.sleep(10)
        return
    phone_list=[]
    for y in range(len(get_phone_list)):
        phone_queue.put(phone.objects.get(id=y+1).phone_code)
    for x in get_phone_list:
        phone_list.append([x.id,x.deviceName,x.platformName,x.platformVersion,x.state,x.used,phone_queue.get()])
    print(phone_list)
    task_queue=get_task_queue_custom(context,'uitest',0) #这个用于获取没有运行的任务列表
    if  task_queue :
        for task_one in task_queue["task_state_list"]:  #全部的任务
            start_time=time.time()
            update_state=task_management.objects.get(id=task_one[0])
            update_state.task_state = 1
            update_state.save()
            test_case_result = []  # 结果列表  单个任务的结果
            report_data={}  #报告的json
            completion_Success = 0  #成功的case数
            pass_case = 0   #通过的个数
            failure_case = 0  #失败的case
            Collapse_case = 0  #崩溃的个数

            if  task_one[3] == 0:
                case_list=eval(task_one[5]) #获取的case列表
                case_total =len(case_list["case_list"])

                for y in case_list["case_list"]:
                    devices_result_list = []
                    case_info = my_case_of_UI.objects.get(id=y)  # 根据 case表的id 查询case的信息，用于运行

                    the_case_pass = 0 #这个case的通过个数
                    the_case_not_pass = 0
                    App_version=case_info.App_version
                    try:
                        case_address = (
                            MY_PYTHON_CODE_NAME + '\\' + MY_APPIUM_PATH + '\\' + case_one.project_name + '.' + case_one.case_address + '.' + case_one.case_name).replace(
                            '\\', '.')
                        run_testcase(rult,phone_list,case_address)
                        for i in range(len(get_phone_list)):
                            now_rult=rult.get()
                            devices_result_list.append(now_rult)
                            if now_rult["result"]==1:
                                the_case_pass=the_case_pass+1
                            else:
                                the_case_not_pass=the_case_not_pass+1
                            if  'error_info' not in now_rult.keys() :
                                completion_Success=completion_Success+1
                        test_case_result_one = {"case_id":case_info.id,"module_name":case_info.module_name, 'case_name':case_info.case_name, "case_pass":the_case_pass,"case_not_pass":the_case_not_pass,"devices_result_list":devices_result_list}
                    except Exception as e:
                        the_case_not_pass=1
                        Collapse_case=Collapse_case+1
                        test_case_result_one = {"case_id":case_info.id,"module_name":case_info.module_name, 'case_name':case_info.case_name, "case_pass":the_case_pass,"case_not_pass":the_case_not_pass,"error_info":'run_case   '+'\'' + str(e) + '\''}
                    finally:
                        print('fin')
                        if the_case_not_pass==0:
                            pass_case=pass_case+len(get_phone_list)
                        else:
                            failure_case=failure_case+1
                        test_case_result.append(test_case_result_one)
                report_data["test_case_result"]=test_case_result
                report_data['platfor'] = task_one[1]
                report_data['project'] = task_one[2]
                report_data['completion_rate'] = int((completion_Success / (case_total *len(get_phone_list)))* 100)  # 终端完成率
                report_data['pass_tate'] = int((pass_case / (case_total *len(get_phone_list)) )* 100)  # Case通过率
                print(111111,pass_case,case_total,len(get_phone_list))
                report_data['failure_rate'] = int((failure_case / (case_total *len(get_phone_list)) )* 100  )# Case失败率
                report_data['Collapse_rate'] = int((Collapse_case / (case_total *len(get_phone_list)) )* 100)  # 终端崩溃率
                report_data['Collapse_time'] = int(time.time() - start_time)
                print(report_data)
                if report_data['pass_tate'] == 100:
                    report_result = 1
                else:
                    report_result = 0
                now_report = my_report(user_name=web_user_name, report_data=report_data, report_result=report_result,
                                       uuid=uuid.uuid4(), App_name=task_one[2], terminal_number=len(get_phone_list), test_type=task_one[1],
                                       App_version=App_version)
                now_report.save()
                update_state.task_state = 2
                update_state.save()
            return


if __name__ == '__main__':
    while 1:
        time.sleep(10)
        run_ui_case()



