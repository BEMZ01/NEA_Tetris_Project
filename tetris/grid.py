import pygame, random
from tetris.blocks import Block
from .constants import DARK_GREY, GREY, LIGHT_GREY, WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, RED, GREEN, ORANGE, YELLOW, PURPLE, BLUE, LIGHT_BLUE, BLACK
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

block1 = random.randint(1,6)
block2 = random.randint(1,6)
block3 = random.randint(1,6)
block4 = random.randint(1,6)

class Grid:
    def __init__(self):
        self.grid1 = []
        self.grid2 = []

    def draw_grid(self, win):
        win.fill(DARK_GREY)
        for col in range(COLS):
            for row in range(col % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (((WIDTH/8)*3)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
        for col in range(COLS):
            for row in range((col+1) % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT_GREY, (((WIDTH/8)*3)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))

    def draw_double_grid(self, win):
        win.fill(DARK_GREY)
        for col in range(COLS):
            for row in range(col % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, ((WIDTH/8)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
        for col in range(COLS):
            for row in range((col+1) % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT_GREY, ((WIDTH/8)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
        for col in range(COLS):
            for row in range(col % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (((WIDTH/8)*5)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
        for col in range(COLS):
            for row in range((col+1) % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT_GREY, (((WIDTH/8)*5)+(col*SQUARE_SIZE), ((HEIGHT/2)-(ROWS*SQUARE_SIZE)/2)+(row*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))

    def create_grid(self):
        for row in range(ROWS+4):
            self.grid1.append([])
            for col in range(COLS):
                self.grid1[row].append(0)

    def create_double_grid(self):
        for row in range(ROWS+4):
            self.grid1.append([])
            for col in range(COLS):
                self.grid1[row].append(0)
        for row in range(ROWS+4):
            self.grid2.append([])
            for col in range(COLS):
                self.grid2[row].append(0)

    def make_T_block1(self):

        self.grid1[1][5] = 1
        self.grid1[2][5] = 1
        self.grid1[2][4] = 1
        self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, PURPLE)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_line_block1(self):

        self.grid1[0][5] = 1
        self.grid1[1][5] = 1
        self.grid1[2][5] = 1
        self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, LIGHT_BLUE)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_L_block1(self):

        self.grid1[1][4] = 1
        self.grid1[2][4] = 1
        self.grid1[3][4] = 1
        self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, ORANGE)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_reverse_L_block1(self):

        self.grid1[1][5] = 1
        self.grid1[2][5] = 1
        self.grid1[3][5] = 1
        self.grid1[3][4] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, BLUE)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_Z_block1(self):

        self.grid1[1][5] = 1
        self.grid1[2][5] = 1
        self.grid1[2][4] = 1
        self.grid1[3][4] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, RED)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_reverse_Z_block1(self):

        self.grid1[1][4] = 1
        self.grid1[2][4] = 1
        self.grid1[2][5] = 1
        self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, GREEN)
                    block.calc_pos(3)
                    block.draw1(WIN)

    def make_square_block1(self):

        self.grid1[2][4] = 1
        self.grid1[2][5] = 1
        self.grid1[3][4] = 1
        self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, YELLOW)
                    block.calc_pos(3)
                    block.draw1(WIN)