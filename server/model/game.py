from .trivia_manager import TriviaManager
from .round import Round
from .player_manager import PlayerManager
from .player import Player
from .server import broadcast_message, start_server

class Game:
    def __init__(self):
        tm = TriviaManager("./db.csv")
        self.trivia_set = tm.get_trivia_set()
        self.player_manager = PlayerManager()
        self.current_round = None

    def start(self):
        start_server(self)

        print("All players are present! Starting game...")
        
        round_number = 1
        while (len(self.trivia_set) > 0):
            trivia = self.trivia_set.pop()
            broadcast_message({"token" : "Round", "number": round_number, "question" : trivia.get_question(), "answers": trivia.get_answers()})

            self.current_round = Round(trivia, self.player_manager)
            self.current_round.start()

            rounds += 1
    
        winner = self.players.get_winner()
        print("The winner is " + winner.get_name())  