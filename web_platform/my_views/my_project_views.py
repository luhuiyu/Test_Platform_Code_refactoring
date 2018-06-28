from django.shortcuts import render,HttpResponse
from web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.my_models.get_txet_case import get_case_text_dict
from  web_platform.my_models.get_api_case import get_case_api_dict
from  web_platform.my_models.get_ui_case import get_case_ui_dict

from  web_platform.models import  *

from django_ajax.decorators import ajax

def my_project(request):
    '''
    负责 home页面的处理
    :param request:
    :return:
    '''
    context_data=get_basic_data()
    context_data['get_text_case_form'] = get_text_case_form
    if request.method == 'GET':
        the_project_name = request.GET.get("the_project_name")
        context_data['the_project_name'] = the_project_name
        context_data=get_case_text_dict(context_data)
    elif request.method == 'POST':
        new_text_case=get_text_case_form(request.POST)
        if new_text_case.is_valid():
            new_text_case=new_text_case.clean()
            print(new_text_case)
            context_data['the_project_name'] = new_text_case['project_name']
            if new_text_case['text_case_id'] ==  '' :
                now_text_case_models = my_case_of_text(
                    project_name=new_text_case['project_name'],
                    module_name=new_text_case['text_module_name'],
                    case_name=new_text_case['text_case_name'],
                    operation_steps=new_text_case['operation_steps'],
                    expected_results=new_text_case['expected_results'],
                    remarks=new_text_case['remarks'],
                    App_version=new_text_case['App_version'],
                    script_type=new_text_case['script_type'],
                    script_address=new_text_case['script_address'],
                    revise_type=0,
                )
                now_text_case_models.save()
            else:
                now_text_case_models = my_case_of_text(
                    id=new_text_case['text_case_id'],
                    project_name=new_text_case['project_name'],
                    module_name=new_text_case['text_module_name'],
                    case_name=new_text_case['text_case_name'],
                    operation_steps=new_text_case['operation_steps'],
                    expected_results=new_text_case['expected_results'],
                    remarks=new_text_case['remarks'],
                    App_version=new_text_case['App_version'],
                    script_type=new_text_case['script_type'],
                    script_address=new_text_case['script_address'],
                    revise_type=1,
                )
                now_text_case_models.save()
            context_data = get_cast_text_dict(context_data)
    return render(request=request, template_name='my_project_html5.html', context=context_data)



def my_project_api_case(request):
    '''
    负责 api case 页面的处理
    :param request:
    :return:
    '''
    context_data = get_basic_data()
    if request.method == 'POST':
        the_project_name = request.POST.get("the_project_name")
        context_data['the_project_name'] = the_project_name
        context_data['get_api_case_form'] = get_api_case_form
        context_data=get_case_api_dict(context_data)
        return render(request=request, template_name='my_ajax_html5/my_project_api_case_ajax.html',
                      context=context_data)
    else:
        return render(request=request, template_name='my_ajax_html5/my_project_api_case_ajax.html')


def my_project_ui_case(request):
    context_data = get_basic_data()
    if request.method == 'POST':
        the_project_name = request.POST.get("the_project_name")
        context_data['the_project_name'] = the_project_name
        context_data['get_ui_case_form'] = get_ui_case_form
        context_data=get_case_ui_dict(context_data)
        return render(request=request, template_name='my_ajax_html5/my_project_ui_case_ajax.html',
                      context=context_data)
    else:
        return render(request=request, template_name='my_ajax_html5/my_project_ui_case_ajax.html')