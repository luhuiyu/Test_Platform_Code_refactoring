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
    path(r'report', my_report_views.my_report, name='my_project'),
    path(r'task', my_task_views.my_task, name='my_task'),
    path(r'my_project_api_case', my_project_views.my_project_api_case, name='my_project_api_case'),
    path(r'my_project_ui_case', my_project_views.my_project_ui_case, name='my_project_ui_case'),
    path(r'my_project_simple_case', my_project_views.my_project_simple_case, name='my_project_simple_case'),
    path(r'rest_api/get_tools_list_api', get_tools_list_api.get_tools_rest_api.as_view(), name='get_tools_list_api'),
    path(r'rest_api/get_text_case_rest_api', get_text_case_data_api.get_text_case_rest_api.as_view(), name='get_text_case_rest_api'),
    path(r'rest_api/get_text_case_data_api', get_api_case_data_api.get_api_case_data_api.as_view(),name='get_api_case_rest_api'),
    path(r'rest_api/get_ui_case_data_api', get_ui_case_data_api.get_ui_case_data_api.as_view(),name='get_ui_case_data_api'),
    path(r'rest_api/get_simple_case_data_api', get_simple_case_data_api.get_simple_case_data_api.as_view(),name='get_simple_case_data_api'),
    path(r'rest_api/delete_case_api', delete_case_api.delete_case.as_view(),name='delete_case_api'),
    path(r'rest_api/source_case_file', source_case_file.source_case_file.as_view(), name='source_case_file'),
    path(r'rest_api/save_api_case_api', save_api_case_api.save_api_case_api.as_view(),name='save_api_case_api'),
    path(r'rest_api/save_ui_case_api', save_ui_case_api.save_ui_case_api.as_view(), name='save_ui_case_api'),
    path(r'rest_api/save_simple_case_api', save_simple_case_api.save_simple_case_api.as_view(), name='save_simple_case_api'),
    path(r'rest_api/save_api_case_file_api', save_api_case_file_api.save_api_case_file_api.as_view(), name='save_api_case_file_api'),


]
