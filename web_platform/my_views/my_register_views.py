from django.shortcuts import render,HttpResponse
from web_platform.my_forms.my_register_form import my_register_form
from django.contrib.auth.models import User
from web_platform.my_models.get_basic_data import get_basic_data
from django.contrib.auth.decorators import login_required



def my_register(request):
    '''
    用于处理注册的逻辑，
    有一个对应的表单 my_register_form
    :param request:
    :return:
    '''
    context_data=get_basic_data()
    context_data['my_register_form'] = my_register_form
    if request.method == 'POST':
        the_my_register = my_register_form(request.POST)
        if the_my_register.is_valid():
            '''
            form 里面 重写了 is_valid ,用于判断新用户是否符合规则
              1.注册的用户是否已存在,
              2.两个密码在否相同
            所以先调用is_valid ，再clean
            '''
            new_user_data = the_my_register.clean()
            new_user=User.objects.create_user(username=new_user_data['user_name'], email=new_user_data['e_mail'], password=new_user_data['pass_word'])
            new_user.save()
        else:
            print(the_my_register.errors)
            context_data['my_register_form']=the_my_register
            return render(request=request, template_name='my_register_html5.html', context=context_data)
    return render(request=request, template_name='my_register_html5.html', context=context_data)