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

# get player's name from lobby
def new_player(pname):
    global player_name
    player_name = pname

def handle_message(data):
    message = json.loads(data)
    if message["token"] == "Name":
        # tm = {"token": "Name", "name": "ClareKyleDamirAnnaKhanh"} #tester
        tm = {"token": "Name", "name": player_name}
        send_message(tm)

    elif message["token"] == "Result":
        print("---- Get winner:", message["winner"])
        # game-over page get winner's name
    

# To be binded by front-end team members
def send_message(message):
    data = json.dumps(message)
    my_socket.sendall(bytes(data,encoding="utf-8"))

# Be called in lobby
def start_client():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))

    print("Connected to server!")
    receiver_thread = Thread(target=receiver_runner)
    receiver_thread.start()

"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""
