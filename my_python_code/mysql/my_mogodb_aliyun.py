  # -*- coding:utf-8 -*-

import pymongo
from sshtunnel import SSHTunnelForwarder


def get_aliyun_mongo_client():
     # 跳板机参数
     ecs_host = "123.57.228.71"
     ecs_user = "dev"
     ecs_password = "Dev@KuaiKuai"

     aliyun_mongo_master_host = "dds-2ze37a86c2ea89e42.mongodb.rds.aliyuncs.com"
     aliyun_mongo_database = "admin"


     host =  aliyun_mongo_master_host
     server = SSHTunnelForwarder(
         (ecs_host, 22),
         ssh_password=ecs_password,
         ssh_username=ecs_user,
         remote_bind_address=(host, 3717))
     server.start()

     client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
     mongo_database = client[aliyun_mongo_database]
     mongo_database.authenticate("root", "Kuaimongodb001Kuai")

     return client


if __name__ == '__main__':
     mongo_client = get_aliyun_mongo_client()
     a=mongo_client["kk_buz"]["user_report_plus"].find({'uuid':'5d5a5a16-f893-4d1a-84b9-cc7057af462c'})
     print(a)
     mongo_client.close()