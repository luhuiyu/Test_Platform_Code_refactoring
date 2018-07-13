#基础数据，所有的变量都要通过这里取得
import time
####API的地址
main_url='http://test.kuaikuaikeji.com/kcas/'
json_url='http://192.168.41.41/KKNewReport/PadGetUUIDUserReportV3?i='
user_phone='15600905550'
password='123456'
beginDate=int(time.time()*1000)  #获取当前时间戳
coachId=1429863157778432  #教练的id
userCode=100230 #用户id
##获取报告列表的
listRange=0  
listSort=0
pageIndex=0
pageSize=100
####用户的身体数据
age= 36     #年龄
armLeft =36 #左臂围
armRight= 33 #右臂围
chestCircumference= 88  #胸围
gender= '男' #性别
height= 188  #身高
hipCircumference= 88 #臀围
legLeft= 33 #左腿
legRight= 33 #右腿
name= 5522 #称重用户的用户名
personType= '普通人' #人物类型 还有 业余运动员爱好者   专业运动员/教练
waistCircumference= 66 #腰围
###用户的称重数据
weight= 60.8
water= 37.1
fat= 14.1
muscle= 53.8
bendingCount= 33
bmi= 17.2
bmr= 1728.7
bones= 2.9
bonesRatio=round(bones/weight*100,1)
entrailsFat= 2
fatRatio= round(fat/weight*100,1)
muscleRatio= round(muscle/weight*100,2)
squatCount= 33
waterRatio=  round(water/weight*100,2)
###













if __name__ == '__main__':
    print(waterRatio)


