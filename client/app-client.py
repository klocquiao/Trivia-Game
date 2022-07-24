

import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

my_socket = None

def start_client():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))

    print("Client has sucessfully booted")

    receiver_runner()

def receiver_runner(name):
    data = my_socket.recv(1024).decode()
    
def send_ready():


