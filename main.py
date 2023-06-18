import pygame
import random
pygame.init()

#initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 224)

# 2048 game color lib
colors = {
    0: (241, 220, 167),
    2: (217, 174, 148),
    4: (186, 165, 135),
    8: (155, 155, 122),
    16: (121, 125, 98),
    32: (255, 203, 105),
    64: (232, 172, 101),
    128: (208, 140, 96),
    256: (181, 132, 99),
    512: (153, 123, 102),
    1024: (107, 112, 92),
    2048: (191, 67, 66),
    'light-text' : (241, 246, 249),
    'dark-text' : (39, 55, 77),
    'other' : (0, 0, 0),
    'bg' : (187, 173, 160 )
    }

# game variables initialize
board_values = [[8 for _ in range(4)] for _ in range(4)]

# draw background for the board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], [5, 5, 390, 390], 0, 10)
    pass

# draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light-text']
            else:
                value_color = colors['dark-text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48-(5*value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center = (j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)
                
#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
