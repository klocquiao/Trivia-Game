class Player:
    '''Instantiates a Player with given name'''
    def __init__(self, name, socket, addr):
        self.name = name
        self.socket = socket
        self.addr = addr
        self.score = 0
        self.is_active = False     # to keep track whether player is in the current game
    
    def __toStr__(self):
        return str(self.name)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1

    def is_active(self):
        return self.is_active

    def set_score(self, newScore):
        if isinstance(newScore, int) == False:
            self.scoreErrorMsg()
        else:
            self.score = newScore

    def set_activity(self, bool):
        self.is_active = bool

    def score_error_msg(self):
        return "Invalid Score: only integer."

    ''' Might be more methods implemented later...'''
