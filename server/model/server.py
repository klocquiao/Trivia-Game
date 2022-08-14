# Server.py
import socket
import json 
from threading import Thread
from .player import Player

HOST = "127.0.0.1"
PORT = 12345

NUMBER_OF_CLIENTS = 4
MAX_MESSAGE_SIZE = 4096  #max byte size

my_socket = None
game = None

def receiver_runner(client):
    while True:
        try:
            # Receive message from a client
            data = client.recv(MAX_MESSAGE_SIZE).decode("utf-8")
            handle_message(data)
        except:
            print("A client has disconnected! Exiting game...")
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
            game.player_manager.add_player(new_player)

            print("Incoming player name: " + res["name"])

            # Start a receiver thread for the new client
            receiver_thread = Thread(target=receiver_runner, args=(client,))
            receiver_thread.start()

        except socket.error as e: 
            print("An error has occured when handling new client!")

def handle_message(data):
    # Handle incoming messages from the client
    message = json.loads(data)
    if message["token"] == "Answer":
        print("Answer message received")
        game.current_round.check_player_answer(message)

def broadcast_message(message):
    # Broadcast message to all connected players
    data = json.dumps(message)
    for player in game.player_manager.get_players():
        player.get_socket().sendall(bytes(data,encoding="utf-8"))


def send_message(player, message):
    # Send message to a specific player
    data = json.dumps(message)
    player.get_socket().sendall(bytes(data,encoding="utf-8"))

def start_server(new_game):
    # Inject game object to make it accessible by server
    global game
    global my_socket
    game = new_game

    # Bind host to port and start listening for players
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST, PORT))
    my_socket.listen()

    # Wait for players to connect and create receiver threads for them
    find_players()

def close_server():
    my_socket.close()

