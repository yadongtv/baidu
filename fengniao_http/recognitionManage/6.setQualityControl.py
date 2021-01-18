#!/usr/bin/python
import requests as req
import base64
import json
import time
import sys

sys.path.append("../")
from device_info import ip, passwd, images_base64
# -*- coding: utf-8 -*-

start_time = time.time()
post_url = "http://"+ip+":8080/recognitionManage/setQualityControl"

data = {
    'pass': passwd ,
    'work_field':'ALL',
    'quality_control':'NONE'
}

json_data = json.dumps(data)

r = req.post(url = post_url, data = json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" %(end_time - start_time))
print(r.text)
