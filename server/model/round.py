from .trivia import Trivia

NUMBER_OF_TURNS = 3

class Round:
    def __init__(self, trivia, players):
        self.trivia = trivia
        self.trivia.shuffle_answers()
        self.players = players
        self.turns = 0

    def start(self):
        while self.turns < NUMBER_OF_TURNS:
            self.trivia.print_answers()
            print("Input your answer!")
            user_choice = input()

            while self.trivia.get_answer(int(user_choice)).check_is_used():
                print("Answer has already been used!")
                user_choice = input()

            self.trivia.get_answer(int(user_choice)).set_to_used()
            if self.trivia.get_answer(int(user_choice)).check_is_correct():
                self.players.get_player(0).increment_score()
                print("Correct!")
            else:
                print("Incorrect!")

            self.turns += 1