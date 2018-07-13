import  requests
import time
import json

data={'POST_L':'POST_LLLL'}
A=requests.post(url='http://127.0.0.1:8000/rest_api/rest_api_tset_of_class',json= data)
print(A.json())
print(A.status_code)
B=requests.get(url='http://127.0.0.1:8000/rest_api/rest_api_tset_of_class?the_project_name=111111')
print(B.json())
print(B.status_code)
