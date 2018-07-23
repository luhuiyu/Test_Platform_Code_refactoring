import  pymongo


def  my_mogodb_test():
    test_client = pymongo.MongoClient("192.168.40.207:27017")
    test_client.authenticate("root", "Kuaimongodb001Kuai")
    return test_client