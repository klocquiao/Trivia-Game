from answer import Answer
import random

class Trivia:
    def __init__ (self, question):
        self.question = question
        self.answers = [Answer()]

    def shuffle_trivia(self):
        random.shuffle(self.answers)
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def get_answer(self, index):
        return self.answers[index]

