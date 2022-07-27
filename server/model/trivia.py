from answer import Answer

class Trivia:

    def __init__ (self, question):
        self.question = question
        self.answers = [Answer()]
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def check_answer(self, index):
        self.answers[index].set_to_used()
        return self.answers[index].check_correct()