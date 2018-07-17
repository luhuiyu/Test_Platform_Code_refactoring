import os
from my_python_code.basic_configuration.configuration_file import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform_Code_refactoring.settings")  # NoQA
os.environ.get(MY_PYTHON_CODE_PATH)
import django
django.setup()  # NoQA
from  my_python_code.mysql.Basic_information import my_sql_link
from web_platform.my_models.get_my_task import get_task_queue_custom
from web_platform.models import task_management,my_case_of_API,my_report
from my_python_code.basic_configuration.configuration_file import *
from multiprocessing import Process,Queue,Pool
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
    case_id_queue= Queue()  # 分发case_id
    p1 = Process(target=task_distribution, args=(case_id_queue,))
  #  p1.daemon = True
    p1.start()
    for  x  in range(work_process_quantity):
        work_process = Process(target=case_work, args=(case_id_queue,))
        work_process.start()
    p1.join()
def task_distribution(case_id_queue):
    '''
    获取任务，把case_id传进 队列 case_id_Queue
    :param case_id:
    :return:
    '''
    task_type='apitest'
    task_state_custom=0
    now_time=timezone.now()
    try:
        get_now_task=task_management.objects.filter(task_type=task_type,
                                                    task_state=task_state_custom,
                                                    create_time__lte=now_time
                                                       ).order_by("-id")[0]
    except IndexError:
        return False
    for case_id in eval(get_now_task.task_data) ['case_list']:
        case_id_queue.put(case_id)
    return True


def case_work(case_id_Queue):
    '''
    运行单个case，同时通过队列传递结果
    :param case_id_Queue: 
    :return: 
    '''
    time.sleep(5) # 因为开始的时候  case_id_Queue.empty() 一定是TRUE,所以需要一个延时
    while 1 :
        time.sleep(1)
        try:
             completion_Success = 0
             pass_case = 0
             failure_case = 0
             Collapse_case = 0
             case_id=case_id_Queue.get(False)
             test_case_result_one = {}
             case_one = my_case_of_API.objects.get(id=case_id)  # 根据 case表的id 查询case的信息，用于运行
             App_version = case_one.App_version
             try:
                 case_address =(MY_PYTHON_CODE_NAME + '\\'+MY_APICASE_PATH + '\\' + case_one.project_name + '.' + case_one.case_address + '.' + case_one.case_name).replace('\\','.')
                 exec('import  ' + case_address)
                 example = eval(case_address + '.API_case()')
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
                 print(test_case_result_one)
                 print(os.getpid(),completion_Success,pass_case,failure_case,Collapse_case)
        except   :
            return

def result_handling():
    pass

if __name__=='__main__':
    run_case_of_api_main(6)