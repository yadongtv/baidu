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
语音播报格式
"""
post_url = "http://" + ip + ":8080/deviceManage/setAIOperatingMode"

data = {
    'pass': passwd,
    'mode': 2,
    'check_type': 3,
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)
