from django.shortcuts import render,HttpResponseRedirect
from  web_platform.my_models.get_basic_data import get_basic_data


def set_up(request):
    context_data=get_basic_data()
    return render(request=request, template_name='my_set_up_html5.html', context=context_data)
