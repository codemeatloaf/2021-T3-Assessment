# Source Python Code: https://github.com/daliborstakic/tictactoe-pygame/blob/master/main.py
import pygame
import math
from pygame.constants import KEYDOWN, K_ESCAPE
pygame.init()
# screen settings
WIDTH <- 300
ROWS <- 3
win <- pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")
# colour settigns
WHITE <- (255, 255, 255)
BLACK <- (0, 0, 0)
GRAY <- (200, 200, 200)
RED <- (255, 0, 0)
BLUE <- (0, 0, 255)
# loading x an o as an image
X_IMAGE <- pygame.transform.scale(pygame.image.load(r"C:\Users\ciara\2021-T3-Assessment\Assessment\Python\Sprites\x_icon.png"), (80, 80))
                      ENDFOR
O_IMAGE <- pygame.transform.scale(pygame.image.load(r"C:\Users\ciara\2021-T3-Assessment\Assessment\Python\Sprites\o_icon.png"), (80, 80))
                      ENDFOR
# fonts
END_FONT <- pygame.font.SysFont('arial', 40)
# drawing the gaps between the lines
FUNCTION draw_grid():
    gap <- WIDTH // ROWS
# set starting 
    x <- 0
    y <- 0
    for i in range(ROWS):
        x <- i * gap
        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0, x), (WIDTH, x), 3)
ENDFUNCTION

    ENDFOR
FUNCTION initialize_grid():
    dis_to_cen <- WIDTH // ROWS // 2
    # initializing the array
    game_array <- [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x <- dis_to_cen * (2 * j + 1)
            y <- dis_to_cen * (2 * i + 1)
            # adding centre coordinates
            game_array[i][j] <- (x, y, "", True)
    ENDFOR
        ENDFOR
    RETURN game_array
# defines what happens when clicks
ENDFUNCTION

  ENDFUNCTION

FUNCTION click(game_array):
    global x_turn, o_turn, images
    # find mouse position
    m_x, m_y <- pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play <- game_array[i][j]
            # distance between mouse AND the centre of the square
            dis <- math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            # IF inside the squares
              ENDIF
            IF dis < WIDTH // ROWS // 2 AND can_play:
                IF x_turn:  # IF it's x's turn
                    images.append((x, y, X_IMAGE))
                    x_turn <- False
                    o_turn <- True
                    game_array[i][j] <- (x, y, 'x', False)
                ELSEIF o_turn:  # IF it's O's turn
                               ENDIF
                    images.append((x, y, O_IMAGE))
                    x_turn <- True
                    o_turn <- False
                    game_array[i][j] <- (x, y, 'o', False)
            ENDIF
                ENDIF
    ENDFOR
        ENDFOR
# checks to see IF someone won
                ENDIF
ENDFUNCTION

FUNCTION has_won(game_array):
    # checking rows for winning lines
                    ENDFOR
    for row in range(len(game_array)):
        IF (game_array[row][0][2] = game_array[row][1][2] = game_array[row][2][2]) AND game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + " has won!")
            RETURN True
        ENDIF
    # checking columns for winning lines
    ENDFOR
                       ENDFOR
    for col in range(len(game_array)):
        IF (game_array[0][col][2] = game_array[1][col][2] = game_array[2][col][2]) AND game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " has won!")
            RETURN True
        ENDIF
    # checking diagonals for winning lines
    ENDFOR
                         ENDFOR
    IF (game_array[0][0][2] = game_array[1][1][2] = game_array[2][2][2]) AND game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " has won!")
        RETURN True
    # checking reverse diagonals for winning lines
    ENDIF
                                 ENDFOR
    IF (game_array[0][2][2] = game_array[1][1][2] = game_array[2][0][2]) AND game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " has won!")
        RETURN True
    ENDIF
    RETURN False
# defines what happens when a draw is made
ENDFUNCTION

  ENDFUNCTION

FUNCTION has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            IF game_array[i][j][2] = "":
                RETURN False
            ENDIF
    ENDFOR
        ENDFOR
    display_message("It's a draw!")
    RETURN True
ENDFUNCTION

FUNCTION display_message(content):
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text <- END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)
ENDFUNCTION

FUNCTION render():
    win.fill(WHITE)
    draw_grid()
    # drawing X's AND O's
    for image in images:
        x, y, IMAGE <- image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    ENDFOR
    pygame.display.update()
# main loop
ENDFUNCTION

FUNCTION main():
    global x_turn, o_turn, images, draw
    images <- []
    draw <- False
    run <- True
    x_turn <- True
    o_turn <- False
    game_array <- initialize_grid()
    while run:
        for event in pygame.event.get():
            IF event.type = pygame.QUIT:
                pygame.quit()
            ENDIF
            IF event.type = pygame.MOUSEBUTTONDOWN:
                click(game_array)
            ENDIF
        ENDFOR
        render()
        IF has_won(game_array) OR has_drawn(game_array):
            run <- False
        ENDIF
ENDFUNCTION

    ENDWHILE
while True:
    IF __name__ = '__main__':
        main(
