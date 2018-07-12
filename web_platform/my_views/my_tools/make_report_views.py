from  my_python_code.tools.add_class import add_class
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.my_models.my_tools.get_add_class import get_course_code,get_course_name
import time
from my_python_code.tools.make_report import make_report
from django.contrib import messages
from django.shortcuts import render
from web_platform.my_forms.my_tools.make_report_forms import make_report_forms
def make_rerort(request):

    context = get_basic_data()
    context['course_code'] = get_course_name()
    context['course_time'] = range(1, 12)
    try:
        if request.method == 'POST':#if request.method == "POST" 空的也ok  if request.POST 不能是空的
            '''
            course_code=request.POST.get("course_code")
            course_time = request.POST.get("course_time")
            class_id=request.POST.get("class_id")
            '''
            add_report_data=make_report_forms(request.POST)
            if add_report_data.is_valid():
                #print(add_report_data)
                course_code_list=get_course_code(add_report_data.clean()['course_code'])
                subject_show_id=course_code_list[1]
                course_code=str(course_code_list[0])+str(add_report_data.clean()['course_time'])
                report_url=make_report(add_report_data.clean()['class_id'], course_code, subject_show_id, dict_index=str(add_report_data.clean()['user_index']), user='15600905550',password='123456')['classReportList']
                context['report_url_data'] = report_url
                if report_url:
                    context['ruesl'] = 'ok'
                    context['buz_class_id']=add_report_data.clean()['class_id']
                else:
                    context['ruesl'] = 'not'
            else:
                print(add_report_data.errors.as_json())
    except:
        context['ruesl'] = 'not'
    return render(request,'my_tools_html5/make_rerort.html',context)