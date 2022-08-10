import socket
from threading import Thread
import json 

HOST = "207.23.183.211"
PORT = 12345
MAX_MESSAGE_SIZE = 4096 

my_socket = None
is_layout_ready = False
player_list = []
question = []
answers = []
is_lock = ""

def receiver_runner():
    while True:
        try:
            data = my_socket.recv(MAX_MESSAGE_SIZE).decode("utf-8")
            handle_message(data)
        except socket.error as e: 
            print("An error has occured! ", e)
            my_socket.close()
            break

# get player's name from lobby
def new_player(pname):
    global player_name
    player_name = pname

def is_enough_player():
    return is_layout_ready

def get_player_list():
    return player_list

def get_question():
    return question

def get_answers():
    return answers


def handle_message(data):
    global player_list, question, answers, is_layout_ready
    message = json.loads(data)
    print("Data receive: ", message)
    if message["token"] == "Name":
        # tm = {"token": "Name", "name": "ClareKyleDamirAnnaKhanh"} #tester
        tm = {"token": "Name", "name": player_name}
        send_message(tm)
    if message["token"] == "Players":
        player_list = message["players"]
        # player_list_score = message["score"]
    if message["token"] == "Round":
        is_layout_ready = True
        question = message["question"]
        answers = message["answers"]

# To be binded by front-end team members
def send_message(message):
    print("Message send: ", message)
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

