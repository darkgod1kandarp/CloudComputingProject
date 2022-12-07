import uvicorn
import cv2  
import socketio
import csv
from main_client  import start_server
from fastapi.middleware.cors import CORSMiddleware
import os

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)
origins = ["http://localhost:3000"]






@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')

@sio.on('reading')
async def stream_viewer(sid , data):
	print('wefewf')
	with open('reading_server_file.txt' ,   'r') as f:
		csvFile  =   csv.reader(f)
		for  lines in csvFile:
			os.system('python3 main_client1.py -i '+'http://'+lines[0]+":"+lines[1]) 
		
	dict1 = {}
	with open('usage_server_reader.txt') as f:
		reader  = f.readlines()
		for read in reader:
			read = read.split(",")
			dict1[read[0]] = float(read[1].split("\n")[0])
	val  =  sorted(dict1.items() ,  key  =  lambda x  :x[1], reverse   = True )
	if val[0][1]<=70:
		
		await sio.emit('serverdetail' , (val[0][0] , True) , to =  sid)
	else:
		await sio.emit('serverdetail' , (False, False) , to =  sid)

@sio.on('streaming')
async def streaming(sid , data):
    
	with open('server_files.txt'  , 'r') as f  :
		csvFile  =  csv.reader(f)
		for  lines in csvFile:
			os.system('python3 main_client.py -i '+'http://'+lines[0]+":"+lines[1]) 
			# await asyncio.run(start_server('http://'+lines[0]+":"+lines[1]))
			
			# http://192.168.0.107:5000
	dict1 = {}
	with  open('usage_server.txt', 'r') as f:
		reader  =  f.readlines()

		for  read  in   reader:
			read =  read.split(",")
			dict1[read[0]] = float(read[1].split("\n")[0])
	val  =  sorted(dict1.items() ,  key  =  lambda x  :x[1], reverse   = True )
	if val[0][1]<=70:
		
		await sio.emit('serverdetail' , (val[0][0] , True) , to =  sid)
	else:
		await sio.emit('serverdetail' , (False, False) , to =  sid)

		
 

        

@sio.event
def disconnect(sid):
    print('disconnected', sid)


if __name__ == '__main__':
    uvicorn.run(app, host='10.1.157.173', port=5000)
	