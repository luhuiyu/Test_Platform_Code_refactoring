from simple_mysql_splice import simple_splice
config = {
        'pool_name': 'local',
        'host': '192.168.41.27',
        'port': 33061,
        'user': 'root',
        'password': '123456',
        'database': 'test_platform'}
instance=simple_splice(config)


print(instance.TABLE('auth_user').SELECT('id').WHERE(id=1).EXECUTE_ALL())