import cv2
from datetime import datetime
import time
import requests as req
import base64
import json

FILENAME = 'myvideo.avi'
WIDTH = 1280
HEIGHT = 720
FPS = 24.1

def open_camera():
    """
    打开摄像头，五分钟获取一张图片信息
    :return: jpg类型的图片
    """
    # 必须指定CAP_DSHOW(Direct Show)参数初始化摄像头,否则无法使用更高分辨率
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 设置摄像头设备分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    # 设置摄像头设备帧率,如不指定,默认600
    cap.set(cv2.CAP_PROP_FPS, 24)
    # 建议使用XVID编码,图像质量和文件大小比较都兼顾的方案
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(FILENAME, fourcc, FPS, (WIDTH, HEIGHT))
    start_time = datetime.now()

    # 播放视频
    while True:
        # global frame
        ret, frame = cap.read()

        if ret:
            out.write(frame)
            # 显示预览窗口
            cv2.imshow('Preview_Window', frame)

            # 录制5秒后停止
            if (datetime.now() - start_time).seconds == 100:
                #
                cv2.imwrite(folder_path + str(count) + '.jpg', frame)  # 存储为图像
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                print(count)
                #
                cap.release()
                break

            # 监测到ESC按键也停止
            if cv2.waitKey(3) & 0xff == 27:
                cap.release()
                break
    # 释放摄像头
    out.release()
    cv2.destroyAllWindows()


def send_images(image_path):
    post_url = "http://192.168.3.99:8080/RecognitionManage"

    # image_path = '/home/lizichen/Desktop/bird/001.jpg'
    with open(image_path, 'rb') as f:
        image = f.read()

    image_base64 = str(base64.b64encode(image), encoding='utf-8')
    # print(image_base64)

    data = {
        'RequestValue': 2819,
        'pass': '123456',
        'image_type': 'image',
        'quality_control': 'NONE',
        'image_content': image_base64,
        'user_num': 1
    }

    json_data = json.dumps(data)
    # print(json_data)

    r = req.post(url=post_url, data=json_data)

    print(r.text)

# 截取图片中500*500的
def screenshot(import_path,output_path):
    frame = cv2.imread(import_path)
    cropped = frame[0:500, 0:500]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(output_path, cropped)


if __name__ == '__main__':
    folder_path = 'D:\\qwe\\'

    # count = 1
    # image_path = folder_path + str(count) + '.jpg'
    # image_path = 'D:\\qwe\\qq.JPG'
    # print(image_path)
    while True:
        open_camera()
        # send_images(image_path)
        # count += 1
        continue
