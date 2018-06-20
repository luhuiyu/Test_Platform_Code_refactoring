from django import forms
from django.forms import widgets
from django.contrib.auth import authenticate,login

class my_login_form(forms.Form):
    '''
    login 和register 分开创建foem，因为后期需要给登录添加验证码，还有别的功能。
    '''
    user_name= forms.CharField(label=False,max_length=10,widget=widgets.TextInput(attrs={'id': 'user_name', 'class': 'form-control','placeholder':'用户名'}))
    pass_word= forms.CharField(label=False,max_length=10,widget=widgets.TextInput(attrs={'id': 'pass_word', 'class': 'form-control','placeholder':'密码','type':"password"}))


    def is_valid(self):
        '''
        重写 is_valid
        添加 用户密码错误时返回一个error 信息。
        为了安全，不明确提示是账号不存在，还是密码不正确
        '''
        try:
            the_user_name = self.data['user_name']
            the_pass_word = self.data['pass_word']
            user = authenticate(username=the_user_name, password=the_pass_word)
            if user  is None :
                self.add_error('pass_word', "账号密码错误，请重新确认")
        except:
            pass

        return self.is_bound and not self.errors