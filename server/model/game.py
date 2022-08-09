from .trivia_manager import TriviaManager
from .round import Round
from .player_manager import PlayerManager
from .player import Player
from .server import broadcast_message, start_server, close_server
import time

class Game:
    def __init__(self):
        tm = TriviaManager("./db.csv")
        self.trivia_set = tm.get_trivia_set()
        self.player_manager = PlayerManager()
        self.current_round = None
        self.rounds = 1

    def start(self):
        start_server(self)

        print("All players are present! Starting game in 3 seconds")

        # Broadcast finalized player array
        broadcast_message({"token": "Players", "players": self.player_manager.get_players_str()})
        
        # while (len(self.trivia_set) > 0):
        #     time.sleep(3)

        #     trivia = self.trivia_set.pop()
        #     broadcast_message({"token" : "Round", "number": self.rounds, "question" : trivia.get_question(), "answers": trivia.get_answers_str()})
        #     print("Round " + str(self.rounds))

        #     self.current_round = Round(trivia, self.player_manager)
        #     self.current_round.start()

        #     self.rounds += 1

        # winner = self.player_manager.get_winner()
        winner = self.players.get_winner()
        print("The winner is " + winner.get_name())

        broadcast_message({"token" : "Result", "winner": winner.get_name()})
        # broadcast_message({"token" : "Result", "winner": "KittyCat"})

        close_server()
