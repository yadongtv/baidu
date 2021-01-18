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
post_url = "http://" + ip + ":8080/deviceManage/setScreenSaver"

# 在device_info.py文件中写setUI_image用来转化图片为base64格式


data = {
    'pass': passwd,
    "is_open": 0,
    "time": 10,
    "images": {
        "image1": "图片数据base64",
        "image2": "图片数据base64",
        "image3": "图片数据base64",
        "image4": "图片数据base64",
        "image5": "图片数据base64"
    }

}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)
