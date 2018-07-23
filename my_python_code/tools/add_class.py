import re,time
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link_stage
from my_python_code.basic_configuration.configuration_file import *

def add_class(star_time,store_name,user_number,classes_checkin_number,course_code,subject_show_id,user_uuid_list=False,dict_index='3',coach_phone=None,end_time=None,environment='test'):
    if environment=='state':
        a=my_sql_link_stage()
    else:
        a = my_sql_link_test()
    db = a.db
    cursor = a.cursor
    if end_time == None:
        end_time=star_time+3600
    else:
        end_time= time.time()+end_time
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(star_time))
    end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

    if user_uuid_list == False:
        uuid =uuid_idct[dict_index]
    else:
        uuid=user_uuid_list
  #  print(uuid)
    def get_gym_id(user_name,cursor=cursor,db=db):  # 获取gym_id
        user_name = str(user_name)
        sql = 'select gym_id from coach WHERE tel like \'' + user_name + '\''
       # print(sql)
        cursor.execute(sql)
        db.commit()
        gym_id = cursor.fetchone()
        gym_id = str(gym_id)
        gym_id = re.sub("\D", "", gym_id)  # 去除非数字
      #  print(gym_id)
        return gym_id
    def gymid(store_name):  # 获取gym_id
        if store_name == '':
            store_name = '通'
        sql = 'select id from gym WHERE name LIKE \'%' + store_name + '%\''
     #   print(sql)
        cursor.execute(sql)
        db.commit()
        gym_id = cursor.fetchone()
        gym_id = str(gym_id)
        gym_id = re.sub("\D", "", gym_id)  # 去除非数字
     #   print(gym_id)
        return gym_id

    try:
        if coach_phone == None:
            gym_id=gymid(store_name)
        else:
            gym_id=get_gym_id(coach_phone)
        # print(gym_id)
        sql = 'select min(id) from subject WHERE gym_id =\'' + gym_id + '\''
        cursor.execute(sql)
        # db.commit()
        subject_id = cursor.fetchone()
        subject_id = str(subject_id)
        subject_id = str(re.sub("\D", "", subject_id) ) # 去除非数字
        sql = 'select max(id) from coach WHERE gym_id=' + '\'' + gym_id + '\''
        cursor.execute(sql)
        # db.commit()
        coach_id = str(cursor.fetchone())
        coach_id = re.sub("\D", "", coach_id)
        class_sql='INSERT IGNORE INTO classes(subject_id, course_code, gym_id, coach_id,  start_time, end_time,TYPE, capacity,subject_show_id)VALUES('+'\''+str(subject_id)+'\','+'\''+course_code+'\','+'\''+str(gym_id)+'\','+'\''+coach_id+'\','+'\''+start+'\','+'\''+end+'\','+'\'1\',\'12\','+str(subject_show_id)+')'
   #     print(class_sql)
        cursor.execute(class_sql)
        # db.commit()
    except Exception as e:
        print('添加课程未成功',e)
    try:
        sql = 'select MAX(id) from classes'
        cursor.execute(sql)
        # db.commit()
        id = cursor.fetchone()
        id = str(id)
        id = re.sub("\D", "", id)
    except:
        print('排序失败')


    def input_to_user_classes(classes_id, n):
        classes_id = str(classes_id)
        n = int(n)
        if n > 24:
            return print('上课人数限制在24人以内')
        url = '\'' + classes_id + '\'' + ')'
        #try:
        for x in uuid[0:n]:
            sql = 'INSERT IGNORE  INTO user_classes (subject_id,user_uuid,classes_type,STATUS,create_time,user_subject_uuid,classes_times,classes_id)VALUES (\'1474199922280448\',\'' + x + '\',\'1\',\'0\',\''+start+'\',\'bd89c9ce-c41b-4256-8fa1-5640a0a149d3\',\'8\',' + url
            cursor.execute(sql)
          #  print(sql)
     #   print('添加学员成功')
       # except:
         #   print('没有成功添加用户')

            # db.commit()

    def input_to_classes_checkin(id, n):
        classes_id = str(id)
        n = int(n)
        if n > 24:
            return print('上课人数限制在24人以内')

        url = '\'' + classes_id + '\'' + ');'
        try:
            for x in uuid[0:n]:
                sql = 'INSERT IGNORE INTO user_classes_checkin (user_uuid,STATUS,create_time,coach_id,classes_id) VALUES (\'' + x + '\',\'1\',\''+start+'\',\'1429863157778432\',' + url
                cursor.execute(sql)
               # print(sql)
           # print('学员签到成功')
        except:
            print('没有签到成功')
            # db.commit()

    #try:
    class_id = id
    #print("添加的学员数量(0-15)")
    if user_number == '':
        user_number = 9
   # print("输入学员签到的数量（0-15）")
    if classes_checkin_number == '':
        classes_checkin_number = 9
    if int(user_number) > 0:
        input_to_user_classes(class_id, int(user_number))
    else:
        print("无学员")
    if int(classes_checkin_number) > 0:
        input_to_classes_checkin(class_id, int(classes_checkin_number))
    else:
        print("无学员签到")
    #except:
    #    print('未能添加学员')
    db.commit()
    return id
if __name__=='__main__':

    print(add_class(time.time()+300, 'seven', 12, 12, 'JXSXBJ1.0.1.1', subject_show_id=9, dict_index='4', coach_phone=15600905550,environment='stage'))


