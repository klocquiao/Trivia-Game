class Player:
    nickname = ""
    score = 0
    player_socket = None
    is_ready = False
    
    def __init__(self, socket):
        self.player_socket = socket
    
    def readyUp(self, nickname):
        self.nickname = nickname
        self.is_ready = True