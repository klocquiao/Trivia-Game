from .trivia import Trivia
from .server import broadcast_message, start_server
import threading

NUMBER_OF_TURNS = 3

class Round:
    def __init__(self, trivia, players):
        self.trivia = trivia
        self.trivia.shuffle_answers()
        self.players = players
        self.turns = 0
        self.round_event = threading.Event()

    def start(self):
        while self.turns < NUMBER_OF_TURNS:
            broadcast_message({"token" : "Turn", "number" : self.turns})
            round_in_progress = self.round_event.wait()



            # self.trivia.print_answers()
            # print("Input your answer!")
            # user_choice = input()


            self.turns += 1
    
    def check_player_choice(self, message):
        player_choice = message["answer"]
        player = self.players.find_player(message["name"])
        
        if (self.trivia.get_answer(player_choice).check_is_correct()):
            player.increment_score()
            broadcast_message({"token": "Player", "Name": player.get_name(), "Score": player.get_score()})
        # while self.trivia.get_answer(int(user_choice)).check_is_used():
        #     print("Answer has already been used!")
        #     user_choice = input()

        # self.trivia.get_answer(int(user_choice)).set_to_used()
        # if self.trivia.get_answer(int(user_choice)).check_is_correct():
        #     self.players.get_player(0).increment_score()
        #     print("Correct!")
        # else:
        #     print("Incorrect!")
