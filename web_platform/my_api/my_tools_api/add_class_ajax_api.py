from django.shortcuts import render
from  web_platform.models import course
from django_ajax.decorators import ajax

@ajax
def get_subject_total(request):
    '''
    这个接口用于接收 course_code，返回该course_code对应的课程总数
    :param request:
    :return:
    '''
   # if request.is_ajax() :
    if  request.method == 'POST' :
        course_code = request.POST['course_code']
        if course_code:
            print(course_code)
            AA=course.objects.get(name=course_code)
            list_course=range(1,int(AA.subject_total)+1)
           # return JsonResponse({'subject_total':int(subject_total)})
            return render(request, 'my_tools_html5/add_class_subject_total.html', {'subject_total':list_course })
    return render(request, 'my_tools_html5/add_class_subject_total.html', {'subject_total': 12})
