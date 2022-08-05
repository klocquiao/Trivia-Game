from .trivia_manager import TriviaManager
from .round import Round
from .player_manager import PlayerManager
from .player import Player
from .server import start_server

class Game:
    def __init__(self):
        tm = TriviaManager("./db.csv")
        self.trivia_set = tm.get_trivia_set()
        self.player_manager = PlayerManager()
        self.current_round = None

    def start(self):
        start_server(self)

        print("All players are present! Starting game...")
        while (len(self.trivia_set) > 0):
            self.current_round = Round(self.trivia_set.pop(), self.player_manager)
            self.current_round.start()
    
        winner = self.players.get_winner()
        print("The winner is " + winner.get_name()) 