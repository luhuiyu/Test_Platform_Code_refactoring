from web_platform.my_models.my_devices_phone import get_devices_info_Android
from web_platform.my_models.my_devices_phone import get_devices_info
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.models import devices_phone
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
@login_required
def devices_phone_views(request):
    context = get_basic_data()
    if request.method == 'POST':
        renew=request.POST.getlist("renew")
        Android_devices_list = request.POST.getlist("Android")
        iOS_devices_list = request.POST.getlist("iOS")
        if  renew:
            devices_phone.objects.filter().delete()
            get_devices_info_Android()  # 本机使用这个更新数据库的连接信息

        if Android_devices_list:
            devices_phone.objects.filter(platformName='Android').update(used=0)
            for uid in Android_devices_list:
                devices_phone.objects.filter(deviceName=uid).update(used='1')
        elif iOS_devices_list:
            devices_phone.objects.filter(platformName='iOS').update(used=0)
            for uid in iOS_devices_list:
                devices_phone.objects.filter(deviceName=uid).update(used='1')

        context['Android'] = get_devices_info('Android')
        context['iOS'] = get_devices_info('iOS')
        return HttpResponseRedirect('/task')
    else:
        context['Android'] = get_devices_info('Android')
        context['iOS'] = get_devices_info('iOS')
        return render(request, 'my_devices_phone_html5.html', context)
