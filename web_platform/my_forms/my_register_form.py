from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

class my_register_form(forms.Form):
    user_name= forms.CharField(error_messages={'required':'用户名已存在'},label=False,max_length=10,widget=widgets.TextInput(attrs={'id': 'user_name', 'class': 'form-control','placeholder':'用户名'}))
    pass_word= forms.CharField(label=False,max_length=10,widget=widgets.TextInput(attrs={'id': 'pass_word', 'class': 'form-control','placeholder':'密码','type':"password"}))
    pass_word2= forms.CharField(label=False,max_length=10,widget=widgets.TextInput(attrs={'id': 'pass_word2', 'class': 'form-control','placeholder':'再次输入','type':"password"}))
    e_mail=forms.EmailField(error_messages={'required':'邮箱错误'}, label=False,widget=widgets.TextInput(attrs={'id': 'e_mail', 'class': 'form-control','placeholder':'e-mail'}) )

    def is_valid(self):
       '''
       重写 is_valid ,
       1.验证注册的用户是否已存在,
       2.验证两个密码在否相同

       self.add_error 用于添加 自定义的error
       原代码里面有相关的注释
       :return:
       '''
       try:
           #这里判断用户名是否重复
            new_user_name =self.data['user_name']
            if new_user_name:
               new_user=User.objects.filter(username=new_user_name)
               if len(new_user)>0:
                   self.add_error('user_name',"该用户名已注册")
            #这里判断两个密码是否相同
            new_pass_word_1 = self.data['pass_word']
            new_pass_word_2 = self.data['pass_word2']
            if new_pass_word_1 != new_pass_word_2 :
                self.add_error('pass_word2', "密码不一致，请重新输入")
       except:
           pass
       return self.is_bound and not self.errors

