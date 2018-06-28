from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.models import *
from web_platform.my_settings import *


class source_case_file(APIView):
    '''
    查看api  case 文件的内容
    传进 case id
    返回  代码  文件地址
    '''
    def post(self, request, *args, **kwargs):
        source_case_info=get_request_data(self, request)
        if source_case_info['source_type'] == 'api':
            case_address=my_case_of_API.objects.get(id=source_case_info['source_id'])
            case_path=MY_PYTHON_CODE_PATH+'\\'+MY_API_CASE_PATH+'\\'+str(case_address.project_name)+'\\'+str(case_address.case_address).replace('.', '\\')+'\\'+str(case_address.case_name)+'.py'
        else:
            #source_case_info['source_type'] == 'ui':
            case_address=my_case_of_UI.objects.get(id=source_case_info['source_id'])
            case_path=MY_PYTHON_CODE_PATH+'\\'+MY_UI_CASE_PATH+'\\'+str(case_address.project_name)+'\\'+str(case_address.case_address).replace('.', '\\')+'\\'+str(case_address.case_name)+'.py'
        with open(case_path, encoding='utf-8') as f:
            case_code = f.read()
        return Response(data={'case_code': case_code, 'case_path': case_path}, status=200, template_name=None,headers=None, exception=False, content_type='json')