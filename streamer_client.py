import asyncio
import socketio
import os
sio = socketio.AsyncClient()
STREAMER_SERVER  = False

@sio.event
async def connect():
    print('connected to server')
    # os.system('python3 client1.py')



@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def hello(a, b, c):
    print(a, b, c)
    
@sio.on('serverdetail') 
async def serverAvailable(serverip , available):
    STREAMER_SERVER =  serverip
    await sio.disconnect()


async def start_server():
    
    await sio.connect('http://192.168.0.107:5000', auth={'token': 'my-token'})
    await sio.emit('streaming' ,{'data':'streaming server'})
    await sio.wait()
        
    # await sio.wait()
    


if __name__ == '__main__':
    asyncio.run(start_server())