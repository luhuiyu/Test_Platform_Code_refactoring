from django import forms
from django.forms import widgets


class get_txt_api_form(forms.Form):
    case_id= forms.CharField(label='用例id(id)',max_length=200,widget=widgets.TextInput(attrs={'id': 'case_id', 'name': 'case_id','class':'form-control'}))
    project_name= forms.CharField(label='项目名(project_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'project_name', 'name': 'project_name','class':'form-control'}))
    text_module_name= forms.CharField(label='模块名(module_name)',max_length=200,widget=widgets.TextInput(attrs={'id': 'text_module_name', 'name': 'text_module_name','class':'form-control'}))
    case_name= forms.CharField(label='用例名(case_name)',max_length=800,widget=widgets.TextInput(attrs={'id': 'case_name', 'name': 'case_name','class':'form-control'}))
    operation_steps= forms.CharField(label='操作步骤(operation_steps)',max_length=800,widget=widgets.Textarea(attrs={'id': 'text_operation_steps', 'name': 'text_operation_steps','class':'form-control','rows':'5'}))
    expected_results= forms.CharField(label='预期结果(expected_results)',max_length=800,widget=widgets.Textarea(attrs={'id': 'expected_results', 'name': 'expected_results','class':'form-control','rows':'5'}))
    remarks= forms.CharField(label='备注(remarks)',max_length=800,widget=widgets.Textarea(attrs={'id': 'remarks', 'name': 'remarks','class':'form-control','rows':'5'}))
    App_version= forms.CharField(label='app版本(App_version)',max_length=200,widget=widgets.TextInput(attrs={'id': 'App_version', 'name': 'App_version','class':'form-control'}))
    script_type= forms.ChoiceField (label='脚本类型(script_type)',choices=((1,'api'),(2,'ui')),widget=widgets.Select(attrs={'id': 'script_type', 'name': 'script_type','class':'form-control'}))

 #   def __init__(self):
     #   forms.Form.__init__(self)









