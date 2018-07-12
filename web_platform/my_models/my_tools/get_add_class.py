from web_platform.models import *
def get_course_name():
    a = course.objects.filter()
    course_code_list=[]
    for x in a:
        course_code_list.append(x.name)
    return course_code_list
def get_course_code(name):
    a = course.objects.filter(name=name)
    course_code_list=[]
    for x in a:
        course_code_list.append(x.course_code)
        course_code_list.append(x.subject_show_id)
    return course_code_list
def get_record(context):
    context['class_id_record']=[]
    all_dict=[]
    all_list=add_class_record.objects.all().order_by("-id")[:10]
    for x in  all_list:
        one_dict = {'id':x.id,'create_time':x.create_time,'start_time':x.start_time,'class_id':x.class_id,'course_code':x.course_code,'store_name':x.store_name}
        all_dict.append(one_dict)
    context['class_id_record']= all_dict
    return context

