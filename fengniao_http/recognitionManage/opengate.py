#!/usr/bin/python
import requests as req
import base64
import json

# 远程开门
# -*- coding: utf-8 -*-
post_url = "http://192.168.1.88:8080/deviceManage/openGate"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)
print(r.text)
