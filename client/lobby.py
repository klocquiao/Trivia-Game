import pygame, sys
from pygame.locals import *


# --------- Game setup ---------
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255, 128, 0)

pygame.init()

scrrenSize = [800,800] 
screen = pygame.display.set_mode(scrrenSize)
pygame.display.set_caption('*** Trivia Game ***')



# ======================   ======================
font = pygame.font.SysFont('Calibri', 25, True, False)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()
frame_rate = 60  


user_input = ''

# create input box:
input_box = pygame.Rect(300,300,150, 25)

# color_active = pygame.Color("lightskyblue")


active = False

# ========= Handle Event loop =======
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True

            else:
                active = False

        if active:
            color = ORANGE
        else:
            color = WHITE

        # print("--- active:", active)

        if event.type == pygame.KEYDOWN:
            
            # handle user remove character:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                # user_input = user_input[0: (len(user_input) - 1)]
                print(user_input)

            # handle any keys except ESCAPE key:
            elif event.key != pygame.K_ESCAPE:
                user_input += event.unicode
                print(user_input)

    screen.fill(BLACK) #stay inside of while loop


    # if active:
    #     color = color_active

    # input box draws on screen
    pygame.draw.rect(screen, color, input_box, 2)

    name_text = font.render(user_input, True, WHITE)
    screen.blit(name_text, [input_box.x + 5, input_box.y])


    # must be with screen.fill in same level, and must be after it
    # ------ Display Title ------
    # font = pygame.font.SysFont('Calibri', 25, True, False)
    font = pygame.font.Font(None, 32)
    title = font.render("*** Welcome to Trivia Game ***", True, ORANGE)
    screen.blit(title, [200,200])

    # ----- Name Input ------
    namelabel = font.render("Enter your name: ", True, WHITE)
    screen.blit(namelabel, [100, 300])

    
    # update game state
    pygame.display.update()
    
    clock.tick(frame_rate)
