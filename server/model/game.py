from .trivia_manager import TriviaManager
from .round import Round
from .player_manager import PlayerManager
from .player import Player

NUMBER_OF_PLAYERS = 4

class Game:
    def __init__(self):
        tm = TriviaManager("./db.csv")
        self.trivia_set = tm.get_trivia_set()
        self.player_manager = PlayerManager()
        self.current_round = None

        while (self.player_manager.get_number_of_players() < NUMBER_OF_PLAYERS):
            print("Waiting for server to find players...")

    def start(self):
        while (len(self.trivia_set) > 0):
            self.current_round = Round(self.trivia_set.pop(), self.players)
            self.current_round.start()
    
        winner = self.players.get_winner()
        print("The winner is " + winner.get_name()) 