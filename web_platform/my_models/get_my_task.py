from  web_platform.models import *
import time
from django.utils import timezone


def get_all_report(context):
    all_report = my_report.objects.all().order_by("-id")[:10]
    report_list=[]
    for  a  in all_report:
        report_one=[]
        report_one.append(a.create_time)
        report_one.append(a.App_name)
        report_one.append(a.App_version)
        report_one.append(a.test_type)
        report_one.append(a.report_result)
        if int(a.report_result)==0:
            report_one.append('未通过')
        elif int(a.report_result)==1:
            report_one.append('通过')
        report_one.append(a.id)
        report_list.append(report_one)
    context['report_list']=report_list
    return context



def get_task_queue(context):
    get_now_task=task_management.objects.filter(task_state__lt=2).order_by("-id")[:5]
    print(get_now_task)
    task_all=[]
    for x in get_now_task:
        task_one=[]
        task_one.append(x.task_type)
        task_one.append(x.task_project)
        task_one.append(x.task_state)
        task_one.append(x.create_time)
        task_one.append(x.task_data)
        task_all.append(task_one)
    context['task_state_list'] = task_all
    return context

def  get_api_case_info(context):
        context['api_case_info']={}
        api_name_list=my_case_of_API.objects.values("module_name","project_name").distinct().order_by("project_name")
        all_api_info=[]
        for x in api_name_list:
            all_api_info.append(x)
        context['api_case_info'] = all_api_info
        return context


def get_ui_case_info(context):
    context['ui_case_info'] = {}
    ui_name_list = my_case_of_UI.objects.values("module_name", "project_name").distinct().order_by("project_name")
    all_ui_info = []
    for x in ui_name_list:
        all_ui_info.append(x)
    context['ui_case_info'] = all_ui_info
    return context




def  get_case_id_by_module_name_and_project_name(selected_case,test_type):

    case_id_list=[]
    if test_type == 'apitest':
        for x in selected_case :
            x=eval(x)
            my_case_db=my_case_of_API.objects.filter(module_name=x['module_name'],project_name=x['project_name'])
            for  y in my_case_db:
                case_id_list.append(y.id)
    elif   test_type == 'uitest':
        for x in selected_case :
            x=eval(x)
            my_case_db=my_case_of_UI.objects.filter(module_name=x['module_name'],project_name=x['project_name'])
            for  y in my_case_db:
                case_id_list.append(y.id)
    else:
        raise KeyError
    return  case_id_list





def get_task_queue_custom(context,task_type_custom,task_state_custom):
    now_time = timezone.now()
    get_now_task=task_management.objects.filter(task_type=task_type_custom,task_state=task_state_custom,create_time__lte=now_time).order_by("-id")
    #print(get_now_task)
    task_all=[]
    for x in get_now_task:
        task_one=[]
        task_one.append(x.id)
        task_one.append(x.task_type)
        task_one.append(x.task_project)
        task_one.append(x.task_state)
        task_one.append(x.create_time)
        task_one.append(x.task_data)
        task_one.append(x.task_uuid)
        task_all.append(task_one)
    context['task_state_list'] = task_all
    return context