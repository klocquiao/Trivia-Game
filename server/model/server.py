import socket
import json 
import threading
from .game import Game

from .player import Player
HOST = "127.0.0.1"
PORT = 12345

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((HOST, PORT))
my_socket.listen()

game = None

def receiver_runner(client):
    while True:
        try:
            data = client.recv(1024).decode("utf-8")
            handle_message(data)
        except:
            print("An error has occured!")
            my_socket.close()

def connection_runner():
    global game
    while True:
        # Accept incoming client
        client, address = my_socket.accept()

        # Request a alias for the incoming client
        req = json.dumps({"token": "Name"})
        client.sendall(bytes(req, encoding="utf-8"))

        # Receive the requested information and create a new player object
        res = client.recv(1024).decode("utf-8")
        new_player = Player(res["Name"], client, address)
        game.player_manager.add_player(new_player)

        # Start a receiver thread for the new client
        receiver_thread = threading.thread(target=receiver_runner)
        receiver_thread.start()

def handle_message(data):
    global game
    if data == "test":
        tm = {"token": "Test", "message": "Hello world!"}
        broadcast_message(tm)

def broadcast_message(message):
    data = json.dumps(message)
    for player in game.player_manager.get_players():
        player.get_socket().sendall(bytes(data,encoding="utf-8"))

def start_server(new_game):
    global game
    game = new_game
    connection_thread = threading.thread(target=connection_runner)
    connection_thread.start()

def close_socket():
    my_socket.close()
    
"""
Token setup:
    - Json
    - Format: {Token: String, Data:....}
"""