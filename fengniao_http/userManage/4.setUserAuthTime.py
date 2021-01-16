#!/usr/bin/python
import requests as req
import base64
import json

# 获取访客有效期
post_url = "http://192.168.1.102:8080/userManage/setUserAuthTime"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'user_id': 'r10819',
    'auth_start_time': 1577690264,
    'auth_end_time': 1577690264
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
