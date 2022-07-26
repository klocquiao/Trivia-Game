class Answer:

    def __init__ (self, answer, isCorrect):
        self.answer = answer
        self.isCorrect = isCorrect
        self.isUsed = False

    def setToUsed(self):
        self.isUsed = True

    


