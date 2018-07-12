from django.shortcuts import render,HttpResponse
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.models import *
import time
def index_views(request):
    context_data = get_basic_data()
    context_data["my_case_of_text_total"]= my_case_of_text.objects.count()
    context_data["my_case_of_api_total"]=my_case_of_API.objects.count()
    context_data["my_case_of_ui_total"]=my_case_of_UI.objects.count()
    context_data['my_project_total']=my_report.objects.count()
    daily_report=[]
    for x in range(10):
        up_time = str(time.strftime('%Y-%m-%d', time.localtime(time.time() - x * 86400))) + ' 23:59:59'
        dow_time = str(time.strftime('%Y-%m-%d', time.localtime(time.time() - x * 86400))) + ' 00:00:01'
        moonday = time.strftime('%Y-%m-%d', time.localtime(time.time() - x * 86400))
        report_total = my_report.objects.filter(create_time__gt=dow_time,create_time__lt=up_time).count()
        pass_report_total = my_report.objects.filter(create_time__gt=dow_time,create_time__lt=up_time,report_result=1).count()
        failure_report_total =my_report.objects.filter(create_time__gt=dow_time,create_time__lt=up_time,report_result=0).count()
        daily_report.append({'moonday': '\'' + moonday + '\'', 'report_total': int(report_total),
                             'pass_report_total': int(pass_report_total),
                             'failure_report_total': int(failure_report_total)})
        context_data['daily_report']=daily_report
    return render(request, 'my_index_html5.html', context_data)
