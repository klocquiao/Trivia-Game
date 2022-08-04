from model.game import Game
from model.server import start_server

if __name__ == '__main__':
    new_game = Game()
    start_server(new_game)
    new_game.start()