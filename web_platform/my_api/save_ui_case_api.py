from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import *
from web_platform.my_api.basic_api import get_request_data
from  web_platform.my_forms.my_project_form import *
from  web_platform.models import  *
class save_ui_case_api(APIView):
    '''
    保存 ui case 有两种情况
    修改已有case,则from里面有 id
    反之新建case则没有.
    '''
    def post(self,request, *args, **kwargs):
   #     A=get_request_data(self, request)
        new_ui_case=get_ui_case_form(request.POST)
        if new_ui_case.is_valid():
            new_ui_case=new_ui_case.clean()
            if new_ui_case['ui_case_id'] == '':
                my_case_of_UI(
                    project_name=new_ui_case['ui_project_name'],
                    module_name=new_ui_case['ui_module_name'],
                    case_name=new_ui_case['ui_case_name'],
                    case_address=new_ui_case['ui_case_address'],
                    App_version=new_ui_case['ui_App_version'],
                    my_case_of_text_id=new_ui_case['my_case_of_text_id'],
                ).save()
            else:
                my_case_of_UI(
                    id=new_ui_case['ui_case_id'],
                    project_name=new_ui_case['ui_project_name'],
                    module_name=new_ui_case['ui_module_name'],
                    case_name=new_ui_case['ui_case_name'],
                    case_address=new_ui_case['ui_case_address'],
                    App_version=new_ui_case['ui_App_version'],
                    my_case_of_text_id=new_ui_case['my_case_of_text_id'],
                ).save()

        return Response(  status=200, template_name=None, headers=None,
                        exception=False, content_type='json')