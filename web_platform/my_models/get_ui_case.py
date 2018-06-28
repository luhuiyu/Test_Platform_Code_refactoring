from  web_platform.models import  my_case_of_UI

def get_case_ui_dict(context_data):
    '''
    返回 当前项目的ui_case数据，json格式
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
    context_data['ui_case_list'] = {}
    case_of_ui_dict = {}
    for x in my_case_of_UI.objects.filter(project_name=context_data['the_project_name']).values(
            'module_name').distinct():
        case_of_ui_list = []
        for y in my_case_of_UI.objects.filter(project_name=context_data['the_project_name'],
                                                module_name=x['module_name']).all():
            case_of_ui_list.append(
                {
                    'id': y.id,
                    'project_name': y.project_name,
                    'module_name': y.module_name,
                    'case_name': y.case_name,
                }
            )
        case_of_ui_dict[x['module_name']] = case_of_ui_list
    context_data['ui_case_list'] = case_of_ui_dict
    return context_data