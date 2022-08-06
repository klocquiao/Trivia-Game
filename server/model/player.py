import socket

class Player:
    '''Instantiates a Player with given name'''
    def __init__(self, name, socket, addr):
        self.name = name
        self.socket = socket
        self.addr = addr
        self.score = 0
        self.is_chosen = False     # to keep track whether player is in the current game
    
    def __toStr__(self):
        return str(self.name)

    def get_name(self):
        return self.name

    def get_socket(self):
        return self.socket

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1

    def is_chosen(self):
        return self.is_chosen

    def set_score(self, newScore):
        if isinstance(newScore, int) == False:
            self.scoreErrorMsg()
        else:
            self.score = newScore

    def set_is_chosen(self, val):
        self.is_chosen = val

    def score_error_msg(self):
        return "Invalid Score: only integer."

    ''' Might be more methods implemented later...'''
