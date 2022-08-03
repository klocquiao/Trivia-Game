class Player:
    '''Instantiates a Player with given name'''
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.is_active = False     # to keep track whether player is in the current game
        self.is_connected = False  #to keep track whether player connects to socket
        self.socket = None
    
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

    def is_connected(self):
        return self.is_connected

    # Set methods: 
    def set_name(self, newName):
        if isinstance(newName, str) == False: #check if name is string
            newName = str(newName)
        self.name = newName

    def set_score(self, newScore):
        if isinstance(newScore, int) == False:
            self.scoreErrorMsg()
        else:
            self.score = newScore

    def set_to_active(self):
        self.is_active = True

    def set_to_connected(self):
        self.is_connected = True

    def score_error_msg(self):
        return "Invalid Score: only integer."

    ''' Might be more methods implemented later...'''
