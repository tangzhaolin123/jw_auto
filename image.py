# from datetime import datetime
# import os
# dt1 = datetime.now()
# dt2 = dt1.strftime('%Y-%m-%d_%H.%M.%S')
# image = os.getcwd() + "\\" + dt2 + ".png"
# print (image)
#
# # os.remove(path)

import requests
import json
def getMedia_id():
    access_token ='c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6'  # 拿到接口凭证
    path = r'D:\jw12\b.png'  # 文件路径
    url = 'https://oapi.dingtalk.com/media/upload?access_token=' + access_token + '&type=file'
    files = {'media': open(path, 'rb')}
    data = {'access_token': access_token,
            'type': 'file'}
    response = requests.post(url, files=files, data=data)
    json = response.json()
    return json["media_id"]
a= getMedia_id()
print (a)