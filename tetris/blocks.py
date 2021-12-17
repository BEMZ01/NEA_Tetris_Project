import pygame
from tetris.constants import ROWS, COLS, RED, GREEN, ORANGE, YELLOW, PURPLE, BLUE, LIGHT_BLUE, BLACK, SQUARE_SIZE, WIDTH, HEIGHT

class Block():
    def __init__(self, row1, row2, col1, col2, colour):
        self.row1 = row1
        self.row2 = row2
        self.col1 = col1
        self.col2 = col2
        self.colour = colour
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def calc_pos(self, main_menu):
        if main_menu == 3:
            self.x1 = ((WIDTH/8)*3)+(SQUARE_SIZE*self.col1)
            #self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1))
            self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1-4))
        elif main_menu == 4:
            self.x1 = (WIDTH/8)+(SQUARE_SIZE*self.col1)
            #self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1))
            self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1-4))
            self.x2 = ((WIDTH/8)*5)-(SQUARE_SIZE*5)+(SQUARE_SIZE*self.col1)
            #self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1))
            self.y1 = ((HEIGHT/2)-(SQUARE_SIZE*10))+(SQUARE_SIZE*(self.row1-4))

    def draw1(self, win):
        pygame.draw.rect(win, self.colour, (self.x1, self.y1, SQUARE_SIZE, SQUARE_SIZE))

    def draw2(self, win):
        pygame.draw.rect(win, self.colour, (self.x1, self.y1, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(win, self.colour, (self.x2, self.y2, SQUARE_SIZE, SQUARE_SIZE))

    def move1(self, row, col, main_menu):
        self.row = row
        self.col = col
        self.calc_pos(main_menu)