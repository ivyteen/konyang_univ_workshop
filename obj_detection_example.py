import os
import sys
import requests
client_id = "zz58id7hhd"
client_secret = "M6tkUGtGZn7DtdnCS7TGJ2KWhy0nNPInWZkj3iey"
url = "https://naveropenapi.apigw.ntruss.com/vision-obj/v1/detect"


files = {'image': open('./img/1.jfif', 'rb')}


headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)