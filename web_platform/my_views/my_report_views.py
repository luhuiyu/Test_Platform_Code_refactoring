from django.shortcuts import render
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_models.get_my_report import get_report,get_maxid
def my_report(request):
    context_data = get_basic_data()
    id = get_maxid()
    if request.method == 'GET':
            get_id = request.GET.get("id")
            if get_id:
                id=get_id
    elif request.method == 'POST':
            get_id = request.POST.get("id")
            if get_id:
                id=get_id
    context_data = get_report(context_data,id)
    #return render(request, 'report.html', context)
    return render(request=request, template_name='my_report_html5.html', context=context_data)
