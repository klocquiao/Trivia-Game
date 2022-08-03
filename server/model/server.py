import socket
import json 
import threading
import selectors
from .player import Player
HOST = "127.0.0.1"
PORT = 12345

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((HOST, PORT))
my_socket.listen()

clients = []

def receiver_runner(client):
    while True:
        try:
            data = client.recv(1024).decode("utf-8")
            handle_message(data)
        except:
            print("An error has occured!")
            my_socket.close()

def connection_runner():
    while True:
        client, address = my_socket.accept()
        req = json.dumps({"token": "Name"})
        client.sendall(bytes(req, encoding="utf-8"))
        res = client.recv(1024).decode("utf-8")
        newPlayer = Player(res["Name"], client, address)

        receiver_thread = threading.thread(target=receiver_runner)
        receiver_thread.start()

def handle_message(data):
    if data == "test":
        tm = {"Token": "Test", "message": "Hello world!"}
        broadcast_message(tm)

def broadcast_message(message):
    data = json.dumps(message)
    for client in clients:
        client.sendall(bytes(data,encoding="utf-8"))

def start_server():
    connection_thread = threading.thread(target=connection_runner)
    connection_thread.start()

def close_socket():
    my_socket.close()
    
"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""