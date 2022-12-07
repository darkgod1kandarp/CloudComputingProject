# Welcome to PyShine
# In this video server is receiving video from clients.
# Lets import the libraries
import socket, cv2, pickle, struct
import imutils
import threading
import pyshine as ps  # pip install pyshine
import cv2
from collections import deque, defaultdict
import datetime
import os 
from dotenv import load_dotenv
load_dotenv()

import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.poll_backend


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)
#

storing_data = defaultdict(list)


def show_client(addr, client_socket):
    # global counter
    # global host_ip
    # udp_socket  =  socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    # udp_socket.bind((host_ip , port_list[counter]))
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        
        stream_streamer_name = client_socket.recv(1024).decode()
        # stream_name  =   client_socket.recv(1024).decode()
        data  =  []
        
        while True:
            stream_data = client_socket.recv(4 * 1024)
            data.append(stream_data)
            if stream_data == "end":
                break
        
            if len(data)==40:
                print('123')
                db[stream_streamer_name ].insert_one({'stream_data':data ,  'timestamp':datetime.datetime.now()  })
                data = []
        client_socket.close()
    except Exception as e:
        print(f"CLINET {addr} DISCONNECTED")
        pass


while True:
    client_socket, addr = server_socket.accept()
    thread = threading.Thread(target=show_client, args=(addr, client_socket))
    thread.start()
    print("TOTAL CLIENTS ", threading.activeCount() - 1)
