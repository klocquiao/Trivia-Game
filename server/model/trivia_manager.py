import csv
import random
from .trivia import Trivia
from .answer import Answer

NUMBER_OF_ROUNDS = 2

class TriviaManager:
    def __init__(self, filename):
        self.trivia_list = []
        with open(filename, newline='') as csvfile:
            trivia_reader = csv.DictReader(csvfile)

            question = ""
            count = -1
            for row in trivia_reader:
                if row["question"] != question:
                    new_trivia = Trivia(row["question"])
                    self.trivia_list.append(new_trivia)
                    count+1
                    question = row["question"]

                new_answer = Answer(row["answer"], eval(row["correct?"]))
                self.trivia_list[count].add_answer(new_answer)

    def get_trivia_set(self):
        random.shuffle(self.trivia_list)
        return self.trivia_list[:NUMBER_OF_ROUNDS + 1]

    def debug_trivia_list(self):
        for item in self.trivia_list:
            print(item)
