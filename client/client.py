import socket
from threading import Thread
import json 

HOST = "127.0.0.1"
PORT = 12345
MAX_MESSAGE_SIZE = 4096 

my_socket = None

def receiver_runner():
    while True:
        try:
            data = my_socket.recv(MAX_MESSAGE_SIZE).decode("utf-8")
            handle_message(data)
        except:
            print("An error has occured!")
            my_socket.close()
            break

def handle_message(data):
    message = json.loads(data)
    if message["token"] == "Name":
        tm = {"token": "Name", "name": "ClareKyleDamirAnnaKhanh"}
        send_message(tm)

# To be binded by front-end team members
def send_message(message):
    data = json.dumps(message)
    my_socket.sendall(bytes(data,encoding="utf-8"))

def start_client():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))

    print("Connected to server!")
    receiver_thread = Thread(target=receiver_runner)
    receiver_thread.start()

if __name__ == '__main__':
    start_client()

"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""