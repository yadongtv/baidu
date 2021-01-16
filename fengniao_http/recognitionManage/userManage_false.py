#!/usr/bin/python
import requests as req
import base64
import json

# 注册或更新人员或人脸信息
post_url = "http://192.168.1.88:8080/userManage"

image_path = 'D:\\桌面\\qing\\data\\1w\\461.jpg'

# 打开照片文件，base64加密
with open(image_path, 'rb') as f:
    image = f.read()

image_base64 = str(base64.b64encode(image), encoding='utf-8')
print(image_base64)



data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    "user_id": "user_id",  # 人员id
    "image_content": image_base64,
    "image_type": "image",
    "user_info": {
        "name": "name",
        "phone_number": "12345"
    },
    "action_type": "APPEND/REPLACE",
    "quality_control": "NONE/LOW/NORMAL/HIGH",
    "auth_start_time": 1577690264,
    "auth_end_time": 1577690264

}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

print(r.text)
