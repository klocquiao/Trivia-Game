from .trivia import Trivia
from .server import broadcast_message, send_message, start_server
import threading

NUMBER_OF_TURNS = 3

class Round:
    def __init__(self, trivia, players):
        self.trivia = trivia
        self.trivia.shuffle_answers()
        self.players = players
        self.turns = 0
        self.round_event = threading.Event()

    def start(self):
        while self.turns < NUMBER_OF_TURNS:
            broadcast_message({"token" : "Turn", "number" : self.turns})
            self.round_event.wait()

            self.turns += 1
            self.round_event.clear()
    
    def check_player_choice(self, message):

        # Need mutexes here
        player_choice = message["answer"]
        player = self.players.find_player(message["name"])
        
        # Player was able to access shared object
        if (self.trivia.get_answer(player_choice).check_usage()):
            player.set_is_chosen = True

            if (self.trivia.get_answer(player_choice).check_is_correct()):
                player.increment_score()
                broadcast_message({"token": "Player", "Name": player.get_name(), "Score": player.get_score()})

        else:
            send_message(player, {"token": "reject"})

        if self.players.is_players_ready():
            self.players.reset_player_state()
            self.round_event.set()