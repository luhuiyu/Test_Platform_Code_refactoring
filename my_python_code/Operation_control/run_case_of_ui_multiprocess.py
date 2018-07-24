import os
import uuid
from my_python_code.basic_configuration.configuration_file import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform_Code_refactoring.settings")  # NoQA
os.environ.get(MY_PYTHON_CODE_PATH)
import django
django.setup()  # NoQA
from my_python_code.basic_configuration.configuration_file import *
from multiprocessing import Process,Queue,Pool,Lock
from django.utils import timezone
import time
from web_platform.models import *
import logging
logging.basicConfig(level=logging.WARNING)

def run_case_of_ui_main():
    '''
    mian 负责控制所有的进程
        返回 启动的结果，不需要返回运行结果
    task_distribution
        负责分发任务，每次只在数据库读取一次任务，然后获取case_list，把case_list的数据分发给case_work
    result_handling
        处理 case_work返回的结果，生成报告插入数据库
    case_work
        负责单个case的运行，
    :return:
    '''
    appium_Queue=Queue()
    task_Queue=Queue()
    the_case_result=Queue()
    task_info=Queue()
    statistical_results=Queue()
    p1 = Process(target=task_distribution, args=(appium_Queue,task_Queue,task_info,))
    p1.start()
    p2= Process(target=result_handling, args=(the_case_result,statistical_results,task_info,))
    p2.start()
    work_process_quantity=len(devices_phone.objects.filter(used=1))
    for x in range(work_process_quantity):
        work_process = Process(target=case_work,args=(appium_Queue,task_Queue,the_case_result,statistical_results,))
        work_process.start()


def task_distribution(appium_Queue,task_Queue,task_info):
    start_time=time.time()
    task_info.put(start_time)
    task_type = 'uitest'
    task_state_custom = 0
    now_time = timezone.now()
    get_now_task = task_management.objects.filter(task_type=task_type, task_state=task_state_custom,create_time__lte=now_time).order_by("-id")[0]
    case_list = eval(get_now_task.task_data)['case_list']
    get_phone_mac_list=devices_phone.objects.filter(used=1)
    get_phone_number=phone.objects.all()
    task_info.put(get_now_task)
    task_info.put(case_list)
    phone_data=[]
    for x in range(min(len(get_phone_mac_list),len(get_phone_number))) :
        my_test_phone_number=get_phone_number[x].phone_code
        my_test_phone_data=get_phone_mac_list[x]
        the_context={}
        the_context['platformName'] = my_test_phone_data.platformName
        the_context['platformVersion'] = my_test_phone_data.platformVersion
        the_context['deviceName'] = my_test_phone_data.deviceName
        the_context['PORT'] = str(4910+x)
        the_context['phone'] = my_test_phone_number
        the_context['system']=my_test_phone_data
        phone_data.append(the_context)
    for z in case_list:
        task_Queue.put(z)
    for y in phone_data:
        appium_Queue.put(y)


def result_handling(the_case_result,statistical_results,task_info):
    start_time=task_info.get()
    get_now_task=task_info.get()
    get_now_task.task_state = 1
    get_now_task.save()
    case_list=task_info.get()
    case_total=len(case_list)
    report_data = {}  # 报告的json
    completion_Success = 0  # 成功的case数
    pass_case = 0  # 通过的个数
    failure_case = 0  # 失败的case
    Collapse_case = 0  # 崩溃的个数
    test_case_result=[]
    App_version=''
    for x in case_list:
        results=statistical_results.get()
        completion_Success=completion_Success+results['completion_Success']
        pass_case=pass_case+results['pass_case']
        failure_case=failure_case+results['failure_case']
        Collapse_case=Collapse_case+results['Collapse_case']
        App_version=results['App_version']
        test_case_result.append(the_case_result.get())
    report_data['test_case_result'] = test_case_result
    report_data['platfor'] = get_now_task.task_type
    report_data['project'] = get_now_task.task_project
    report_data['completion_rate'] = int(completion_Success / case_total * 100)  # 终端完成率
    report_data['pass_tate'] = int(pass_case / case_total * 100)  # Case通过率
    report_data['failure_rate'] = int(failure_case / case_total * 100)  # Case失败率
    report_data['Collapse_rate'] = int(Collapse_case / case_total * 100)  # 终端崩溃率
    report_data['Collapse_time'] = int(time.time() - start_time)
    if report_data['pass_tate'] == 100:
        report_result = 1
    else:
        report_result = 0
    my_report(user_name=web_user_name, report_data=report_data, report_result=report_result, uuid=uuid.uuid4(),
              App_name=get_now_task.task_project, terminal_number=1, test_type=get_now_task.task_type,
              App_version=App_version).save()
    get_now_task.task_state = 2
    get_now_task.save()

def case_work(appium_Queue,task_Queue,the_case_result,statistical_results,):
    context=appium_Queue.get()
    while True:
         if task_Queue.empty():
            return
         completion_Success = 0  # 成功的case数
         pass_case = 0  # 通过的个数
         failure_case = 0  # 失败的case
         Collapse_case = 0  # 崩溃的个数
         case_id = task_Queue.get()
         test_case_result_one = {}
         devices_result_list=[]
         the_case_pass = 0  # 这个case的通过个数
         the_case_not_pass = 0
         case_info = my_case_of_UI.objects.get(id=case_id)  # 根据 case表的id 查询case的信息，用于运行
         App_version = case_info.App_version
         try:
             case_address = (MY_PYTHON_CODE_NAME + '\\' + MY_APPIUM_PATH + '\\' + case_info.project_name + '.' + case_info.case_address + '.' + case_info.case_name).replace( '\\', '.')
             exec('import  ' + case_address)
             context['case_address']=case_address
             running_result = eval(case_address + '.test_case(context)')
             if running_result["result"] == 1:
                 the_case_pass = the_case_pass + 1
             else:
                 the_case_not_pass = the_case_not_pass + 1
             if 'error_info' not in running_result.keys():
                 completion_Success = completion_Success + 1
             devices_result_list.append(running_result)
             test_case_result_one = {"case_id":case_info.id,"module_name":case_info.module_name,
                                     'case_name':case_info.case_name,"case_pass":the_case_pass,
                                     "case_not_pass":the_case_not_pass,"devices_result_list":devices_result_list}
         except Exception as e:
             the_case_not_pass = 1
             Collapse_case = Collapse_case + 1
             test_case_result_one = {"case_id": case_info.id, "module_name": case_info.module_name,
                                     'case_name': case_info.case_name, "case_pass": the_case_pass,
                                     "case_not_pass": the_case_not_pass,
                                     "error_info": 'run_case   ' + '\'' + str(e) + '\'',"result": -1,}
         finally:
             the_case_result.put(test_case_result_one)
             statistical_results.put(
                 {'completion_Success': completion_Success, 'pass_case': the_case_pass, 'failure_case': the_case_not_pass,
                  'Collapse_case': Collapse_case, 'App_version': App_version})
             if task_Queue.empty():
                 return




if __name__=='__main__':
    run_case_of_ui_main()