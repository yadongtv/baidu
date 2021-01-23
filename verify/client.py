import asyncio
import websockets
import time

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

async def hello(uri):
    async with websockets.connect(uri) as websocket:

        while True:
            # recv 接收
            recv_text = await websocket.recv()
            print("> {}".format(recv_text))
            en = decode(recv_text)
            print(en)

            print('-------------------------------')

            time.sleep(3)
            # 判断二进制是否是连接
                # 是连接送 ok
            await  websocket.send(encode("客户端"))

asyncio.get_event_loop().run_until_complete(hello('ws://192.168.1.10:8080'))
