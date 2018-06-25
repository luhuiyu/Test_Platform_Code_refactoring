'''
用于获取
1.tools_list
2.project_list
'''
from web_platform.models import my_project
from web_platform.models import my_tools

def get_basic_data():
    context={}
    context['my_project'] = get_my_project()
    context['my_tools']=get_tools_list()
    return context


def get_tools_list():
    tools=my_tools.objects.filter()
    tools_list=[]
    for x in tools:
        one_tools={}
        one_tools['tools_name']=x.tools_name
        one_tools['tools_address']=x.tools_address
        one_tools['id']=x.id
        tools_list.append(one_tools)
    return  tools_list


def get_my_project():
    '''
    获取当前的项目列表
    :return:
    '''
    conn=my_project.objects.filter()
    project_list=[]
    for x in conn:
        one_project={}
        one_project['project_name']=x.project_name
        one_project['project_address']=x.project_address
        one_project['id']=x.id
        project_list.append(one_project)
    return  project_list