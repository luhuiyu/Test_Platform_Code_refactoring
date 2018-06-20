from django.shortcuts import render,HttpResponse
from web_platform.my_forms.my_login_form import my_login_form
from django.contrib.auth import authenticate,login


def my_login(request):
    context_data={}
    context_data['my_login_form']=my_login_form
    if request.method == 'POST':
        the_my_login=my_login_form(request.POST)
        if the_my_login.is_valid():
            user_login_data=the_my_login.clean()
            user = authenticate(username=user_login_data['user_name'], password=user_login_data['pass_word'])
            if user is not None:
                login(request, user)  # 验证成功之后登录
                return render(request=request, template_name='head_html5.html', context=context_data)
        else:
            context_data['my_login_form'] = the_my_login
            return render(request=request, template_name='my_login_html5.html', context=context_data)
    return render(request=request, template_name='my_login_html5.html', context=context_data)