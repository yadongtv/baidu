#!/usr/bin/python
import requests as req
import base64
import json
import time

# -*- coding: utf-8 -*-
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64


# 获取用户信息
post_url = "http://"+ip+":8080/userManage/getUserList"

data = {
    'pass':passwd,
    'start': 0,
    'length': 1000,
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
