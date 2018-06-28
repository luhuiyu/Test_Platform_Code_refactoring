from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
class get_api_case_data_api(APIView):
    '''
    这个接口用于获取api_case的数据，通过id
    只允许post
    '''
    def post(self, request, *args, **kwargs):
        get_data = get_request_data(self, request)
        id=get_data['id']
        case_data=my_case_of_API.objects.get(id=id)
        return_dict={
            'case_id':case_data.id,
            'project_name':case_data.project_name,
            'module_name':case_data.module_name,
            'api_name':case_data.api_name,
            'case_name':case_data.case_name,
            'case_address':case_data.case_address,
            'App_version':case_data.App_version,
            'my_case_of_text_id':case_data.my_case_of_text_id,
        }
        return Response(return_dict,status=200, template_name=None, headers=None,
                 exception=False, content_type='json')