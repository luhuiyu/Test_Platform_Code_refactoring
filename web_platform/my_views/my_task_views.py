from django.shortcuts import render,HttpResponseRedirect
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_models.get_my_task import *
import time
import uuid
from  web_platform.models import *

def my_task(request):
    context_data = get_basic_data()
    if request.method == 'GET' and request.GET.get('test_type')== 'apitest' :
        context_data=get_api_case_info(context_data)
        context_data["todaytime"] = str(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time())))
        return render(request=request, template_name='my_task_html5/my_task_api_html5.html', context=context_data)
    elif  request.method == 'GET' and request.GET.get('test_type')== 'uitest' :
        context_data["todaytime"] = str(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time())))
        context_data=get_ui_case_info(context_data)
        return render(request=request, template_name='my_task_html5/my_task_ui_html5.html', context=context_data)
    elif  request.method == 'POST' :
        selected_case=request.POST.getlist("selected_case")
        task_info=request.POST.get('task_info')
        todaytime = request.POST.get('todaytime')
        todaytime = str(todaytime).replace('T', ' ')
        task_info=eval(task_info)
        project_name=task_info['project_name']
        test_type=task_info['test_type']
        case_id_list = get_case_id_by_module_name_and_project_name(selected_case,test_type)
        task_management(task_project=project_name,
                        task_uuid=uuid.uuid4(),
                        task_state=0,
                        task_type=test_type,
                        task_data={'case_list': case_id_list},
                        create_time=todaytime).save()
        return HttpResponseRedirect('/task')
    else:
        context_data = get_task_queue(context_data)
        context_data = get_all_report(context_data)
        return render(request=request, template_name='my_task_html5.html', context=context_data)
