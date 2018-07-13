#!/usr/bin/env python
# coding=utf-8
import my_python_code.myCase.api_case.interface.login_args
from imp import reload
import logging,time
import json,pymysql
from my_python_code.myCase.api_case.interface.Basics_class import Basics_case, get_error
from  my_python_code.myCase.api_case.interface.接口记录 import *
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
from my_python_code.mysql.Basic_information import my_sql_link_test,my_sql_link
from  my_python_code.tools.make_report import make_report
from my_python_code.myCase.api_case.interface.login_args import login
import time,re
logging.basicConfig(level=logging.INFO)
true=True
false=False
class API_case(Basics_case):
    def __init__(self):
        self.API_name =  上传学员运动数据
        Basics_case.__init__(self)  # 子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用
    @get_error
    def test_case(self):  #case  上传同一份classdata,对比除了repor uuid之外的数据检查得分在否和数据库的数据相匹配
        login_heard = login(self.client)
        a = orm_to_mysql(my_sql_link_test())
        all_case_json = self.orm.table('web_platform_comparison_library').select(api_name=V3报告json数据).all()
        all_rult_list=[]
        for x in all_case_json:
            old_class_data = self.client.get(x['send_json'])
            class_id=old_class_data.json()['classDataList'][0]['classesId']
            user_uuid=old_class_data.json()['classDataList'][0]['userUuid']
            a.table('user_report').delete(user_uuid=user_uuid)
            a.table('user_daily_weight').delete(user_uuid=user_uuid)
            get_report_list = self.client.post(url=self.API_url(), data=old_class_data, headers=login_heard)
            while not a.table('user_report').select(user_uuid=user_uuid).one():
                time.sleep(1)
            case_rult = self.client.post(url=self.url + 获取当前课程的报告列表, json={"classesId": class_id,"subjectId": 1441109786806272}, headers=login_heard)
            print(case_rult.json()['classReportList'][0]['reportUrl'])

            report_uuid=re.findall(r'i=(.*.)',case_rult.json()['classReportList'][0]['reportUrl'] )[0]     #获取报告的uuid
            new_report_json=self.client.get('http://192.168.41.41/KKNewReport/PadGetUUIDUserReportV3?i='+report_uuid).json()
            old_report_json=eval(x['receive_json'])
            print(case_rult.json()['classReportList'][0]['reportUrl'])
            rult_list = []
            #总分
            if new_report_json['score']!=old_report_json['score']:rult_list.append({'mod_name':'总分score', 'new_report_json':new_report_json['score'],'old_report_json':old_report_json['score']})
           #卡路里
            if new_report_json['trainCalorie']!=old_report_json['trainCalorie']:rult_list.append({'mod_name':'trainCalorie ', 'new_report_json':new_report_json['trainCalorie'],'old_report_json':old_report_json['trainCalorie']})
           #报告类型
            if new_report_json['reportType']!=old_report_json['reportType']:rult_list.append({'mod_name':'得分reportType', 'new_report_json':new_report_json['reportType'],'old_report_json':old_report_json['reportType']})
            # 动作速度极值达标率
            if new_report_json['coordinates']['unitnumStandardRate']!=old_report_json['coordinates']['unitnumStandardRate']:rult_list.append({'mod_name':'动作速度极值达标率', 'new_report_json':new_report_json['coordinates']['unitnumStandardRate'],'old_report_json':old_report_json['coordinates']['unitnumStandardRate']})
            #abilityScore  PK综合运动能力的分
            if new_report_json['musleRates']['exerciseAbility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['abilityScore']:rult_list.append({'mod_name':'bilityScore  PK综合运动能力的分', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['abilityScore']})
            #"身体平衡能力"
            if new_report_json['musleRates']['exerciseAbility']['balanceAbility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['balanceAbility']['abilityScore']:rult_list.append({'mod_name':'身体平衡能力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['balanceAbility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['balanceAbility']['abilityScore']})
            #"身体控制能力"
            if new_report_json['musleRates']['exerciseAbility']['bodyontrolAbility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['bodyontrolAbility']['abilityScore']:rult_list.append({'mod_name':'身体控制能力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['bodyontrolAbility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['bodyontrolAbility']['abilityScore']})
            #"心肺耐力"
            if new_report_json['musleRates']['exerciseAbility']['cardioPulmonaryEndurance']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['cardioPulmonaryEndurance']['abilityScore']:rult_list.append({'mod_name':'心肺耐力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['cardioPulmonaryEndurance']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['cardioPulmonaryEndurance']['abilityScore']})
            #"协调能力"
            if new_report_json['musleRates']['exerciseAbility']['coordinationAbility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['coordinationAbility']['abilityScore']:rult_list.append({'mod_name':'协调能力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['coordinationAbility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['coordinationAbility']['abilityScore']})
            #"核心稳定能力"
            if new_report_json['musleRates']['exerciseAbility']['coretabilizationAbility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['coretabilizationAbility']['abilityScore']:rult_list.append({'mod_name':'核心稳定能力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['coretabilizationAbility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['coretabilizationAbility']['abilityScore']})
            #"核心肌肉耐力"
            if new_report_json['musleRates']['exerciseAbility']['coreuscletrength']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['coreuscletrength']['abilityScore']:rult_list.append({'mod_name':'核心稳定能力', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['coreuscletrength']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['coreuscletrength']['abilityScore']})
            #"爆发力"
            if new_report_json['musleRates']['exerciseAbility']['explosiveorce']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['explosiveorce']['abilityScore']:rult_list.append({'mod_name':'explosiveorce', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['explosiveorce']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['explosiveorce']['abilityScore']})
            #"柔韧度"
            if new_report_json['musleRates']['exerciseAbility']['flexibility']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['flexibility']['abilityScore']:rult_list.append({'mod_name':'"柔韧度"', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['flexibility']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['flexibility']['abilityScore']})
            #"下肢力量"
            if new_report_json['musleRates']['exerciseAbility']['lowerLimbStrength']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['lowerLimbStrength']['abilityScore']:rult_list.append({'mod_name':'"下肢力量"', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['lowerLimbStrength']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['lowerLimbStrength']['abilityScore']})
            #"灵活性"
            if new_report_json['musleRates']['exerciseAbility']['sensitivity']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['sensitivity']['abilityScore']:rult_list.append({'mod_name':'""灵活性""', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['sensitivity']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['sensitivity']['abilityScore']})
            #"上肢力量"
            if new_report_json['musleRates']['exerciseAbility']['upperLimbStrength']['abilityScore']!=old_report_json['musleRates']['exerciseAbility']['upperLimbStrength']['abilityScore']:rult_list.append({'mod_name':'""灵活性""', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['upperLimbStrength']['abilityScore'],'old_report_json':old_report_json['musleRates']['exerciseAbility']['upperLimbStrength']['abilityScore']})
            #vomaxRealValue
            if new_report_json['musleRates']['exerciseAbility']['vomaxRealValue'] !=old_report_json['musleRates']['exerciseAbility']['vomaxRealValue'] :rult_list.append({'mod_name':'""vomaxRealValue""', 'new_report_json':new_report_json['musleRates']['exerciseAbility']['vomaxRealValue'] ,'old_report_json':old_report_json['musleRates']['exerciseAbility']['vomaxRealValue']})

            print(rult_list)
        return {"result": 1}
if __name__ == '__main__':
    example = API_case()
    print(example.test_case())
