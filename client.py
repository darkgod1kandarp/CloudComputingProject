import asyncio
import socketio
import os
sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected to server')
    os.system('python3 client1.py')



@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def hello(a, b, c):
    print(a, b, c)


async def start_server():
    await sio.connect('http://localhost:5000', auth={'token': 'my-token'})
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())