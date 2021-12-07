import pygame
pygame.init()

WIDTH, HEIGHT = 1920, 1080
ROWS, COLS = 20, 10
SQUARE_SIZE = (WIDTH//4)//COLS

DARK_GREY = (100, 100, 100)
GREY = (150, 150, 150)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 0)
PURPLE = (200, 0, 255)
LIGHT_BLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BIG_FONT = pygame.font.SysFont('Corbel', 50)
SMALL_FONT = pygame.font.SysFont('Corbel', 25)