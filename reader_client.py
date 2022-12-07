
import asyncio
import socketio
import base64
sio = socketio.AsyncClient()
import numpy as np
import cv2
import time
import threading
import argparse

parser  =  argparse.ArgumentParser()
parser.add_argument("-i" , "--ip" ,  help  =  "give ip to connect" )
parser.add_argument("-s" , "--streamname" ,  help  =  "give stream name" )
parser.add_argument("-n" ,  "--name" ,  help =  "give user name")
args  =  parser.parse_args()

d =  []
name  = args.name
streamername = args.streamname


def stream_func():
    global d
    while True :
        if d:
            frames =  d.pop(0)
            for  i  in range(len(frames)):
                data =  base64.b64decode(frames[i])

                npdata  =   np.fromstring(data  ,dtype  = np.uint8)
                frame  =  cv2.imdecode(npdata ,  1)
                cv2.imshow("Recieving Video" , frame)
                
                key  =  cv2.waitKey(100)


@sio.event
async def connect():
    print('connected to server')



@sio.event
async def disconnect():
    print('disconnected from server')

@sio.on("frame_sender")
async def streaming_data(frames_data): 
    
    global d , name  , streamername
    if frames_data['is_running']:

        index   =   frames_data['index']
        frames   =  frames_data['frame']

        d.append(frames)
      
        await sio.emit('give_data' , {'streamername':name,  "streamname":streamername , "frame":index+1})

    else:
        await sio.disconnect()
        

    



async def start_server():
   
    await sio.connect(args.ip, auth={'token': 'my-token'})
    await sio.emit('give_data' , {'streamername':name ,  "streamname":streamername , "frame":None})  
    thread1 = threading.Thread(target=stream_func , args =())
    thread1.start()
    await sio.wait()
        
    


if __name__ == '__main__':
    asyncio.run(start_server())


