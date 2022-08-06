class PlayerManager:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)

    def find_player(self, name):
        return filter(lambda x: str(x) == name, self.players)
        
    def get_player(self, index):
        return self.players[index]

    def get_players(self):
        return self.players

    def get_player_names(self):
        return list(map(lambda x: str(x), self.players))

    def get_winner(self):
        winner = self.players[0]
        for player in self.players:
            if (player.get_score() > winner.get_score()):
                winner = player
                
        return winner

    def get_number_of_players(self):
        return len(self.players)
    
    def reset_players_state(self):
        for player in self.players:
            player.set_is_chosen(False)

    def is_players_ready(self):
        for player in self.players:
            if not player.is_chosen():
                return False
        
        return True