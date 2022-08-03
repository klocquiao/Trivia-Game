from model.game import Game
import model.server
from server.model.server import start_receiver

if __name__ == '__main__':
    start_receiver()
    new_game = Game()
    new_game.start()