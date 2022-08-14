# Game Lobby page 
import pygame, sys
from player import Player
from client import start_client
from client import new_player
from pygame.locals import *
from client import is_enough_player
from layout import main


# --------- Lobby page setup ---------
BLACK = (0,0,0)
WHITE = (255,255,255)
NAVYBLUE = (60,60,100) # bg color
ORANGE = (255,128,0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BOX_WIDTH = 230     # text input box
BOX_HEIGHT = 25     # text input box
display_lobby = True
at_lobby_page = True

lobby_page = 1

pygame.init()

screenSize = [SCREEN_WIDTH,SCREEN_HEIGHT] 
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('*** Trivia Game ***')

# manage how fast the screen updates
clock = pygame.time.Clock()
frame_rate = 60

font_large = pygame.font.SysFont('Calibri', 25, True, False)  
font_small = pygame.font.SysFont('Calibri', 20, True, False)  

# create input box:
input_box = pygame.Rect(SCREEN_WIDTH/2 - BOX_WIDTH/2, SCREEN_HEIGHT/2 - BOX_HEIGHT/2 , BOX_WIDTH, BOX_HEIGHT)
user_input = ''
box_active = False

# create ready button
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30
BUTTON_X = SCREEN_WIDTH/2 - BUTTON_WIDTH/2
BUTTON_Y = SCREEN_HEIGHT/2 + SCREEN_HEIGHT/4
ready_button = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
button_active = False
show_warning = False


# ============== Lobby Page Event loop ==============
run = True
while run and display_lobby: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # input is clicked
            if input_box.collidepoint(event.pos):
                box_active = True
                show_warning = False
            else:
                box_active = False

            # button is clicked
            if ready_button.collidepoint(event.pos):
                
                button_active = True
            else:
                button_active = False

        # button pressed up
        if event.type == pygame.MOUSEBUTTONUP:
            if ready_button.collidepoint(event.pos):
                if len(user_input) == 0:
                    show_warning = True
                else: 
                    #======== starts client socket and pass player data ======
                    player = Player(user_input)
                    new_player(player.get_name())
                    start_client()
                    if (is_enough_player()):
                        main() #open game page
                    else: 
                        at_lobby_page = False #direct to waiting page
                
                button_active = False

        if box_active:
            box_color = ORANGE  #highlight 
        else:
            box_color = WHITE

        if button_active:
            button_color = ORANGE
        else:
            button_color = WHITE

        if event.type == pygame.KEYDOWN:
            #allow input only when input box is active:
            if box_active:
                # handle user remove character:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[0: (len(user_input) - 1)]

                # handle any keys except ESCAPE key:
                elif event.key != pygame.K_ESCAPE:
                    if len(user_input) < 15:
                        user_input += event.unicode

    screen.fill(NAVYBLUE) #stay inside of while loop

    
    # must be with screen.fill in same level, and must be after it
    if at_lobby_page:
        # ------ Display Title ------
        title = font_large.render("*** Welcome to Trivia Game ***", True, ORANGE)
        title_center = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        screen.blit(title, title_center)

        # ----- Display Name Input ------
        name_label = font_large.render("Enter your name: ", True, WHITE)
        name_label_center = name_label.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5))
        screen.blit(name_label, name_label_center)

        name_text = font_small.render(user_input, True, WHITE)
        screen.blit(name_text, [input_box.x + 5, input_box.y])

        # ----- Display Input Box -------
        # draw input box to screen:
        pygame.draw.rect(screen, box_color, input_box, 2)

        #------ Display Ready button ------
        pygame.draw.rect(screen, button_color, ready_button)
        
        ready_text = font_small.render("Ready", True, BLACK)
        ready_text_center = ready_text.get_rect(center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y + BUTTON_HEIGHT/2))
        screen.blit(ready_text, ready_text_center)
        
        #------ Display warning ------
        if show_warning:
            warning = font_small.render("Please enter a name.", True, WHITE)
            screen.blit(warning, [input_box.x + input_box.width + 10, input_box.y])


# ================== Waiting Page ==================
    if at_lobby_page == False:
        title = font_large.render("*** Please wait here for other players connected. ***", True, ORANGE)
        title_center = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        screen.blit(title, title_center)
        if (is_enough_player()):
            main()


    # update game state
    pygame.display.update()    
    clock.tick(frame_rate)





