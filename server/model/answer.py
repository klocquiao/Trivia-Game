from threading import Thread, Lock

mutex = Lock()

class Answer:
    def __init__ (self, answer, is_correct):
        self.answer = answer
        self.is_correct = is_correct
        self.is_used = False

    def __repr__(self):
        return self.answer
    
    def check_usage(self):
        mutex.acquire()
        if not self.is_used:
            self.is_used = True
        mutex.release()

    def check_is_correct(self):
        return self.is_correct