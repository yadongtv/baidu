#!/usr/bin/python
import requests as req
import base64
import json

# 获取用户信息
post_url = "http://192.168.1.91:8080/userManage/getUserInfo"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'user_id': '1604573320777'
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)