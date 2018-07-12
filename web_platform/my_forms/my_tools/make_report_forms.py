from django import forms
class make_report_forms(forms.Form):
    class_id =  forms.IntegerField()
    course_code = forms.CharField(max_length=30)
    course_time = forms.IntegerField()
    user_index=  forms.IntegerField()
