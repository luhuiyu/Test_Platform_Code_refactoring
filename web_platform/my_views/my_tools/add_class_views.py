from  my_python_code.tools.add_class import add_class
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.my_models.my_tools.get_add_class import get_course_code,get_course_name,get_record
import time
from django.contrib import messages
from django.shortcuts import render
from web_platform.models import add_class_record


def add_classes(request):
    context = get_basic_data()
    context=get_record(context)
    context['store_name'] = ['硬件测试专用店A','硬件测试专用店B','重庆江北区东原D7店','武汉江岸区航天双城店','西安融侨馨苑店','Seven店','上海亚都国际名园七星旗舰店','西安逸翠店','通州万达店','Rocky店','A店','B店','C店','D店','E店']
    context['user_number'] = range(1, 25)
    context['classes_checkin_number'] = range(1, 25)
    context['course_code'] = get_course_name()
    context['course_time'] = range(1, 38)
    context['now_time_day'] = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    context['now_time_h']=str(time.strftime('%H:%M',time.localtime(time.time())))
    print(context['now_time_day'])
    if request.method == 'POST':#if request.method == "POST" 空的也ok  if request.POST 不能是空的
        store_name=request.POST.get("store_name")
        print(store_name)
        day=request.POST.get("day")
        up_time=request.POST.get("up_time")
        course_code=request.POST.get("course_code")
        environment=request.POST.get("environment")
        user_number=request.POST.get("user_number")
        course_time=request.POST.get("course_time")
        user_index=request.POST.get("user_index")
        classes_checkin_number=request.POST.get("classes_checkin_number")
        timeArray = time.strptime(day+' '+up_time, "%Y-%m-%d %H:%M")
        star_time = time.mktime(timeArray)
        course_code_name=course_code
        course_code_list=get_course_code(course_code)
        subject_show_id=course_code_list[1]
        course_code=str(course_code_list[0])+str(course_time)
        class_id=add_class(star_time=star_time, store_name=store_name, user_number=user_number, classes_checkin_number=classes_checkin_number, course_code=course_code, subject_show_id=subject_show_id,dict_index=user_index,environment=environment)
        messages.add_message(request, messages.INFO, class_id)
        context['class_id'] = str(class_id)
        if class_id:
            context['ruesl'] = 'ok'
            add_class_record(create_time=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))),start_time=str(day+' '+up_time),class_id= str(class_id),course_code=course_code_name,store_name=store_name).save()
        else:
            context['ruesl'] = 'not'
            #messages.success(request,class_id)
      #  return render(request,'pop.html',context)
        context['class_id'] = class_id
        #return render(request, 'add_class.html', context)
   # else:
    return render(request,'my_tools_html5/add_class.html',context)