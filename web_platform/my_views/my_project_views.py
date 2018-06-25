from django.shortcuts import render,HttpResponse
from web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.my_models.get_txet_case import get_cast_text_dict
def my_project(request):
    context_data=get_basic_data()
    context_data['get_txt_api_form']=get_txt_api_form
    if request.method == 'GET':
        the_project_name = request.GET.get("the_project_name")
        context_data['the_project_name'] = the_project_name
        context_data=get_cast_text_dict(context_data)
    return render(request=request, template_name='my_project_html5.html', context=context_data)