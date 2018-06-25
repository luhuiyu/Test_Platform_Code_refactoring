from rest_framework.views import APIView
from rest_framework.response import Response
from web_platform.models import my_tools
class get_tools_rest_api(APIView):
    '''
    这个接口用于获取tools表里面的数据.
    留着以后用
    '''
    def get(self, request, *args, **kwargs):
        tools_list=[]
        for tool in  my_tools.objects.all():
            tools_list.append({'tools_name':tool.tools_name,'tools_address':tool.tools_address,'tools_id':tool.id})
        return Response(data={'tools_list':tools_list},status=200 ,template_name=None, headers=None,
                 exception=False, content_type='json')
    def post(self, request, *args, **kwargs):
        tools_list = []
        for tool in my_tools.objects.all():
            tools_list.append({'tools_name': tool.tools_name, 'tools_address': tool.tools_address,'tools_id':tool.id})
        return Response({ 'tools_list': tools_list},status=200, template_name=None, headers=None,
                 exception=False, content_type='json')