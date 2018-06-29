from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.models import  *
class save_simple_case_api(APIView):
    '''
       保存 simple case 有两种情况
       修改已有case,则from里面有 id
       反之新建case则没有.
       '''

    def post(self, request, *args, **kwargs):
        #     A=get_request_data(self, request)
        new_simple_case = get_simple_case_form(request.POST)
        if new_simple_case.is_valid():
            new_simple_case=new_simple_case.clean()
            if new_simple_case['simple_case_id']:
                comparison_library(
                    id=new_simple_case['simple_case_id'],
                    api_name=new_simple_case['simple_api_name'],
                    send_json=new_simple_case['simple_send_json'],
                    receive_json=new_simple_case['simple_receive_json'],
                    status_code=new_simple_case['simple_status_code'],
                    remarks=new_simple_case['simple_remarks'],
                    project_name=new_simple_case['simple_name'],
                ).save()
            else:
                comparison_library(
                    api_name=new_simple_case['simple_api_name'],
                    send_json=new_simple_case['simple_send_json'],
                    receive_json=new_simple_case['simple_receive_json'],
                    status_code=new_simple_case['simple_status_code'],
                    remarks=new_simple_case['simple_remarks'],
                    project_name=new_simple_case['simple_name'],
                ).save()
        return Response(status=200, template_name=None, headers=None,
                        exception=False, content_type='json')