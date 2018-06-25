"""Test_Platform_Code_refactoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_platform.views import *
from web_platform.my_api import *
from  web_platform.my_views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'head', my_basics_html, name='head'),
    path(r'my_login', my_login, name='my_login'),
    path(r'logout', logout, name='logout'),
    path(r'my_register', my_register, name='my_register'),
    path(r'project', my_project_views.my_project, name='my_project'),
    path(r'rest_api/get_tools_list_api', get_tools_list_api.get_tools_rest_api.as_view(), name='get_tools_list_api'),
    path(r'rest_api/get_text_case_rest_api', get_text_case_data_api.get_text_case_rest_api.as_view(), name='get_text_case_rest_api'),


]
