import pygame, sys
from pygame.locals import *

# sys.path.append('.')
# sys.path.append('../server/model')
import player
from game_over import open_game_over

FPS = 30 # frames per second, the general speed of the program
WINDOW_WIDTH = 700 # size of window's width in pixels
WINDOW_HEIGHT = 500 # size of windows' height in pixels
BOX_WIDTH = 150 # size of box's width in pixels
BOX_HEIGHT = 50 # size of box's height in pixels
GAP_SIZE = 20 # size of gap between boxes in pixels
TOTAL_COLUMNS = 4 # number of row of boxes
TOTAL_ROWS = 4 # number of column of boxes
XMARGIN = int((WINDOW_WIDTH - (TOTAL_COLUMNS * (BOX_WIDTH + GAP_SIZE))) / 2) + 10 # Center horizontal 
YMARGIN = int((WINDOW_HEIGHT - (TOTAL_ROWS * (BOX_HEIGHT + GAP_SIZE))) / 2) # Center vertical


#            R    G    B
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
GREY     = (105, 105, 105)


BG_COLOR = NAVYBLUE
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE
RIGHT_ANSWER_COLOR = GREY

# TEST DATA 
QUESTION = "Which of the following are fruit?"
ALL_ANSWERS = ('Pear', 'Apple', 'Mango', 'Peach',
            'Cherry', 'Durian', 'Orange', 'Lime',
            'Tomato', 'Pepper', 'Coconut', 'Pumpkin',
            'Eggplant', 'Cucumber', 'Avocado', 'Olive'
            )
# RIGHT_ANSWERS = ('Pear', 'Apple', 'Mango')


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('CMPT371 Project')

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event

    main_answer_board = generate_answer_board()
    is_pressed_answer_boxes = generate_is_pressed_answer(False)

    DISPLAYSURF.fill(BG_COLOR)

    # Handle time
    counter = 10 # Set default time out to 10
    time_delay = 1000 # 1000 = 1s
    time_event = pygame.USEREVENT+1
    pygame.time.set_timer(time_event, time_delay)

    # Handle turn
    turn = 1

    # Declare player list
    player_list = generate_player_list()

    while True: # main game loop
        mouse_pressed = False

        DISPLAYSURF.fill(BG_COLOR) # drawing the window
        draw_answer_board(main_answer_board, is_pressed_answer_boxes, counter, turn, player_list)

        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if counter == 0:
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    pygame.time.set_timer(time_event, time_delay)
                    counter = 10
                mousex, mousey = event.pos
                mouse_pressed = True
            elif event.type == time_event:
                counter -= 1
                if counter == 0: # If time out then reset layout 
                    pygame.time.set_timer(time_event, 0) # Stop the timer
                    turn += 1

                    # open_game_over()    # once winner is ready -------- still under testing

        boxx, boxy = get_box_at_pixel(mousex, mousey) # Column, row of answer_board. Index is from 0
        if boxx != None and boxy != None: # If user touch answer box inside answer_board
            if not is_pressed_answer_boxes[boxx][boxy]: # If user only touch, not pressed
                draw_highlight_box(boxx, boxy)
            if not is_pressed_answer_boxes[boxx][boxy] and mouse_pressed: # When user pressed and choose correct answer
                is_pressed_answer_boxes[boxx][boxy] = True
                player_list[0].increment_score()
       
        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generate_player_list():
    player1 = player.Player('Player 1')
    player2 = player.Player('Player 2')
    player3 = player.Player('Player 3')
    player4 = player.Player('Player 4')
    player_list = [player1, player2, player3, player4]
    return player_list

def generate_answer_board():
    # Create the board data structure, with answer options
    board = []
    answer = list(ALL_ANSWERS) # Copy all answer options
    for x in range(TOTAL_ROWS):
        column = []
        for y in range(TOTAL_COLUMNS):
            column.append(answer[0])
            del answer[0] # remove after assign
        board.append(column)
    return board

def generate_is_pressed_answer(val):
    # To check whether a answer box is pressed
    is_pressed_answer_boxes = []
    for i in range(TOTAL_COLUMNS):
        is_pressed_answer_boxes.append([val] * TOTAL_ROWS)
    return is_pressed_answer_boxes

def draw_answer_board(board, pressed, counter, turn, player_list):
    font = pygame.font.Font(None, 20)
    # Display question text
    display_textbox_horizontal(QUESTION, 20, WHITE, 80)

    # Display time button
    # Change time format to second
    counter = str(counter)
    if (counter == '10'): 
        counter = '00:' + counter
    else: 
        counter = '00:0' + counter
    display_text(counter, 20, WHITE, (WINDOW_WIDTH - XMARGIN - BOX_WIDTH, 400, BOX_WIDTH, BOX_HEIGHT))

    # Display turn button
    turn = 'Turn: ' + str(turn)
    display_text(turn, 20, WHITE, (XMARGIN, 400, BOX_WIDTH, BOX_HEIGHT))

    # Draws all of the boxes in their pressed or not pressed state.
    BOX_COLOR = WHITE
    for boxx in range(TOTAL_ROWS):
        for boxy in range(TOTAL_COLUMNS):
            left, top = left_top_coords_of_box(boxx, boxy)
            if not pressed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, BOX_WIDTH, BOX_HEIGHT))
            else: # Assume pressed = right answer
                pygame.draw.rect(DISPLAYSURF, RIGHT_ANSWER_COLOR, (left, top, BOX_WIDTH, BOX_HEIGHT))

            answer_text = get_answer_value(board, boxx, boxy)
            draw_answer_text(answer_text, boxx, boxy)
    
    # Draw player list
    left = XMARGIN
    top = 30
    for index, player in enumerate(player_list):
        player_score_str = player_list[index].get_name() + ': '+ str(player.get_score())
        display_text(player_score_str, 20, WHITE, (left, 30, BOX_WIDTH, BOX_HEIGHT))
        left += (GAP_SIZE + BOX_WIDTH)

def left_top_coords_of_box(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOX_WIDTH + GAP_SIZE) + XMARGIN
    top = boxy * (BOX_HEIGHT + GAP_SIZE) + YMARGIN
    return (left, top)

def get_box_at_pixel(x, y):
    for boxx in range(TOTAL_ROWS):
        for boxy in range(TOTAL_COLUMNS):
            left, top = left_top_coords_of_box(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def get_answer_value(board, boxx, boxy):
    return board[boxy][boxx]

def draw_answer_text(answer, boxx, boxy):
    half =    int(BOX_HEIGHT * 0.5)  # syntactic sugar
    left, top = left_top_coords_of_box(boxx, boxy) # get pixel coords from board coords
    display_text(answer, 20, BLACK, (left + 10, top, 100, half))


def draw_highlight_box(boxx, boxy):
    left, top = left_top_coords_of_box(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHT_COLOR, (left - 5, top - 5, BOX_WIDTH + 10, BOX_HEIGHT + 10), 4)

def display_textbox_horizontal (string, font_size, font_color, paddingTop):
    font = pygame.font.Font(None, font_size)
    text = font.render(string, True, font_color)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, paddingTop))
    DISPLAYSURF.blit(text, text_rect)

def display_text (string, font_size, font_color, position):
    font = pygame.font.Font(None, font_size)
    text_rect = pygame.Rect(position)
    text_value = font.render(string, True, font_color)
    DISPLAYSURF.blit(text_value, (text_rect.x, text_rect.y))

    
if __name__ == '__main__':
    main()
