"""
蜂鸟注册人脸
"""
# !/usr/bin/python
import requests as req
import base64
import json
import time
import sys

sys.path.append('../')
from device_info import ip, passwd, images_base64

# -*- coding: utf-8 -*-
# 添加用户

start_time = time.time()
post_url = "http://" + ip + ":8080/userManage/addUser"

# image_path = '/home/hanchunyu/fengniao/userManage/杨洪天_006_男.jpg'
# image_path = 'D:\\Data\\img\\data\\天哥.jpg'
# image_path = 'D:\\Data\\img\\data\\晨哥.jpg'
# image_path = 'D:\\Data\\img\\data\\华哥.jpg'
# image_path = 'D:\\Data\\img\\data\\阿东.jpg'
# image_path = 'D:\\Data\\img\\data\\强sir.JPG'a
# image_path = 'D:\\Data\\img\\data\\吴将军.JPG'
# image_path = 'D:\\Data\\img\\data\\兴.JPG'
image_path = 'D:\\Data\\fengniao_http\\a.jpg'




# 打开照片文件，base64加密
with open(image_path, 'rb') as f:
    image = f.read()
# image = 'AAAIPgDAO74AQKS+AADmPADAEj8AAA6+AHAXPwDQOz8AgM69AJBKvwBAZT4AwHa+AKAIvwBwJr8AgF0+AGCPPgDAOj4AQE4+AEDFPgCAmz4AAPg7AAB6PQCAdz4AgII/AIDfPgCQHr8AQIW/AADYvgAA/j0AgCu+AJAEvwAACL0AkDi/AEB7vgAAM74AAEw+ADAMvwAAGb0AwEo/ACDSvgAAOr4AQEa+AADZPQAAMT0AAFA8ACDevgCASj4A4KG+AMDHPgAAMDwAAB09AAB4PADQUD8AIDK/ANAiPwCwHj8AQMK+AMADPgAAez4A0JE/AABxvQDADT4AQNc+AID4PQAATj8AgIw9AEA6vgDALr4AwII+ACCOvgBAqj4AAHS8AAALvQCA7j0AYKE+AABwuwDAH74AwFu+AAA9vQCAPT4AgAk/AFAEvwDA4r4AABM9AAA6PQAA8LwAAAm9AECePgAAWD0AIOe+AMDjvgCg2D4A0Di/AMArPgBAFb4AAPa9AKACvwBgvL4AAPK+AADmvgAAVT0AUCk/AIBavgDwaD8A0E+/AIBiPgDg0T4A8Ak/AIAevwAA7DwAAJ8+AODMvgBgjb4AYBi/AMDLvgCAjz0AAHI+AADLPQCAqL4AAES8ACCUvgCADD4AgN0+AEAEPgBwCL8AQE4+AMD8vgAAND0=',

image_base64 = str(base64.b64encode(image), encoding='utf-8')
# print(image_base64)

data = {
    'pass': passwd,
    'user_id': 'baidu0000007',
    'image_content': image_base64,
    'image_type': 'image',
    'user_info': {
        'user_type': 1,
        'name': 'jia哥',
        "card_number": "3644243977"
    },
}

json_data = json.dumps(data)

r = req.post(url=post_url, data=json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" % (end_time - start_time))
print(r.text)

"""
翠鸟注册人脸
"""
# # !/usr/bin/python
# import requests as req
# import time
# import base64
# import json
#
# post_url = "http://192.168.1.117:8080/userManage/addUser"
#
# # image_path = '/home/hanchunyu/fengniao/userManage/杨洪天_006_男.jpg'
# # image_path = 'D:\\Desktop\\测试图片1.jpg'
# # image_path = 'D:\\Data\\img\\data\\阿东.jpg'
# image_path = 'D:\\Data\\img\\data\\贾老板.jpg'
#
#
# # 打开照片文件，base64加密
# with open(image_path, 'rb') as f:
#     image = f.read()
#
# image_base64 = str(base64.b64encode(image))
#
# data = {
#     "RequestValue": 2817,
#     "user_id": "0006",
#     "pass": "123456",
#     "image_content": image_base64,
#     "image_type": "image",
#     "user_info": {
#         "name": "韩枫100",
#         "card_number": "3125520912"
#     },
#     "quality_control": "NONE",
# }
#
#
#
#
# json_data = json.dumps(data)
#
# r = req.post(url=post_url, data=json_data)
# print(r.text)
