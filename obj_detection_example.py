import os
import sys
import requests
client_id = "5a7ujbpf09"
client_secret = "aNIgCvVKdwD4iMFk6JtpRotkhosHR8llILAMvqx3"
url = "https://naveropenapi.apigw.ntruss.com/vision-obj/v1/detect"


files = {'image': open('./img/1.jfif', 'rb')}


headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)
