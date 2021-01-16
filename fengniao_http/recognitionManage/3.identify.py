#!/usr/bin/python
import requests as req
import base64
import json
import time

# -*- coding: utf-8 -*-

start_time = time.time()
post_url = "http://192.168.1.88:8080/recognitionManage/identify"

# image_path = '/home/hanchunyu/fengniao/userManage/杨洪天_006_男.jpg'
image_path = '/home/hanchunyu/fengniao/userManage/a.jpg'

with open(image_path, 'rb') as f:
    image = f.read()
    image_base64 = str(base64.b64encode(image), encoding='utf-8')

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'image_content': image_base64,
    'image_type': 'image',
    'quality_control': 'NONE',
    'threshold': 80,
    'user_num': 10,
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)
