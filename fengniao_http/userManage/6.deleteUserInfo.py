#!/usr/bin/python
import requests as req
import base64
import json

"""
批量删除用户信息
"""
post_url = "http://192.168.1.91:8080/userManage/deleteUserInfo"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    # 用户ID集合
    'user_id_list': [
        '2', '1'
    ]
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
