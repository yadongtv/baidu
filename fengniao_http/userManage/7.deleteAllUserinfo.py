#!/usr/bin/python
import requests as req
import base64
import json

"""
批量删除用户信息
"""
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64


# 获取用户信息
post_url = "http://"+ip+":8080/userManage/deleteUserInfo"

data = {
    'pass': passwd,
    # 用户ID集合
    'user_id_list': [
        'nihao', 'ayayi'
    ]
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
