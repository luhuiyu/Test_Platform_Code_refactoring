import  django.http.request

def  get_request_data(self, request, *args, **kwargs):
    if self.request.method =='POST':
         if  type(self.request.data) is dict:
             return self.request.data
         elif type(self.request.data) is django.http.request.QueryDict:
             return self.request.data.dict()
         else:
             raise TypeError
    elif  self.request.method =='GET':
             return self.request.GET.dict()