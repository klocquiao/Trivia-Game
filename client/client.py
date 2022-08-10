import socket
from threading import Thread
import json 
from player import Player
HOST = "127.0.0.1"
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

def handle_message(data):
    global player_list, question, answers, is_layout_ready
    message = json.loads(data)
    print("Data receive: ", message)
    if message["token"] == "Name":
        tm = {"token": "Name", "name": player_name}
        send_message(tm)
    elif message["token"] == "Players":
        player_list = list(map(lambda x: Player(x), message["players"]))
    elif message["token"] == "Round":
        is_layout_ready = True
        question = message["question"]
        answers = message["answers"]
    elif message["token"] == "Player":
        update_player_list(message["name"] ,message["score"])
    elif message["token"] == "Lock":
        unlock_button_press()
    elif message["token"] == "Locked":
        lock_answer(message["answer"])

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

# Helpers 

def is_enough_player():
    return is_layout_ready

def new_player(pname):
    global player_name
    player_name = pname

def update_player_list(name, score):
    for player in player_list:
        if player.get_name() == name:
            player.set_score(score)

def get_player_name():
    return player_name

def get_player_list():
    return player_list

def get_question():
    return question

def get_answers():
    return answers


