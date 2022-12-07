from ast import arg
import asyncio
import socketio
import argparse
import cv2
import pickle 
import time 
import json
import base64
import threading 
parser  =  argparse.ArgumentParser()
parser.add_argument("-i" , "--ip" ,  help  =  "give ip to connect" )
parser.add_argument("-s" , "--streamname" ,  help  =  "give stream name" )
parser.add_argument("-n" ,  "--username" ,  help =  "give user name")
args  =  parser.parse_args()
ssio = socketio.AsyncClient()


@ssio.event
async def connect():
    print('connected to server')

@ssio.event
async def disconnect():
    print('disconnected from server')

# @ssio.on('hello')
# async def hello

@ssio.on("start")
async def startVideo():
    print('wefwef')
    vid  =  cv2.VideoCapture(0)
    d = []
    index  =   0
    print('ererfwefewfewf')
    while True:
        ret  , frame  =  vid.read()
        ret, buffer  =   cv2.imencode(".jpeg" ,  frame  ,  [int(cv2.IMWRITE_JPEG_QUALITY ),80])
        message  =   base64.b64encode(buffer)
        
        d.append(message)
        if len(d)==10:
            print('emitting the data')
            await ssio.emit('send' ,  (args.username ,  args.streamname , d, index)) 
            
            await ssio.sleep(1)
            d = []
            index+=1
            print('not getting there')




async def start_server(connection):
    print("wefwefewf")
    await ssio.connect('http://'+connection, auth={'token': args.username}, wait_timeout=10)
    print(connection)
    print('efewfew')
    await ssio.emit('start')
    print('wefewf')
    await ssio.wait()
    
        
    
    

    
    


if __name__ == '__main__':
    asyncio.run(start_server(args.ip))