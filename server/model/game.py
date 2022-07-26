from server.model.trivia_manager import TriviaManager
from server.model.trivia_manager import Round

class Game:
    trivia_set = []
    players = []

    def __init__(self):
        tm = TriviaManager("../db.csv")
        self.trivia_set = tm.getTriviaSet()
        
        while (len(self.players) < 4):
            print("Waiting for server to find players...")
        

    def startGame(self):
        while (len(self.trivia_set) > 0):
            new_round = Round(self.trivia_set.pop())