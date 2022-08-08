from .answer import Answer
import random

class Trivia:
    def __init__ (self, question):
        self.question = question
        self.answers = []

    def get_question(self):
        return self.question

    def get_answers(self):
        return self.answers

    def get_answers_str(self):
        return list(map(lambda x: str(x), self.answers))

    def shuffle_answers(self):
        random.shuffle(self.answers)
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def get_answer(self, index):
        return self.answers[index]  

    def print_answers(self):
        print(self.answers)

