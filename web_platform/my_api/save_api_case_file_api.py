from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.models import *
from web_platform.my_settings import *

class save_api_case_file_api(APIView):
    def post(self, request, *args, **kwargs):
        api_case_data = get_request_data(self, request)
        case_data=api_case_data['case_code']
        case_data = case_data.replace('\r\n\r\n', '\r')  # 很重要，不知道为什么保存的时候会有换行符
        case_data = case_data.replace('\r\n', '\r')
        with open(api_case_data['updata_api_case'], 'w', encoding='utf-8') as f:
            f.writelines(case_data)
        return Response(status=200, template_name=None, headers=None, exception=False, content_type='json')



'''


    '''