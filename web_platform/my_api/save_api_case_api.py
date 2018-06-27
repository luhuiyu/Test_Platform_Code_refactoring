from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.models import  *
class save_api_case_api(APIView):
    def post(self,request, *args, **kwargs):
   #     A=get_request_data(self, request)
        new_api_case=get_api_case_form(request.POST)
        if new_api_case.is_valid():
            new_api_case=new_api_case.clean()
            if new_api_case['api_case_id'] == '':
                my_case_of_API(
                    project_name=new_api_case['api_project_name'],
                    module_name=new_api_case['api_module_name'],
                    api_name=new_api_case['api_name'],
                    case_name=new_api_case['api_case_name'],
                    case_address=new_api_case['api_case_address'],
                    App_version=new_api_case['api_App_version'],
                    my_case_of_text_id=new_api_case['my_case_of_text_id'],
                ).save()
            else:
                my_case_of_API(
                    id=new_api_case['api_case_id'],
                    project_name=new_api_case['api_project_name'],
                    module_name=new_api_case['api_module_name'],
                    api_name=new_api_case['api_name'],
                    case_name=new_api_case['api_case_name'],
                    case_address=new_api_case['api_case_address'],
                    App_version=new_api_case['api_App_version'],
                    my_case_of_text_id=new_api_case['my_case_of_text_id'],
                ).save()

        return Response(  status=200, template_name=None, headers=None,
                        exception=False, content_type='json')