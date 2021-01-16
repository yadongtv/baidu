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
post_url = "http://" + ip + ":8080/recognitionManage/getFeature"

# image_path = '/home/hanchunyu/fengniao/userManage/杨洪天_006_男.jpg'
# images_base64('D:\\Data\\qing\\data\\1w\\7.jpg')

data = {
    'pass': passwd,
    'image_content': images_base64('../a.jpg'),
    'image_type': 'image',
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)
