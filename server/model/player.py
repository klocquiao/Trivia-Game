# player class
# from select import select


class Player():
    '''Instantiates a Player with given name'''
    def __init__(self, name):
        self._name = name
        self._score = 0
        self._isActive = False     # to keep track whether player is in the current game
        self._isConnected = False  #to keep track whether player connects to socket
    
    def __toStr__(self):
        return str(self.name)

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score
    
    def is_active(self):
        return self._isActive

    def is_connected(self):
        return self._isConnected

    # Set methods: 
    def set_name(self, newName):
        if isinstance(newName, str) == False: #check if name is string
            newName = str(newName)
        self._name = newName

    def set_score(self, newScore):
        if isinstance(newScore, int) == False:
            self.scoreErrorMsg()
        else:
            self._score = newScore

    def set_to_active(self):
        self._isActive = True

    def set_to_connected(self):
        self._isConnected = True

    def score_error_msg(self):
        return "Invalid Score: only integer."

    ''' Might be more methods implemented later...'''