from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
class get_simple_case_data_api(APIView):
    '''
    这个接口用于获取simple_case的数据，通过id
    只允许post
    '''
    def post(self, request, *args, **kwargs):
        get_data = get_request_data(self, request)
        id=get_data['id']
        case_data=comparison_library.objects.get(id=id)
        return_dict={
            'case_id':case_data.id,
            'api_name':case_data.api_name,
            'send_json':case_data.send_json,
            'receive_json':case_data.receive_json,
            'status_code':case_data.status_code,
            'remarks':case_data.remarks,
            'project_name':case_data.project_name,
        }
        return Response(return_dict,status=200, template_name=None, headers=None,
                 exception=False, content_type='json')