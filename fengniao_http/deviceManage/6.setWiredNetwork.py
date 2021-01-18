#!/usr/bin/python
import requests
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64
"""
设备重启
"""
# -*- coding: utf-8 -*-

post_url = "http://" + ip + ":8080/deviceManage/setWiredNetwork"

# 开启有线DHCP
# data = {
#     'pass': passwd,
#     'DHCP': True
# }

# 关闭有线DHCP，并手动设置ip
data = {
    'pass': passwd,
    'DHCP': False,
    "IP": "192.168.3.182",
    "gateway": "192.168.1.1",
    "subnet_mask": "255.255.255.0",
    "DNS": "192.168.1.1"
}
json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)
