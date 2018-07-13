import re,time
import pymysql
import logging
import threading
from my_python_code.mysql.Basic_information import my_sql_link_test
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.info('添加课程')




def addclasses(user_name,user_uuid,mutex=None,add_time=None):
    #mutex = threading.Lock()  # 创建锁
    #mutex.acquire()  # 取得锁
    a=my_sql_link_test()
    enroll_number=len(user_uuid)
    db=a.db
    cursor=a.cursor
    start = time.time()
    end = time.time() + 3600
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))
    end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    if add_time:
            start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+int(add_time)))
            end = time.strftime('%Y-%m-%d %H:%M:%S',  time.localtime(time.time()+int(add_time)+3600))
    try:
        uuid=[]
        uuid=user_uuid

        class_number=len(uuid)

        if mutex:
            mutex.acquire()
        def get_gym_id(user_name):  # 获取gym_id
            user_name = str(user_name)
            sql = 'select gym_id from coach WHERE tel like \'' + user_name + '\''
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            gym_id = cursor.fetchone()
            gym_id = str(gym_id)
            gym_id = re.sub("\D", "", gym_id)  # 去除非数字
            return gym_id

        def input_to_user_classes(classes_id, n):
            classes_id = str(classes_id)
            n = int(n)
            if n > 15:
                return print('上课人数限制在15人以内')
            url = '\'' + classes_id + '\'' + ')'
            try:
               for x in uuid[0:n]:
                    x=str(x)
                    #print(x)
                    sql = 'INSERT IGNORE  INTO user_classes (subject_id,user_uuid,classes_type,STATUS,create_time,user_subject_uuid,classes_times,classes_id)VALUES (1474199922280448,\'' + x + '\',\'1\',\'0\',\''+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'\',\'bd89c9ce-c41b-4256-8fa1-5640a0a149d3\',\'8\',' + url
                    #print(sql)
                    cursor = db.cursor()
                    cursor.execute(sql)
                    db.commit()
                    logger.info('添加学员成功')
                    # print('添加学员成功')
            except:
               # print('没有成功添加用户')
                logger.info('没有成功添加用户')
                # db.commit()

        def input_to_classes_checkin(id, n):
            classes_id = str(id)
            n = int(n)
            if n > 15:
                return print('上课人数限制在15人以内')
            url = '\'' + classes_id + '\'' + ');'
            try:
                for x in uuid[0:n]:
                    #print(1)
                    x = str(x)
                    #print(x)
                    sql = 'INSERT IGNORE INTO user_classes_checkin (user_uuid,STATUS,create_time,coach_id,classes_id) VALUES (\'' + x + '\',\'1\',\'2016-10-09 14:16:32\',\'1429863157778432\',' + url
                    #print(sql)
                    cursor.execute(sql)
                    db.commit()
                    # print('学员签到成功')
            except:
                print('没有签到成功')
        def get_to_mysql():
            cursor.execute(str(sql)) #每取一次返回值就得重新查询
            if str(cursor.fetchall())=='()':
                return 0

        class_number=int(class_number)
        user_name=str(user_name)
        gym_id=get_gym_id(user_name)
        #print(gym_id)
        sql='select max(id) from subject WHERE gym_id =\''+gym_id+'\''
        cursor = db.cursor()
        cursor.execute(sql)
        #db.commit()

        subject_id=cursor.fetchone()
        subject_id=str(subject_id)
        subject_id=re.sub("\D", "",subject_id)   #去除非数字
        sql='select max(id) from coach WHERE gym_id='+'\''+gym_id+'\''
        #print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        #db.commit()
        coach_id=str(cursor.fetchone())
        coach_id=re.sub("\D", "",coach_id)
        class_sql='INSERT IGNORE INTO classes(subject_id, course_code, gym_id, coach_id,  start_time, end_time,TYPE, capacity,subject_show_id,enroll_number)VALUES('+'\''+subject_id+'\','+'\'BJ.1.0.1.1\','+'\''+gym_id+'\','+'\''+coach_id+'\','+'\''+start+'\','+'\''+end+'\','+'\'1\',\'12\',5,'+ str(enroll_number)+  ')'
        #print(class_sql)
        cursor.execute(class_sql)
        db.commit()
        sql='select MAX(id) from classes'   # WHERE start_time='+'\''+start+'\''
        cursor = db.cursor()
        cursor.execute(sql)
        #db.commit()
        id = cursor.fetchone()
        id = str(id)
        id=re.sub("\D", "",id)
        class_id=id
        #print(class_id)
        #print("添加的学员数量(0-15)")
        user_number=class_number
        #print("输入学员签到的数量（0-15）")
        classes_checkin_number=class_number
        if int(user_number)>0:
            input_to_user_classes(class_id,int(user_number))
        else:print("无学员")
        if int(classes_checkin_number)>0:
            input_to_classes_checkin(class_id,int(classes_checkin_number))
        else:print("无学员签到")
        db.commit()
        sql = 'select * from classes  where id=\'' + class_id + '\''
        while get_to_mysql()==0:
            time.sleep(0.1)

        db.commit()
        cursor.close()
        db.close()
        if mutex:
            mutex.release()
      #  mutex.release()  # 释放锁
        return class_id
    except:
        print('加课失败')

if __name__ == '__main__':
    uuid = ['85d47fad-a507-4ed6-8693-e9f64e8ad087',
            '4c73f62e-50df-4504-9a7a-925bcc2c7101',
            'ecbd60c2-c40f-49cc-aef7-fe62f947178d',
            '3e4d6e11-bb41-4ec9-b2f5-75c4d8b93ab0',
            '3588e0f6-da85-475d-9654-643f26e2d905',
            '915ab89d-4e86-48ae-b0bd-9b0212525d55',
            'd1aaa4cc-306f-472a-ae09-da32d32b18f3',
            '502623a7-8ce9-45ba-a6c4-60023f2d2500',
            '90a723e4-6f1d-4b14-b4b6-a716f00a5e64',
            'be37a6d70aaa444fa8a9b73ae82a505b',
            '3cada9f2-85cc-46be-a2b5-9b3a03276263',
            'f2cfb74b-e593-4a02-bdd3-49d09ef60ed1',

            ]

    addclasses(15600905550, uuid, add_time=1)








