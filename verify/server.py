import asyncio
import websockets
import time

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

async def echo(websocket, path):
    while True:

        q1 = encode("服务器")
        await websocket.send(q1)

        time.sleep(3)
        long = await websocket.recv()
        print("> {}".format(long))
        de = decode(long)
        print(de)
        print("-----------------------------")

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, '192.168.1.10', 8080))
asyncio.get_event_loop().run_forever()
