#!/usr/bin/python
import requests as req
import base64
import json
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64


# 获取用户信息
post_url = "http://"+ip+":8080/userManage/getUserInfo"
data = {
    'pass': passwd,
    'user_id': 'baidu0000007'
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)