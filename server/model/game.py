from server.model.trivia_manager import TriviaManager
from server.model.round import Round
from server.model.player_manager import PlayerManager

class Game:
    def __init__(self):
        tm = TriviaManager("../db.csv")
        self.trivia_set = tm.getTriviaSet()
        self.players = PlayerManager()
        
        while (len(self.players) < 4):
            print("Waiting for server to find players...")
        

    def start(self):
        while (len(self.trivia_set) > 0):
            new_round = Round(self.trivia_set.pop())
            new_round.start()
    
        winner = self.players.get_winner()
        print("The winner is " + self.winner.get_name()) 