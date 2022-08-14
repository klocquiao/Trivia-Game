class Player:
    '''Instantiates a Player with given name'''
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def __toStr__(self):
        return str(self.name)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def increment_score(self):
        self.score += 1

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

    def score_error_msg(self):
        return "Invalid Score: only integer."
