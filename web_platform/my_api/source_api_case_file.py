from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.models import *
from web_platform.my_settings import *


class source_api_case_file(APIView):
    def post(self, request, *args, **kwargs):
        api_case_id=get_request_data(self, request)
        case_address=my_case_of_API.objects.get(id=api_case_id['source_id'])
        api_case_path=MY_PYTHON_CODE_PATH+'\\'+MY_API_CASE_PATH+'\\'+str(case_address.project_name)+'\\'+str(case_address.case_address).replace('.', '\\')+'\\'+str(case_address.case_name)+'.py'
        with open(api_case_path, encoding='utf-8') as f:
            case_code = f.read()
        return Response(data={'case_code':case_code,'api_case_path':api_case_path},status=200, template_name=None, headers=None, exception=False, content_type='json')