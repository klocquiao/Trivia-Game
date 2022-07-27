class Answer:

    def __init__ (self, answer, isCorrect):
        self.answer = answer
        self.isCorrect = isCorrect
        self.isUsed = False

    def set_to_used(self):
        self.isUsed = True
    
    def check_is_correct(self):
        return self.isCorrect

    def check_is_used(self):
        return self.isUsed