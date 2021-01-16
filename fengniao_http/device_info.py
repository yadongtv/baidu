import hashlib
import base64

ip = "192.168.1.124"
password = "123456"

md5 = hashlib.md5()  # 要加密的字符串
md5.update(password.encode("utf-8"))
passwd = md5.hexdigest()
print(passwd)


def images_base64(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
    print(image)
    image_base64 = str(base64.b64encode(image), encoding='utf-8')
    return image_base64
