from server.model.trivia import Trivia

NUMBER_OF_TURNS = 3

class Round:
    def __init__(self, trivia, pm):
        self.trivia = trivia
        self.turns = 0
        self.players = pm
    
    def start(self):
        while self.turns < NUMBER_OF_TURNS:
            user_choice = input()
            while (not self.trivia.check_valid(int(user_choice))):
                print("Answer has already been used!")
                user_choice = input()

            self.trivia.disable_answer(int(user_choice))
            if (self.trivia.check_answer(int(user_choice))):
                self.players.get_player(0).increment_score()
            
            
            self.turns += 1