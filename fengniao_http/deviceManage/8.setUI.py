#!/usr/bin/python
import requests
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64

# -*- coding: utf-8 -*-
post_url = "http://" + ip + ":8080/deviceManage/setUI"

# 写http服务脚本
data = {
	"pass":passwd,
	"resource_pack":"URL"
}

json_data = json.dumps(data)

r = requests.post(url=post_url, data=json_data)

print(r.text)
