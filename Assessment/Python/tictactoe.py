import pygame
import sys
import time
from pygame.locals import *
pygame.init()

# show the starting variables 
xo = 'x'
winner = None 
draw = None

# settings like colours and screen width or height
width = 400
height = 400
bg = (255, 255,255)
line = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]

pygame.display.set_caption("Tic Tac Toe")

# infrastructural settings
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height + 100), 0, 32)

# load images as Python objects
x_img = pygame.image.load(r'C:\Users\ciara\2021-T3-Assessment\Assessment\Python\Sprites\x_icon.png')
o_img = pygame.image.load(r'C:\Users\ciara\2021-T3-Assessment\Assessment\Python\Sprites\o_icon.png')

# set image size 
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))

# start game
def game_initiating_window():
    screen.fill(bg)
    
# vertical lines
    pygame.draw.line(screen, line, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
   
# horizontal lines
    pygame.draw.line(screen, line, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, line, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global draw

# winner & loser message
    if winner is None:
        message = xo.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    font = pygame.font.Font(None, 30)

    text = font.render(message, 1, (255, 255, 255))

    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center =(width / 2, 500-50))
    screen.blit(text, text_rect)
    pygame.display.update()

def check_win():
    global board, winner, draw
   
    # checking for winning rows
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(screen, (250, 0, 0),
                         (0, (row + 1)*height / 3 -height / 6),
                         (width, (row + 1)*height / 3 - height / 6 ),
                         4)
            break
   
    # checking for winning columns
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), \
                          ((col + 1)* width / 3 - width / 6, height), 4)
            break
   
    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
          
        # game won diagonally left to right
        winner = board[0][0]
        pygame.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
          
        # game won diagonally right to left
        winner = board[0][2]
        pygame.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4)
   
    if(all([all(row) for row in board]) and winner is None ):
        draw = True
    draw_status()

def drawxo(row, col):
    global board, xo
      
    # for the first row, the image
    # should be pasted at a x coordinate
    # of 30 from the left margin
    if row == 1:
        posx = 30
          
    # for the second row, the image 
    # should be pasted at a x coordinate 
    # of 30 from the game line     
    if row == 2:
  
        # margin or width / 3 + 30 from 
        # the left margin of the window
        posx = width / 3 + 30
          
    if row == 3:
        posx = width / 3 * 2 + 30
   
    if col == 1:
        posy = 30
          
    if col == 2:
        posy = height / 3 + 30
      
    if col == 3:
        posy = height / 3 * 2 + 30
          
    # setting up the required board 
    # value to display
    board[row-1][col-1] = xo
      
    if(xo == 'x'):
          
        # pasting x_img over the screen 
        # at a coordinate position of
        # (pos_y, posx) defined in the
        # above code
        screen.blit(x_img, (posy, posx))
        xo = 'o'
      
    else:
        screen.blit(o_img, (posy, posx))
        xo = 'x'
    pygame.display.update()
   
def user_click():
    # get coordinates of mouse click
    x, y = pygame.mouse.get_pos()
   
    # get column of mouse click (1-3)
    if(x<width / 3):
        col = 1
      
    elif (x<width / 3 * 2):
        col = 2
      
    elif(x<width):
        col = 3
      
    else:
        col = None
   
    # get row of mouse click (1-3)
    if(y<height / 3):
        row = 1
      
    elif (y<height / 3 * 2):
        row = 2
      
    elif(y<height):
        row = 3
      
    else:
        row = None
        
    # after getting the row and col, 
    # we need to draw the images at
    # the desired positions
    if(row and col and board[row-1][col-1] is None):
        global xo
        drawxo(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    xo = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

game_initiating_window()

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            user_click()
            if(winner or draw):
                reset_game()
    pygame.display.update()
    clock.tick(fps)