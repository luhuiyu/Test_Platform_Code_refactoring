import requests

A=requests.get(url='http://test.kuaikuaikeji.com/kcas/appcheck21?build=20454')
print(A.json())