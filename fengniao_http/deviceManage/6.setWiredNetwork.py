#!/usr/bin/python
import requests
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64

post_url = "http://192.168.3.99:8080/UserManage"
image_path = "D:\\桌面\\1.jpg"

with open(image_path, 'rb') as f:
    image = f.read()
image_base64 = str(base64.b64encode(image), encoding='utf-8')

data = {
    "RequestValue": 2817,
    "pass": "123456",
    "image_content": image_base64,
    "image_type": "image",
    "quality_control": "NONE",
    "user_id": "0004",
    "user_info": {
        "name": "jhg"
    }
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)


"""
设备重启
"""
# -*- coding: utf-8 -*-

# post_url = "http://" + ip + ":8080/deviceManage/setWiredNetwork"
#
# # 开启有线DHCP
# # data = {
# #     'pass': passwd,
# #     'DHCP': True
# # }
#
# # 关闭有线DHCP，并手动设置ip
# data = {
#     'pass': passwd,
#     'DHCP': False,
#     "IP": "192.168.1.183",
#     "gateway": "192.168.1.1",
#     "subnet_mask": "255.255.255.0",
#     "DNS": "192.168.1.1"
# }
# json_data = json.dumps(data)
#
# r = requests.post(url=post_url, data=json_data)
#
# print(r.text)


# data = {
#     "RequestValue": 2817,
#     "pass": "123456",
#     "image_content": image_base64,
#     "image_type": "image",
#     "quality_control": "NONE"
# }



# 3.3.3图像对比
# post_url = "http://192.168.3.99:8080/RecognitionManage"
# image_path = "../face_image/天哥.jpg"
#
# with open(image_path, 'rb') as f:
#     image = f.read()
# image_base64 = str(base64.b64encode(image), encoding='utf-8')
#
# data = {
#     "RequestValue": 2819,
#     "pass": "123456",
#     "image_content": image_base64,
#     "image_type": "image",
#     "quality_control": "NONE"
# }
#
# json_data = json.dumps(data)
#
# r = requests.post(url=post_url, data=json_data)
#
# print(r.text)
