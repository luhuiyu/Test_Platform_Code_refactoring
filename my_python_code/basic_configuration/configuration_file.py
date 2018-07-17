import requests
from my_python_code.mysql.Basic_information import *

my_python_code_path=r'/my_python_code'
my_apicase_path=r'.myCase.api_case'
my_appium_path=r'.myCase.appium_case'
Complete_path=r'F:/Test_Platform'
my_api_case_log=r'F:\Test_Platform\my_log\my_api_case_log.txt'

#    case_address=r'F:/Test_Platform'+ '/my_python_code/myCase/appium_case/快快教瘦/test_case'


client = requests.session()  # requests 长链接

kk_test=my_sql_link_test() #连接kk的测试库

user_uuid = '4be9950e-cb60-4d0d-8861-f22debd00210' #用于测试的用户

web_user_name='luhuiyu'

oss_url='http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/'

uuid_idct={'1':  [
    '3b1d5be6-90f2-46c4-ac6f-82df7433584d',
'85dc8136-2aef-40a1-8c73-0b9412f3a1e8',
'62cd95fe854f4491a9ce0eaa9658d3bc',
'ed31a7da-7dbf-4314-aa3e-abd7db4fb84d',
'7165e70f5f4645f3bf8aaefec305f78e',
'37d526122e6947f39e767341e7dd15b4',
'd9f8b8f7c5064a1bb420565d444854e8',
'be37a6d70aaa444fa8a9b73ae82a505b',
'b90b7d1860054845a0fc2bfba48dbaa6',
'3cada9f2-85cc-46be-a2b5-9b3a03276263',
'f9c0d7800f53403eb7fef9b855830fbe',
'7ed405e55f5a4352be6f6e9980358b0d',
'066dfb04194f472e9c91c18486885fca',
'a1d3287bb5c94c6a948f8dddf30e39e7',
'b41ebc90117d46599fef75be3ceebf1e',
'4eb5284b0fc74d59bd6c7b5a0d800689',
            ]}
uuid_idct['2']=[
            'c1f0a33587e747ad81be7dbe58e36cc9',
'15ce2e663df14a33946fab848a214494',
'ccda6eeac3c34563b7ca9b45245ca136',
'00b5af3016fa459a816c5b063437a88b',
'9a696044f6f94bd1a97a873a2021dd5f',
'7285f375a1a04d16a022a142e6723bf1',
'fd30b3e5e42c42a3b4b5deb58ca84bfe',
'7a546d88848d4853801bd44e065d6f40',
'bf8f15e8bce34f599a01ec0b18f200a0',
'6e3802dbe3bb4c168351b060682f7fc7',
'7ed33bbd0d4f462aa16a21c67f6c788a',
'adec9c22354443c2ba8d59fd2a06b209',
'984ab4f150584da492f402f34458dc52',
'b09bcd54-7b9d-41e8-9a6f-a8589f93569d',
'8825d32a-6f77-49e6-8160-9f432fa7c126',]
uuid_idct['3']=[
    '0fd404f3-61f6-409d-b8d5-aafa74676295',
'784125bc-0a89-4323-a5cc-45f66ac822e8',
'6cfca81e-352b-4e66-b21f-1905287c0b8f',
'f8fbeb76-9b64-4f87-94f3-6ebbefc4da06',
'0a7a4b12dbb84343b5c1adfb775b4134',
'7c5ad0c829b645a2bef518665517388b',
'e71d34d2-291d-4367-97bc-2509d1d5d46c',
'40bf217e-25fa-4cca-b7be-de9b17296dc7',
'ea99878c-affb-416f-9a74-c8af57407934',
'98bf4e6c3ef84a96a3595afd81eeb110',
'b09c80d7-ae45-4b48-9d60-6841a9eeab35',
'0f774310-55ba-4b82-a201-ecd3825daf87',
'bee0072f-5363-428d-b648-3f464fc4bb64',
'20a0fda6-4fbd-43ca-8abc-0c9ba9ccdca2',
'4f3b55d4-557c-4eb0-b574-fe3995c41f69',
    ]
