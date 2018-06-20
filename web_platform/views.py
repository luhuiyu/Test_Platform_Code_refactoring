from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from web_platform.my_views import  *
def my_basics_html(request):
    return render(request, 'head_html5.html')
def my_login(request):
    return my_login_views.my_login(request)
def my_register(request):
    return my_register_views.my_register(request)
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('my_login')