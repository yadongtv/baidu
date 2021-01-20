#!/usr/bin/python
import requests
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64

# -*- coding: utf-8 -*-

start_time = time.time()
post_url = "http://" + ip + ":8080/deviceManage/setRecognitionCallback"

data = {
    "pass": passwd,
    "callback_url": "http://192.168.1.1:8011/face",
    "interval_time": 100
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)
