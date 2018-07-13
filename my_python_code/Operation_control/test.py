import requests
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    while 1:
    #  a=time.time()
      requests.post('http://47.94.10.221:8000/rest_api/rest_api_tset_of_class', data={'1': '2'})
    #  print(time.time()-a)


if __name__=='__main__':
    print(1111)
    p = Pool()
    for i in range(50):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    p.join()
