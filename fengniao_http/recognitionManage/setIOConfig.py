#!/usr/bin/python
import requests as req
import base64
import json

"""
IO配置
"""
# -*- coding: utf-8 -*-
# ip = str(input("请输入板子IP：(例：192.168.1.88)"))
# post_url = "http://" + ip + ":8080/recognitionManage/setIOConfig"
# print(str(post_url))
post_url = "http://192.168.1.68:8080/recognitionManage/setIOConfig"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'gate_open_timeout': 8,
    'gate_open_time': 3,
    'gate_mode': 1,
    'relay_mode': 2,
    # 'alarm_in': 1,
    # 'alarm_out': [1, 1, 1, 1, 1, 1, 1, 1],
    # 'gpio_in_1': 1,
    # 'gpio_in_2': 1,
    # 'gpio_out_1': 2,
    # 'gpio_out_2': 2
}
json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)
print(r.text)
