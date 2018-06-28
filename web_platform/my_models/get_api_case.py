from  web_platform.models import  my_case_of_API

def get_case_api_dict(context_data):
    '''
    返回 当前项目的api_case数据，json格式
    {   module_name1：{
            {case_data1},{case_data2},
        },
        module_name2：{
            {case_data1},{case_data2},
        }
    }
    只传部分数据，表的部分数据
    传进来的 context 里 context['the_project_name'] 不为空
    :param context_data:
    :return:
    '''
    context_data['api_case_list'] = {}
    case_of_api_dict = {}
    for x in my_case_of_API.objects.filter(project_name=context_data['the_project_name']).values(
            'module_name').distinct():
        case_of_api_list = []
        for y in my_case_of_API.objects.filter(project_name=context_data['the_project_name'],
                                                module_name=x['module_name']).all():
            case_of_api_list.append(
                {
                    'id': y.id,
                    'project_name': y.project_name,
                    'module_name': y.module_name,
                    'case_name': y.case_name,
                    'api_name':y.api_name
                }
            )
        case_of_api_dict[x['module_name']] = case_of_api_list
    context_data['api_case_list'] = case_of_api_dict
    return context_data