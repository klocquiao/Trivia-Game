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

    def getName(self):
        return self._name

    def getScore(self):
        return self._score
    
    def isActive(self):
        return self._isActive

    def isConnected(self):
        return self._isConnected

    # Set methods: 
    def setName(self, newName):
        if isinstance(newName, str) == False: #check if name is string
            newName = str(newName)
        self._name = newName

    def setScore(self, newScore):
        if isinstance(newScore, int) == False:
            self.scoreErrorMsg()
        else:
            self._score = newScore

    def setToActive(self):
        self._isActive = True

    def setToConnected(self):
        self._isConnected = True

    def scoreErrorMsg(self):
        return "Invalid Score: only integer."

    ''' Might be more methods implemented later...'''