#!/usr/bin/python
import requests as req
import base64
import json
import time

# -*- coding: utf-8 -*-

start_time = time.time();
post_url = "http://192.168.1.88:8080/recognitionManage/match"

image_path_1 = '/home/hanchunyu/fengniao/userManage/1.jpg'
image_path_2 = '/home/hanchunyu/fengniao/userManage/a.jpg'


with open(image_path_1, 'rb') as f:
 image = f.read()
 image_base64_1 = str(base64.b64encode(image), encoding='utf-8')

with open(image_path_2, 'rb') as f:
 image = f.read()
 image_base64_2 = str(base64.b64encode(image), encoding='utf-8')


data = {
    'pass': 'e10adc3949ba59abbe56e057f20f883e',
    'image1':{
    	'image_content':image_base64_1,
	'image_type':'image',
	'image_name':'1',
    },
    'image2':{
    	'image_content':'wGwCPTnVST1CMPs8Kf7IvUqsnj2FdvY9TIC6O0QaRz2RpT8+z051vKgZMr2uoMc9YCCRvZ++Fr5MlhY9W4Mfvk5qBr1rWkw+sH/RPS6mPj4yTmA8ZNPiPFfFNz1COz294Q9CPO0+Cz5uIyK9/v8vPqVQhLyr18W8y6aRPf0V5LzhD8I8j9ENvhGreL2HYJa961Q/PdqTmj33eMa9h2swvHLWc702F4o9x93nO1mZPT446/29cPfpvUfjBj6KKfC9wx/UvT2eCT4go5c8udoqPl1XO7y48Aa+WoPLvVmZpz07tNM71spEPb9sWrzcZ2I9jedXvNbgIL2kW8q9NSKkvXHszz3rSf08EbaOPcM1hL5tLjy8YBXPvGanUj35bYC98eZCPEnCprxRKHI94BowvhR/Jj4IRdk9fRsZvfaOorytq+G94+5LvY7Rez19ENe7o1v2vRG2ur1F+VC9j8ZhPWa9rrvRIuU9xvPDPflXULvV6w4+c9abvRkcrr36QfS9+ky2vXO1fT1H2Fq91uCgPASHcT2oGbI8JFaRPWiGXL1lyJy90EMDvdEi5T0lQLU9IKMXPWl7wjx9EFe7f/oMPq+VAb0Uf7y9OsovvZ3UNL1ZmSe9xf7dvW0jej2UeQM9CiS3vMQUOr3I0k290DjBvVT8Cb0XPWY+W23vvAhQR70=',
	'image_type':'feature',
	'image_name':'2',
    },
    'quality_control':'NONE',
}

json_data = json.dumps(data)

r = req.post(url = post_url, data = json_data)

end_time = time.time()
print("single user registeration takes %.2f seconds" %(end_time - start_time))
print(r.text)
