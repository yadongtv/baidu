#!/usr/bin/python
import requests as req
import base64
import json
import time
import sys

sys.path.append("../")
from device_info import ip, passwd, images_base64
# -*- coding: utf-8 -*-

post_url = "http://" + ip + ":8080/recognitionManage/getFeature"

# image_path = '/home/hanchunyu/fengniao/userManage/杨洪天_006_男.jpg'
image_path = 'D:\\Data\\fengniao_http\\a.jpg'

with open(image_path, 'rb') as f:
    image = f.read()
# print(image)
image_base64 = str(base64.b64encode(image), encoding='utf-8')

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'image_content': image_base64,
    'image_type': 'image',
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)