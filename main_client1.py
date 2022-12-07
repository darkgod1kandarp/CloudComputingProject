
import socketio
import os
import csv
sio = socketio.AsyncClient()
print('wef')
import asyncio
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help = "Show Output")
args = parser.parse_args()

@sio.event
async def connect():
    print('connected to server')



@sio.event
async def disconnect():
    print('disconnected from server')


@sio.on('usage')
async def usage(ip ,usage):
    with open('usage_server_reader.txt' , 'a') as f :
        f.writelines(ip+str(",")+ str(usage)+'\n')
    await sio.disconnect()
    



async def start_server(connection):
    try:
        
        await sio.connect(connection, auth='main_client')
        await sio.emit('cpuusage')
        await sio.wait()
    except Exception as exp:
        await sio.disconnect()
        print('not able to connect')


if __name__ == '__main__':
    asyncio.run(start_server(args.ip))