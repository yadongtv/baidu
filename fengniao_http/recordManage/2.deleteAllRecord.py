#!/usr/bin/python
import requests as req
import base64
import json
import time
import sys

sys.path.append("../")
from device_info import ip, passwd, images_base64
# -*- coding: utf-8 -*-

post_url = "http://"+ip+":8080/recordManage/deleteRecords"

data = {
    'pass': passwd,
    'user_id': 'r10925'
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
