from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.models import *


class delete_case(APIView):
    '''
    用于删除case ，post json结构
    { 'id' :id  ,'case_type':'text'}
    case_type   text  api ui
    '''
    def post(self, request, *args, **kwargs):
        delete_case_info=get_request_data(self, request)
        delete_case_info=eval(delete_case_info['delete_case_data'])
        if delete_case_info['case_type'] == 'text':
            my_case_of_text.objects.filter(id=int(delete_case_info['id'])).delete()
        elif delete_case_info['case_type'] == 'api':
            my_case_of_API.objects.filter(id=int(delete_case_info['id'])).delete()
        elif delete_case_info['case_type'] == 'ui':
            my_case_of_UI.objects.filter(id=int(delete_case_info['id'])).delete()
        elif delete_case_info['case_type'] == 'simple':
            comparison_library.objects.filter(id=int(delete_case_info['id'])).delete()
        return Response(status=200, template_name=None, headers=None,exception=False, content_type='json')