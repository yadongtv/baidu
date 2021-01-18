#!/usr/bin/python
import requests
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64

# -*- coding: utf-8 -*-
"""
自定义信息设置
"""
post_url = "http://" + ip + ":8080/deviceManage/setPrompting"

data = {
    "pass": passwd,
    "main_msg": "main_word",
    "success_msg": "success_word",
    "fail_msg": "fail_word",
    "error_msg": "error_word",
    "show_name": True,
    "show_photo": True,
    " blacklist_pass": True,
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)
