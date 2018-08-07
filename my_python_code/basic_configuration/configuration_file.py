import requests
from my_python_code.mysql.Basic_information import *


MY_PYTHON_CODE_PATH=r'F:\Test_Platform_Code_refactoring'
MY_PYTHON_CODE_NAME=r'my_python_code'
MY_APICASE_PATH=r'myCase\api_case'
MY_APPIUM_PATH=r'myCase\appium_case'
MY_API_CASE_LOG=r'F:\Test_Platform_Code_refactoring\my_python_code\my_log\my_api_case_log.txt'
my_api_case_log=MY_API_CASE_LOG

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
    '0959353b-e23e-4e1f-b22d-8f3a2a88f846',
    '0ab00aef-0692-4269-ae27-849e9dd75163',
    '0d406f44-df35-44c5-9b8b-2239f8b1cf85',
    '0dc9662c-939e-4ce3-bfb6-f9697eef578d',
    '0ddbde49-f749-4b29-9d0b-a59697cec848',
    '10de2ca3-a1dd-4e65-a7f4-053ee03ae0f4',
    '1118ad05-a87c-40f8-81ed-3066779a0c42',
    '11dcf4ba-d070-4fc0-9092-a15a378644b4',
    '132aebfa-aa47-477c-8023-5112549babf9',
    '179407f6-41ad-4243-9b0b-84589ac4c60b',
    '19624fb9-d301-45de-a9f0-5615a8ae8804',
    '1b3ceb4d-6c73-45e1-be5c-c4fd17cdc6df',
    '1fed3027-98c5-461d-9c56-97e333dc217b',
]


uuid_idct['5']=[
    '1d074a60-ae89-41cb-88c3-240a807613c5',
    '8c215f9c-48c0-4bf9-94e2-39796e211a1c',
    '0f3f9fb8-a046-46c6-90ea-871faf2b414a',
    '6b2432c0-f8ba-4db5-9878-8660f755399b',
    'dfa8ed1b-4fb4-4c1d-9b26-b1e0aab86355',
    '852a196e-ba1e-439c-b803-c45b430b559d',
    'b2b22226-4492-4bf1-acc3-c34f794bf3d8',
    'e3f2a096-339b-4094-a60a-89ce648a536a',
    '21470f69-ce70-4a9f-b139-623bf32a45ba',
    '0866ea40-6deb-45e5-a278-0d27482e1e88',

]