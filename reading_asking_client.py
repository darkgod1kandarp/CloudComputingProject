import asyncio
import socketio
import base64
import os
sio = socketio.AsyncClient()
import numpy as np
import cv2
import time
import threading
name  = ""
streamername = ""

@sio.on('serverdetail')
async def func1(data1 , data):
    print(data1)
    if data:
        
        global name 
        global streamername
       
        await sio.disconnect()
        os.system('python3 reader_client.py -i '+'http://'+data1 +" -n" +name + " -s" +streamername) 
    else:
        await sio.disconnect()


async def start_server():
    global name
    global streamername
    name = input("Enter your streamer name : ")
    streamername = input("Enter your streamer streamname : ")
    await sio.connect('http://10.1.157.173:5000', auth={'token': 'my-token'})
    await sio.emit('reading',  {'token':'qwrqwr56wqr'})
  
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())