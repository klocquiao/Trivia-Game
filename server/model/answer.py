class Answer:
    def __init__ (self, answer, is_correct):
        self.answer = answer
        self.is_correct = is_correct
        self.is_used = False

    def __repr__(self):
        return self.answer

    def set_to_used(self):
        self.is_used = True
    
    def check_is_correct(self):
        return self.is_correct

    def check_is_used(self):
        return self.is_used