uuid_idct['4']=[
    'cc6d4005-a790-47aa-82ae-b2b1a1f15248',
   # 'e9c10cbd-042b-4cf1-b49d-a7a6562e83c8',
    '237f7020-af58-4144-8586-8531fabd898f',
    'a78d2f2a-c9da-4427-8cd4-0358df32bcfb',
    '9ca3fd9c-ad74-4784-b98d-3dc0dd58e3d7',
    '9ba5e744-b9f1-4fbf-9999-54d634860819',
    '0fbf7bb6-cd56-4c0b-832c-0647c5b4903d',
    '4b3b78363712499a919a397322dff3e8',
    '910bc5ef-6c1e-486f-a2d7-0ed52f6cdbf8',
    '650f0a9064bc460cb4a61e9b9023b288',
    '0b985409-adb4-4be0-879b-98a7bbb26e68',
    '8f2fee0e-ab04-4ca6-bc19-d797ed9b2fa0',
    'a81aff37-c203-4ac7-b386-1baa7522cd92',
    '0b3cb4c301ba49a7b6c4f5796985883d',
    'a0b552ee00644fd6b0276cddb32dcbe9',
    'ae0c34bc-b718-4c03-aa35-2d816e571a60',
    '4435683513ac4ae1953356b2741e6473',
    '56236cb4-0187-458a-bc17-07a5c80795f1',
    '02ca3a2b-1443-482c-b692-2d777fb18d59',
    '059d5364-b19b-49fc-9fc3-6fa71b7e2773',
    '3a77bddc-5307-47b2-a308-0f6af95aeaff',
    'fd6c1678-bb28-4727-bca8-dceae094e1ba',
    '78bf0053-a627-4c75-859e-4e9e8822eb9d',
    '49c64eb7-37f9-41fd-a081-fa0998bd200e',
    'fbcdb2d7-c030-4768-92ef-c66d58844eab',
    'fb01f387-7654-407e-bb57-839bafad8929',
    '91b4de98-c869-4b70-a652-b19f525ef11d',
    '482377be-d96d-4b7d-aab5-32440bd3aa1f',
    '399ce994-bd96-493b-85e3-54c5bd89c9c0',
    'fbb747a4-383b-40ec-82ab-e069a39f7c37',
    '0f209660-b934-47e9-9347-7eb5f0225d2a',
    '2ca04cc9-09c2-4668-bffd-18c91ce046d3',
    'e9de898f-22f2-4757-acc6-96803c13da17',
    'bfba8776-5fb4-4f17-b5f1-701551ff9d3f',


]

uuid_idct['0']=[
 #'06855f59-f80f-4c4a-9202-39016ba04772',
  #  'c5ca1533-8ab4-4f98-958d-9114b809b62b',
 #   'f6523836-de2c-4758-9d6c-6666d472dab3',
#'939fd80e-fe28-4bfc-902d-43458c9f10ef',
#'a57906c6-fa02-4ca4-b99d-f0669709f5be',
#'5d9fef97-9c53-4435-af01-4fe26bb020c3',
#    '43e5de14-a322-42f9-8bf8-65f55a1d1285',
#'ccfa52ed-3c36-4c68-a619-c3a6562085c4',
#    '5a90ffb9-e6a6-4c11-aeae-e44453b2f93f',
#'06855f59-f80f-4c4a-9202-39016ba04772',
#   '02ca3a2b-1443-482c-b692-2d777fb18d59',
  #  '059d5364-b19b-49fc-9fc3-6fa71b7e2773',
    #'e623c2ba-4469-4b5f-9b61-aa6874770476',
   # '0623c8d4-dd73-4e3e-ad22-a85018298336',
#'001e5c0b-548d-45fc-b3d1-564d65c84dd3',
'e260a966-9a44-4923-9c39-7a9bf4170cff' ,
    'b2207bc8-d0ad-4fea-b472-ecad76a6116b',
    '3a77bddc-5307-47b2-a308-0f6af95aeaff',
    'fd6c1678-bb28-4727-bca8-dceae094e1ba',
    '78bf0053-a627-4c75-859e-4e9e8822eb9d',
    '49c64eb7-37f9-41fd-a081-fa0998bd200e',
    'fbcdb2d7-c030-4768-92ef-c66d58844eab',
    'fb01f387-7654-407e-bb57-839bafad8929',
    '91b4de98-c869-4b70-a652-b19f525ef11d',
    '482377be-d96d-4b7d-aab5-32440bd3aa1f',
    '399ce994-bd96-493b-85e3-54c5bd89c9c0',
    'fbb747a4-383b-40ec-82ab-e069a39f7c37',
    '0f209660-b934-47e9-9347-7eb5f0225d2a',
    '2ca04cc9-09c2-4668-bffd-18c91ce046d3',
    'e9de898f-22f2-4757-acc6-96803c13da17',
    'bfba8776-5fb4-4f17-b5f1-701551ff9d3f',


]


