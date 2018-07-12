from django.shortcuts import render,HttpResponse
from web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.my_models.get_txet_case import get_case_text_dict
from  web_platform.my_models.get_api_case import get_case_api_dict
from  web_platform.my_models.get_ui_case import get_case_ui_dict
from  web_platform.models import  *

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
            context_data = get_case_text_dict(context_data)
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
        return render(request=request, template_name='my_project_html5/my_project_api_case_ajax.html',
                      context=context_data)
    else:
        return render(request=request, template_name='my_project_html5/my_project_api_case_ajax.html')

def my_project_ui_case(request):
    context_data = get_basic_data()
    if request.method == 'POST':
        the_project_name = request.POST.get("the_project_name")
        context_data['the_project_name'] = the_project_name
        context_data['get_ui_case_form'] = get_ui_case_form
        context_data=get_case_ui_dict(context_data)
        return render(request=request, template_name='my_project_html5/my_project_ui_case_ajax.html',
                      context=context_data)
    else:
        return render(request=request, template_name='my_project_html5/my_project_ui_case_ajax.html')

def my_project_simple_case(request):
    context_data = get_basic_data()
    if request.method == 'POST':
        context_data['api_list']={}
        the_project_name = request.POST.get("the_project_name")
        the_api_name=request.POST.get("api_name")
        context_data['the_project_name'] = the_project_name
        if the_project_name :
            simple_case_data = comparison_library.objects.filter(project_name=the_project_name).values('api_name').distinct()
            api_list = []
            for y in simple_case_data:
                api_list.append(y)
            context_data['api_list'] = api_list
        if  the_api_name  and the_project_name :
            all_case = comparison_library.objects.filter(project_name=the_project_name,api_name=the_api_name).all()
            all_case_list = []
            for x in all_case:
                all_case_list.append(
                    {'id': x.id,  'remarks': x.remarks,
                     'api_name': x.api_name, 'project_name': x.project_name})
            context_data['all_case_value']=all_case_list
            context_data['the_api_name']=the_api_name
        context_data['get_simple_case_form'] = get_simple_case_form
        return render(request=request, template_name='my_project_html5/my_project_simple_case_ajax.html',
                      context=context_data)
    return render(request=request, template_name='my_project_html5/my_project_simple_case_ajax.html', context=context_data)
