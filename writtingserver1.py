from distutils.log import debug
import pickle
import uvicorn
import cv2  
import socketio
# Importing the library
import asyncio
import psutil
from datetime import datetime
import numpy  as np
import threading
import motor.motor_asyncio
loop = asyncio.get_event_loop()


# Calling psutil.cpu_precent() for 4 seconds

class RunThread(threading.Thread):
    def __init__(self, func, a, b, stream):
        self.func = func
        self.a  =  a
        self.b  =   b 
        self.stream  =  stream
        self.result = None
        super().__init__()

    def run(self):
        self.result = asyncio.run(self.func(self.a , self.b , self.stream))

def run_async(func, a, b, stream):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        thread = RunThread(func, a, b, stream)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(func(*args, **kwargs))

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://kandarp:Sd0QWPOfcNGGwcop@cluster0.bx7xret.mongodb.net/?retryWrites=true&w=majority")

client.get_io_loop = asyncio.get_running_loop
db  = client.stream
# try:
#     loop = asyncio.get_running_loop()
# except RuntimeError:  # 'RuntimeError: There is no current event loop...'
#     loop = None

STREAM_NAME  =  None

@sio.event 
async def connect(sid, environ, auth):
    
    print(f'connected auth={auth} sid={sid}')
    
        
@sio.event
def disconnect(sid):
    if STREAM_NAME:
        db[STREAM_NAME].insert_one({'stream_data':None  ,  'index' :None})
    print('disconnected', sid)
    
@sio.on('send')
async def streamData(sid   ,a, b, data, index):

    global STREAM_NAME 
    STREAM_NAME =  a+"_"+b

    if data=="last":
        print("ewfew")
    await db[a+"_"+b].insert_one({'stream_data':data , 'index':index})
    
    
    
@sio.on('start')
async def startingPermission(sid):
    print('hello')
    await sio.emit('start', to = sid)
    
    
@sio.on('cpuusage')
async def usage(sid):
   
    val  = psutil.cpu_percent(4)
  
    await sio.emit('usage',('192.168.0.108:6000' , val) , to  =  sid  )

if __name__ == '__main__':
    uvicorn.run(app, host='192.168.0.108', port=6000  )