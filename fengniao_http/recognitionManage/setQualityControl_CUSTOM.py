#!/usr/bin/python
import requests as req
import base64
import json
import time

# -*- coding: utf-8 -*-

start_time = time.time();
post_url = "http://192.168.1.88:8080/recognitionManage/setQualityControl"

data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'work_field':'ALL',
    'quality_control':'CUSTOM',
    'umvalueMin':20,
    'umvalueMax':56,
    'pose':30,
    'occlusion':45,
}

json_data = json.dumps(data)

r = req.post(url = post_url, data = json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" %(end_time - start_time))
print(r.text)
