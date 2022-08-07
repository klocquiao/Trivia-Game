from threading import Thread, Lock

mutex = Lock()

class Answer:
    def __init__ (self, answer, is_correct):
        self.answer = answer
        self.is_correct = is_correct
        self.is_available = True

    def __str__(self):
        return self.answer
    
    def check_available(self):
        mutex.acquire()
        temp = self.is_available
        if self.is_available:
            self.is_available = False
        mutex.release()

        return temp


    def check_is_correct(self):
        return self.is_correct