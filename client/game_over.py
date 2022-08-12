# Game over
import pygame, sys
import client
from pygame.locals import *

# --------- page setup ---------
BLACK = (0,0,0)
WHITE = (255,255,255)
NAVYBLUE = (60,60,100) # bg color
ORANGE = (255,128,0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screenSize = [SCREEN_WIDTH,SCREEN_HEIGHT] 
screen = pygame.display.set_mode(screenSize)

pygame.init()
# manage how fast the screen updates
clock = pygame.time.Clock()
frame_rate = 60


def open_game_over():
# def open_game_over(winner_param):
    while True:
        font_large = pygame.font.SysFont('Calibri', 25, True, False)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # update game state
        pygame.display.update()
        clock.tick(frame_rate)

        screen.fill(NAVYBLUE) 
        # ----------- Display Winner -----------
        winner_param = client.get_winner_name()
        title = font_large.render(f"*** Player {winner_param} Won! ***", True, ORANGE)
        title_center = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        screen.blit(title, title_center)

        # ----------- Display game over --------
        game_over_text = font_large.render("Game over.", True, ORANGE)
        game_over_text_center = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(game_over_text, game_over_text_center)

    