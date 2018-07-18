import os
import uuid
from my_python_code.basic_configuration.configuration_file import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform_Code_refactoring.settings")  # NoQA
os.environ.get(MY_PYTHON_CODE_PATH)
import django
django.setup()  # NoQA
from  my_python_code.mysql.Basic_information import my_sql_link
from web_platform.my_models.get_my_task import get_task_queue_custom
from web_platform.models import task_management,my_case_of_API,my_report
from my_python_code.basic_configuration.configuration_file import *
from multiprocessing import Process,Queue,Pool,Lock
from django.utils import timezone
import time


def run_case_of_api_main(work_process_quantity=4):
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
    # 进程锁，用于操作数据库时
    my_db_lock=Lock()
    # 分发case_id
    case_id_queue= Queue()
    task_info= Queue()
    the_case_result=Queue()
    statistical_results=Queue()
    start_test=Queue()
    work_process_total=work_process_quantity
    p1 = Process(target=task_distribution, args=(case_id_queue,task_info,start_test,work_process_total))
    result_report= Process(target=result_handling, args=(task_info,the_case_result,statistical_results))
    result_report.start()
    p1.start()
    for  x  in range(work_process_quantity):
        work_process = Process(target=case_work, args=(case_id_queue,my_db_lock,the_case_result,statistical_results,start_test,))
        work_process.start()
    p1.join()
def task_distribution(case_id_queue,task_info,start_test,work_process):
    '''
    获取任务，把case_id传进 队列 case_id_Queue
    :param case_id:
    :return:
    '''
    task_type='apitest'
    task_state_custom=0
    now_time=timezone.now()
    get_now_task=task_management.objects.filter(task_type=task_type,task_state=task_state_custom,create_time__lte=now_time).order_by("-id")[0]
    case_list=eval(get_now_task.task_data) ['case_list']
    for case_id in case_list:
        case_id_queue.put(case_id)
    for x in range(work_process)  :
        start_test.put(1)
    task_info.put(get_now_task)
    task_info.put(len(case_list))
    return True


def case_work(case_id_Queue,my_db_lock,the_case_result,statistical_results,start_test):
    '''
    运行单个case，同时通过队列传递结果
    :param case_id_Queue:
    :return:
    '''
    start_test.get()
    try:
        while 1 :
             completion_Success = 0
             pass_case = 0
             failure_case = 0
             Collapse_case = 0
             case_id=case_id_Queue.get(False)
             test_case_result_one = {}
             try:
                 case_one = my_case_of_API.objects.get(id=case_id)  # 根据 case表的id 查询case的信息，用于运行
                 App_version = case_one.App_version
                 case_address =(MY_PYTHON_CODE_NAME + '\\'+MY_APICASE_PATH + '\\' + case_one.project_name + '.' + case_one.case_address + '.' + case_one.case_name).replace('\\','.')
                 exec('import  ' + case_address)
                 example = eval(case_address + '.API_case(my_db_lock=my_db_lock) ')
                 running_result = example.test_case()
                 test_case_result_one = {"case_id": case_one.id, "module_name": case_one.module_name,
                                         'case_name': case_one.case_name, "api_name": case_one.api_name,
                                         }
                 test_case_result_one.update(running_result)
                 completion_Success = completion_Success + 1
             except Exception as e:
                 test_case_result_one = {"case_id": case_one.id, "module_name": case_one.module_name,
                                         'case_name': case_one.case_name, "api_name": case_one.api_name,
                                         }
                 test_case_result_one.update({"result": -1, "error_info": '\'' + str(e) + '\''})
             finally:
                 if test_case_result_one["result"] == 1:
                     pass_case = pass_case + 1
                 elif test_case_result_one["result"] == 0:
                     failure_case = failure_case + 1
                 elif test_case_result_one["result"] == -1:
                     Collapse_case = Collapse_case + 1
             the_case_result.put(test_case_result_one)
             statistical_results.put({'completion_Success':completion_Success,'pass_case':pass_case,'failure_case':failure_case,'Collapse_case':Collapse_case,'App_version':App_version})
    except  Exception as e :
        return

def result_handling(task_info,the_case_result,statistical_results):
    the_task_info=task_info.get()
    update_state = task_management.objects.get(id=the_task_info.id)
    update_state.task_state = 1
    update_state.save()
    start_time=time.time()
    report_data={}
    test_case_result=[]
    completion_Success = 0
    pass_case = 0
    failure_case = 0
    Collapse_case = 0
    App_version=''
    case_total=int(task_info.get())
    for x  in range(case_total):
        test_case_result.append(the_case_result.get())
        case_statistical=statistical_results.get()
        completion_Success=completion_Success+case_statistical['completion_Success']
        pass_case=pass_case+case_statistical['pass_case']
        failure_case=failure_case+case_statistical['failure_case']
        Collapse_case=Collapse_case+case_statistical['Collapse_case']
        App_version=case_statistical['App_version']
    report_data['test_case_result'] = test_case_result
    report_data['platfor'] =the_task_info.task_type
    report_data['project'] = the_task_info.task_project
    report_data['completion_rate'] = int(completion_Success / case_total * 100)  # 终端完成率
    report_data['pass_tate'] = int(pass_case / case_total * 100)  # Case通过率
    report_data['failure_rate'] = int(failure_case / case_total * 100)  # Case失败率
    report_data['Collapse_rate'] = int(Collapse_case / case_total * 100)  # 终端崩溃率
    report_data['Collapse_time'] = int(time.time() - start_time)
    if report_data['pass_tate'] == 100:
        report_result = 1
    else:
        report_result = 0
    my_report(user_name=web_user_name, report_data=report_data, report_result=report_result,uuid=uuid.uuid4(), App_name=the_task_info.task_project, terminal_number=1, test_type=the_task_info.task_type,App_version=App_version).save()
    update_state.task_state = 2
    update_state.save()
if __name__=='__main__':
    run_case_of_api_main(10)