import socket
import json 
from threading import Thread
from .player import Player

HOST = "127.0.0.1"
PORT = 12345

NUMBER_OF_CLIENTS = 4
MAX_MESSAGE_SIZE = 4096 

my_socket = None
game = None

def receiver_runner(client):
    while True:
        try:
            data = client.recv(MAX_MESSAGE_SIZE).decode("utf-8")
            handle_message(data)
        except:
            print("Client " + client.get_name() + " has crashed! Exiting game...")
            my_socket.close()
            break

def find_players():
    while game.player_manager.get_number_of_players() < NUMBER_OF_CLIENTS:
        # Accept incoming client
        print("Listening for clients")
        client, address = my_socket.accept()
        print("Player has been found!")

        try:
            # Request a alias for the incoming client
            req = json.dumps({"token": "Name"})
            client.sendall(bytes(req, encoding="utf-8"))

            # Receive the requested information and create a new player object
            res = json.loads(client.recv(MAX_MESSAGE_SIZE).decode("utf-8"))
            new_player = Player(res["name"], client, address)

            # Broadcast new player information
            broadcast_message({"token": "Player", "Name": res["name"], "Score": 0})

            game.player_manager.add_player(new_player)
            print("Incoming player name: " + res["name"])

            # Start a receiver thread for the new client
            receiver_thread = Thread(target=receiver_runner, args=(client,))
            receiver_thread.start()

        except:
            print("An error has occured when handling new client!")

def handle_message(data):
    message = json.loads(data)
    if message["token"] == "Name":
        tm = {"token": "Name", "name": "ClareKyleDamirAnnaKhanh"}
        broadcast_message(tm)

def broadcast_message(message):
    data = json.dumps(message)
    for player in game.player_manager.get_players():
        player.get_socket().sendall(bytes(data,encoding="utf-8"))

def start_server(new_game):
    global game
    global my_socket
    
    game = new_game
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST, PORT))
    my_socket.listen()

    find_players()

def close_socket():
    my_socket.close()
    
"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""