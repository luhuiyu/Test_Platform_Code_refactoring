from django import forms
from django.forms import widgets


class get_text_case_form(forms.Form):
    text_case_id= forms.CharField( required=False,label='用例id(id)',max_length=200,widget=widgets.TextInput(attrs={'id': 'text_case_id', 'name': 'text_case_id','class':'form-control'}))
    project_name= forms.CharField(label='项目名(project_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'project_name', 'name': 'project_name','class':'form-control'}))
    text_module_name= forms.CharField(label='模块名(module_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'text_module_name', 'name': 'text_module_name','class':'form-control'}))
    text_case_name= forms.CharField(label='用例名(case_name)',max_length=800,widget=widgets.TextInput(attrs={'id': 'text_case_name', 'name': 'text_case_name','class':'form-control'}))
    operation_steps= forms.CharField(label='操作步骤(operation_steps)',max_length=800,widget=widgets.Textarea(attrs={'id': 'text_operation_steps', 'name': 'text_operation_steps','class':'form-control','rows':'5'}))
    expected_results= forms.CharField(label='预期结果(expected_results)',max_length=800,widget=widgets.Textarea(attrs={'id': 'expected_results', 'name': 'expected_results','class':'form-control','rows':'5'}))
    remarks= forms.CharField(required=False,label='备注(remarks)',max_length=800,widget=widgets.Textarea(attrs={'id': 'remarks', 'name': 'remarks','class':'form-control','rows':'5'}))
    App_version= forms.CharField(required=False,label='app版本(App_version)',max_length=200,widget=widgets.TextInput(attrs={'id': 'App_version', 'name': 'App_version','class':'form-control'}))
#    script_type= forms.ChoiceField (label='脚本类型(script_type)',choices=((1,'api'),(2,'ui')),widget=widgets.Select(attrs={'id': 'script_type', 'name': 'script_type','class':'form-control'}))
    script_type= forms.CharField (required=False,label='脚本类型(script_type)',max_length=200,widget=widgets.TextInput(attrs={'id': 'script_type', 'name': 'script_type','class':'form-control'}))
    script_address=  forms.CharField (required=False,label='脚本地址(script_address)',max_length=200,widget=widgets.TextInput(attrs={'id': 'script_address', 'name': 'script_address','class':'form-control'}))
 #   def __init__(self):
     #   forms.Form.__init__(self)



class get_api_case_form(forms.Form):
    '''
    为了低耦合  不使用 modelForm
    '''
    api_case_id= forms.CharField( required=False,label='用例id(api_case_id)',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_case_id', 'name': 'api_case_id','class':'form-control api_case'}))
    api_project_name= forms.CharField(label='项目名(project_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_project_name', 'name': 'project_name','class':'form-control api_case' }))
    api_module_name= forms.CharField(label='模块名(api_module_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_module_name', 'name': 'api_module_name','class':'form-control api_case'}))
    api_name= forms.CharField(label='接口名(api_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_name', 'name': 'api_name','class':'form-control api_case'}))
    api_case_name= forms.CharField(label='api_case_name',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_case_name', 'name': 'api_case_name','class':'form-control api_case'}))
    api_case_address=forms.CharField(label='api_case_address',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_case_address', 'name': 'api_case_address','class':'form-control api_case'  }))
    api_App_version= forms.CharField(label='app版本(App_version)',max_length=200,widget=widgets.TextInput(attrs={'id': 'api_App_version', 'name': 'App_version','class':'form-control api_case ' }))
    my_case_of_text_id=  forms.CharField( required=False,label='my_case_of_text_id',max_length=200,widget=widgets.TextInput(attrs={'id': 'my_case_of_text_id', 'name': 'my_case_of_text_id','class':'form-control api_case'}))


class get_ui_case_form(forms.Form):
    ui_case_id = forms.CharField(required=False, label='用例id(ui_case_id)', max_length=200, widget=widgets.TextInput(attrs={'id': 'ui_case_id', 'name': 'ui_case_id', 'class': 'form-control api_case'}))
    ui_project_name = forms.CharField(label='项目名(project_name)', max_length=200, widget=widgets.TextInput(attrs={'id': 'ui_project_name', 'name': 'ui_project_name', 'class': 'form-control api_case'}))
    ui_module_name = forms.CharField(label='模块名(ui_module_name)', max_length=200, widget=widgets.TextInput(attrs={'id': 'ui_module_name', 'name': 'ui_module_name', 'class': 'form-control api_case'}))
    ui_case_name= forms.CharField(label='ui_case_name',max_length=200,widget=widgets.TextInput(attrs={'id': 'ui_case_name', 'name': 'ui_case_name','class':'form-control api_case'}))
    ui_case_address=forms.CharField(label='ui_case_address',max_length=200,widget=widgets.TextInput(attrs={'id': 'ui_case_address', 'name': 'ui_case_address','class':'form-control api_case'  }))
    ui_App_version= forms.CharField(label='app版本(App_version)',max_length=200,widget=widgets.TextInput(attrs={'id': 'ui_App_version', 'name': 'ui_App_version','class':'form-control api_case ' }))
    my_case_of_text_id=  forms.CharField( required=False,label='my_case_of_text_id',max_length=200,widget=widgets.TextInput(attrs={'id': 'my_case_of_text_id', 'name': 'my_case_of_text_id','class':'form-control api_case'}))



