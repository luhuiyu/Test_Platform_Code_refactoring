import threading
Lock = threading.Lock()


class Singleton(object):

    # 定义静态变量实例
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            Lock.acquire()
            try:
                # double check
                if not cls.__instance:
                    cls.__instance = super(Singleton, cls).__new__(cls)#(cls, args, kwargs) 原来的是这个参数
            finally:
                Lock.release()
        return cls.__instance



class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance