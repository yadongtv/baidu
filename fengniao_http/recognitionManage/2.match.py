#!/usr/bin/python
import requests as req
import base64
import json
import time

# -*- coding: utf-8 -*-

start_time = time.time()
post_url = "http://192.168.1.102:8080/recognitionManage/match"

# 1
# image_path_1 = 'D:\\桌面\\蜂鸟\\picker\\3\\1.jpg'
# image_path_2 = 'D:\\桌面\\蜂鸟\\picker\\3\\2.jpg'

# 1.1
image_path_1 = 'D:\\桌面\\蜂鸟\\picker\\3\\3.jpg'
image_path_2 = 'D:\\桌面\\蜂鸟\\picker\\3\\4.jpg'

# 2
# image_path_1 = 'D:\\桌面\\蜂鸟\\picker\\2\\1.jpg'
# image_path_2 = 'D:\\桌面\\蜂鸟\\picker\\2\\2.jpg'

# 3
# image_path_1 = 'D:\\桌面\\蜂鸟\\picker\\1\\1.jpg'
# image_path_2 = 'D:\\桌面\\蜂鸟\\picker\\2\\2.jpg'

with open(image_path_1, 'rb') as f:
    image = f.read()
    image_base64_1 = str(base64.b64encode(image), encoding='utf-8')

with open(image_path_2, 'rb') as f:
    image = f.read()
    image_base64_2 = str(base64.b64encode(image), encoding='utf-8')

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'image1': {
        'image_content': image_base64_1,
        'image_type': 'image',
        'image_name': '1',
    },
    'image2': {
        'image_content': image_base64_2,
        'image_type': 'image',
        'image_name': '2',
    },
    'quality_control': 'NONE',
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)
