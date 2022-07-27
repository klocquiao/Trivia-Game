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
            while (not self.trivia.get_answer(int(user_choice)).check_is_used()):
                print("Answer has already been used!")
                user_choice = input()

            self.trivia.get_answer(int(user_choice)).set_to_used()
            if (self.trivia.get_answer(int(user_choice)).check_is_correct()):
                self.players.get_player(0).increment_score()
            
            
            self.turns += 1