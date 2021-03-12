#네이버 Papago NMT API 예제

import os
import sys
import urllib.request
client_id = "zz58id7hhd"
client_secret = "M6tkUGtGZn7DtdnCS7TGJ2KWhy0nNPInWZkj3iey"

encText = urllib.parse.quote("안녕하세요")


data = "source=ko&target=en&text=" + encText
url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
request.add_header("X-NCP-APIGW-API-KEY",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)