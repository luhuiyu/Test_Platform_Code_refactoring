
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform.settings")  # NoQA
import django
django.setup()  # NoQA


from  my_python_code.mysql.Basic_information import my_sql_link
from web_platform.models import task_management,my_case_of_API,my_report
from web_platform.my_models.get_task import get_task_queue_custom
from my_python_code.basic_configuration.configuration_file import *
import uuid,time
def  run_api_case():
    context={}
    task_queue=get_task_queue_custom(context,'apitest',0) #这个用于获取没有运行的任务列表
   # print('task_queue',task_queue)
    test_case_result=[]
    for x in task_queue['task_state_list']:
         update_state=task_management.objects.get(id=x[0])
         update_state.task_state=1
         update_state.save()
         report_data = {}  # 报告的json 对应的位置是 web_platform_my_report的report_data
         if x[3] == 0:
            completion_Success=0
            pass_case=0
            failure_case=0
            Collapse_case=0
          #  print(x[0],x[1],x[2],x[3],x[4])
            a_list=eval(x[5])
            case_total=len(a_list['case_list'])
          #  print('case_total',case_total)
            for y in a_list['case_list']:
                test_case_result_one={}
                case_one = my_case_of_API.objects.get(id=y)  # 根据 case表的id 查询case的信息，用于运行
                App_version=case_one.App_version
                try:
                    case_address=my_python_code_path+my_apicase_path+'.'+case_one.project_name+'.'+case_one.case_address+'.'+case_one.case_name
                    exec ('import  '+ case_address)
                    example=eval(case_address+'.API_case()')
                    running_result=example.test_case()
                    test_case_result_one = {"case_id": case_one.id, "module_name": case_one.module_name,
                                            'case_name': case_one.case_name, "api_name":case_one.api_name,
                                           }
                    test_case_result_one.update(running_result)
                    completion_Success=completion_Success+1
                except Exception as e:
                    test_case_result_one = {"case_id": case_one.id, "module_name": case_one.module_name,
                                            'case_name': case_one.case_name, "api_name": case_one.api_name,
                                            }
                    test_case_result_one.update({"result": -1, "error_info": '\'' + str(e) + '\''})


                finally:
                    if test_case_result_one["result"]==1:
                        pass_case=pass_case+1
                    elif test_case_result_one["result"]==0:
                        failure_case=failure_case+1
                    elif test_case_result_one["result"] == -1 :
                        Collapse_case=Collapse_case+1
                    test_case_result.append(test_case_result_one)

         report_data['test_case_result']=test_case_result
         report_data['platfor']=x[1]
         report_data['project']=x[2]
         report_data['completion_rate']= int(completion_Success/case_total*100) #终端完成率
         report_data['pass_tate']=int(pass_case/case_total*100)  #Case通过率
         report_data['failure_rate']=int(failure_case/case_total*100) #Case失败率
         report_data['Collapse_rate']=int(Collapse_case/case_total*100) #终端崩溃率
        # print(report_data)
        # print(report_data['pass_tate'],type(report_data['pass_tate']))
         if report_data['pass_tate']==100:
             report_result=1
         else:
             report_result=0
         now_report=my_report(user_name=web_user_name,report_data=report_data,report_result=report_result,uuid=uuid.uuid4(),App_name=x[2],terminal_number=1,test_type=x[1],App_version=App_version)
         now_report.save()
         update_state.task_state = 2
         update_state.save()



if __name__ == '__main__':
    while 1:
        run_api_case()
        time.sleep(10)










