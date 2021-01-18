#!/usr/bin/python
import requests as req
import base64
import json
import time
import sys

sys.path.append("../")
from device_info import ip, passwd, images_base64
# -*- coding: utf-8 -*-

post_url = "http://"+ip+":8080/recognitionManage/setRecognitionParam"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'recognition_thr':80
}

json_data = json.dumps(data)

r = req.post(url = post_url, data = json_data)

print(r.text)
