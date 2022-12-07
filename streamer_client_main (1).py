import asyncio
import socketio
import os
sio = socketio.AsyncClient()
STREAMER_NAME  =  None
STREAMER_STREAM_NAME = None
STREAM_VIDEO =  0

@sio.event
async def connect():
    print('connected to server')
    # os.system('python3 client1.py')



@sio.event
async def disconnect():
    print('disconnected from server')

    
@sio.on('serverdetail') 
async def serverAvailable(serverip , available):
    print(serverip , available)
    await sio.disconnect()
    if available :

        if int(STREAM_VIDEO)!=0:
            os.system('python  streamer_client_writer_video.py -i '+str(serverip)+" -n "+ STREAMER_NAME+" -s "+STREAMER_STREAM_NAME)
        else:
            os.system('python  streamer_client_writer_own.py -i '+str(serverip)+" -n "+ STREAMER_NAME+" -s "+STREAMER_STREAM_NAME)


    else:
        print("Server not available")
   


async def start_server():
    await sio.connect('http://10.1.157.173:5000', auth={'token': 'my-token'})
    await sio.emit('streaming' ,{'data':'streaming server'})
    await sio.wait()
        
    


if __name__ == '__main__':
    STREAMER_NAME =  input("Enter your name : ")
    STREAMER_STREAM_NAME =   input("ENter your stream name : ")
    STREAM_VIDEO =   input("Enter  your stream type :")
    asyncio.run(start_server())