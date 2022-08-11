# Round.py

from .trivia import Trivia
from .server import broadcast_message, send_message, start_server
import threading
import time 
NUMBER_OF_TURNS = 3

class Round:
    def __init__(self, trivia, players):
        self.trivia = trivia
        self.players = players
        self.turns = 1
        self.round_event = threading.Event()

    def start(self):
        while self.turns <= NUMBER_OF_TURNS:
            time.sleep(3)
            print("Starting turn " + str(self.turns))

            broadcast_message({"token" : "Turn", "number" : self.turns})
            self.round_event.wait()

            self.turns += 1
            self.round_event.clear()

    def check_player_answer(self, message):
        # Need mutexes here
        player_choice = int(message["answer"])
        print("Received player choice", player_choice)
        player = self.players.find_player(message["name"])
        print("player_name: ", player)
        
        # Player was able to access shared object
        if (self.trivia.get_answer(player_choice).check_available()):
            player.set_is_chosen(True)

            if (self.trivia.get_answer(player_choice).check_is_correct()):
                player.increment_score()

            print(player.get_name() + " obtained answer " + str(self.trivia.get_answer(player_choice)))
            broadcast_message({"token": "Player", "answer": player_choice, "name": player.get_name(), "score": player.get_score()})

        else:
            print(player.get_name() + " failed race condition for " + str(self.trivia.get_answer(player_choice)))
            send_message(player, {"token": "Locked"})

        if self.players.is_players_ready():
            self.players.reset_players_state()
            self.round_event.set()

