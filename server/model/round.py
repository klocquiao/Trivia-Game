NUMBER_OF_TURNS = 3

class Round:
    trivia = None
    turns = 0
    def __init__(self, trivia):
        self.trivia = trivia
    
    def start(self):
        while self.turns < NUMBER_OF_TURNS:
