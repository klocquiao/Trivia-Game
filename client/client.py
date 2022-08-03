import socket
import threading
import json 

HOST = "127.0.0.1"
PORT = 12345

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((HOST, PORT))

def receiver_runner():
    while True:
        try:
            data = my_socket.recv(1024).decode("utf-8")
            handle_message(data)
        except:
            print("An error has occured!")
            my_socket.close()

def handle_message(data):
    if data == "test":
        tm = {"token": "Test", "message": "Hello world!"}
        send_message(tm)

# To be binded by front-end team members
def send_message(message):
    data = json.dumps(message)
    my_socket.sendall(bytes(data,encoding="utf-8"))

def start_client():
    receiver_thread = threading.thread(target=receiver_runner)
    receiver_thread.start()

"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""