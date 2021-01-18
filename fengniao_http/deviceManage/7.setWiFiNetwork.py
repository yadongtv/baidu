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
post_url = "http://" + ip + ":8080/deviceManage/setWiFiNetwork"

# 无线开启DHCP
data = {
    "pass": passwd,
    "DHCP": True,
    "SSID": "oppo",
    "PWD": "12345678"
}

# 无线关闭DHCP
# data = {
#         "pass": passwd,
#         "enable": True,
#         "DHCP": False,
#         "SSID": "SSID",
#         "PWD": "admin",
#         "IP": "192.168.1.71",
#         "gateway": "192.168.1.1",
#         "subnet_mask": "255.255.0.0",
#         "DNS": "192.168.1.1"
#     }

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)
