
import pickle
import uvicorn
import cv2
import socketio
# Importing the library
import asyncio
import psutil
from datetime import datetime
import numpy as np
import threading
import motor.motor_asyncio

# Calling psutil.cpu_precent() for 4 seconds

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://kandarp:Sd0QWPOfcNGGwcop@cluster0.bx7xret.mongodb.net/?retryWrites=true&w=majority"
)
client.get_io_loop = asyncio.get_running_loop
db = client.stream


@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')


@sio.on("give_data")
async def stream_data(sid, data):
    print(data , 'wefew')
    if not data['frame']:   
        first_data_list = []
        while len(first_data_list)!=25:
            first_data = db[data['streamername'] + "_" + data["streamname"]].find(
                allow_disk_use=True).sort('index', -1).limit(25)

            first_data_list = await first_data.to_list(length=None)
            print(first_data_list[0]['index'])
        if first_data_list:
            frames_arr = []
            last_index = None
            for data in first_data_list:
                frames_arr += data['stream_data']
            last_index = data['index']
            frames_arr =  frames_arr[::-1]

            await sio.emit('frame_sender', {
                'frame': frames_arr,
                'index': last_index,
                'is_running': True
            },
                           to=sid)

        else:
            
            await sio.emit('frame_sender', {
                'frame': None,
                'index': None,
                'is_running': False
            },
                           to=sid)

    else:
        next_frame_list = []
        print(data['frame'] , "wefew")
        while next_frame_list!=5:
           
            next_frame = db[data['streamername'] + "_" + data["streamname"]].find({
                'index': {
                    "$gt": data['frame'] -1
                }
            }).sort('index').limit(5)
            
            
            next_frame_list = await next_frame.to_list(length=None)
            print(len(next_frame_list) )
        if not next_frame_list:
            await sio.emit('frame_sender', {'is_running': False}, to=sid)
        else:
            frames_arr = []
            last_index = None
            for data in next_frame_list:
                frames_arr += data['stream_data']
            
            last_index = data['index']
            frame_arr =  frame_arr[::-1]

            await sio.emit('frame_sender', {
                'frame': frames_arr,
                'index': last_index,
                'is_running': True
            },
                           to=sid)


@sio.event
def disconnect(sid):
    print('disconnected', sid)


if __name__ == '__main__':
    uvicorn.run("reading_server:app", host='192.168.0.108', port=8000 , reload = True, workers= 2)