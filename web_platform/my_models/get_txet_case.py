from  web_platform.models import  my_case_of_text

def get_case_text_dict(context_data):
    '''
    返回 当前项目的case数据，json格式
    {   module_name1：{
            {case_data1},{case_data2},
        },
        module_name2：{
            {case_data1},{case_data2},
        }
    }
    传进来的 context 里 context['the_project_name'] 不为空
    :param context:
    :return:
    '''
    context_data['text_case_list']={}
    case_of_text_dict={}
    for x in  my_case_of_text.objects.filter(project_name=context_data['the_project_name'] ).values('module_name').distinct():
        case_of_text_list = []
        for y in my_case_of_text.objects.filter(project_name=context_data['the_project_name'],module_name=x['module_name']).all():
               case_of_text_list.append(
                   {
                       'id': y.id,
                       'project_name': y.project_name,
                       'module_name': y.module_name,
                       'case_name': y.case_name,
                       'sign': y.sign
                   }
               )
        case_of_text_dict[x['module_name']]=case_of_text_list
    context_data['case_of_text_dict']=case_of_text_dict
    return context_data