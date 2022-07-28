class PlayerManager:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
    
    def get_player(self, index):
        return self.players[index]
    
    def get_winner(self):
        winner = self.players[0]
        for player in self.players:
            if (player.get_score() > winner.get_score()):
                winner = player
        
        return winner

    def get_number_of_players(self):
        return len(self.players)