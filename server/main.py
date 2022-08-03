from model.game import Game
import model.server
from server.model.server import start_receiver, start_server

if __name__ == '__main__':
    start_server()
    new_game = Game()
    new_game.start()