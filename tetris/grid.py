import pygame, random
from tetris.blocks import Block
from .constants import DARK_GREY, GREY, LIGHT_GREY, WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, RED, GREEN, ORANGE, YELLOW, PURPLE, BLUE, LIGHT_BLUE, BLACK
from pprint import pprint
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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
        for pos in range(len(self.grid1)):
            for col in range(COLS):
                self.grid1[pos].append(0)

    def create_double_grid(self):
        for row in range(ROWS+4):
            self.grid1.append([])
        for pos in range(len(self.grid1)):
            for col in range(COLS):
                self.grid1[pos].append(0)
        for row in range(ROWS+4):
            self.grid2.append([])
        for pos in range(len(self.grid2)):
            for col in range(COLS):
                self.grid2[pos].append(0)

    def move1(self, rowa, rowb, rowc, rowd, cola, colb, colc, cold, row1, row2, row3, row4, col1, col2, col3, col4, main_menu, block1):
        if col1 < 0 or col2 < 0 or col3 < 0 or col4 < 0:
            raise("")
        elif col1 > 9 or col2 > 9 or col3 > 9 or col4 > 9:
            raise("")
        if self.grid1[row1][col1] > 1 or self.grid1[row2][col2] > 1 or self.grid1[row3][col3] > 1 or self.grid1[row4][col4] > 1:
            raise("")
        if row1 == rowa + 1 and row2 == rowb + 1 and row3 == rowc + 1 and row4 == rowd + 1 or col1 == cola + 1 and col2 == colb + 1 and col3 == colc + 1 and col4 == cold + 1 or col1 == cola - 1 and col2 == colb - 1 and col3 == colc - 1 and col4 == cold - 1 or block1 != 5:
            if rowa + cola < row1 + col1 or rowb + colb < row2 + col2 or rowc + colc < row3 + col3 or rowd + cold < row4 + col4:
                self.grid1[rowd][cold], self.grid1[row4][col4] = self.grid1[row4][col4], self.grid1[rowd][cold]
                self.grid1[rowc][colc], self.grid1[row3][col3] = self.grid1[row3][col3], self.grid1[rowc][colc]
                self.grid1[rowb][colb], self.grid1[row2][col2] = self.grid1[row2][col2], self.grid1[rowb][colb]
                self.grid1[rowa][cola], self.grid1[row1][col1] = self.grid1[row1][col1], self.grid1[rowa][cola]
            else:
                self.grid1[rowa][cola], self.grid1[row1][col1] = self.grid1[row1][col1], self.grid1[rowa][cola]
                self.grid1[rowb][colb], self.grid1[row2][col2] = self.grid1[row2][col2], self.grid1[rowb][colb]
                self.grid1[rowc][colc], self.grid1[row3][col3] = self.grid1[row3][col3], self.grid1[rowc][colc]
                self.grid1[rowd][cold], self.grid1[row4][col4] = self.grid1[row4][col4], self.grid1[rowd][cold]
        else:
            self.grid1[rowa][cola], self.grid1[row1][col1] = self.grid1[row1][col1], self.grid1[rowa][cola]
            self.grid1[rowb][colb], self.grid1[row2][col2] = self.grid1[row2][col2], self.grid1[rowb][colb]
            self.grid1[rowc][colc], self.grid1[row3][col3] = self.grid1[row3][col3], self.grid1[rowc][colc]
            self.grid1[rowd][cold], self.grid1[row4][col4] = self.grid1[row4][col4], self.grid1[rowd][cold]
        block = Block(0, 0, 0, 0, 0)
        block.move1(row1, col1, main_menu)
        block.move1(row2, col2, main_menu)
        block.move1(row3, col3, main_menu)
        block.move1(row4, col4, main_menu)

    def get_square_position(self):
        squares_located = 0
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    if squares_located == 0:
                        row1 = row
                        col1 = col
                        squares_located = squares_located + 1
                    elif squares_located == 1:
                        row2 = row
                        col2 = col
                        squares_located = squares_located + 1
                    elif squares_located == 2:
                        row3 = row
                        col3 = col
                        squares_located = squares_located + 1
                    elif squares_located == 3:
                        row4 = row
                        col4 = col
                        squares_located = squares_located + 1
                if squares_located == 4:
                    rotation = [
                        {"right":
                            [
                                {"t_block":
                                    [
                                        {"north": [row1 + 2, row2 + 1, row3, row4, col1 + 1, col2, col3, col4]},
                                        {"east": [row1, row2+1, row3, row4, col1, col2+1, col3, col4]},
                                        {"south": [row1 + 1, row2, row3, row4, col1-1 , col2, col3, col4]},
                                        {"west": [row1, row2-1, row3, row4, col1, col2, col3-1, col4]}
                                    ]
                                },
                                {"line_block":
                                    [
                                        {"north": [row1 + 3, row2 + 2, row3 + 1, row4, col1 + 2, col2 + 1, col3 - 1, col4]},
                                        {"east": [row1 - 3, row2 , row3 - 2, row4-1, col1+1, col2, col3-1, col4-2]},
                                        {"south": [row1 + 3, row2 + 2, row3 + 1, row4, col1 + 2, col2 + 1, col3 - 1, col4]},
                                        {"west": [row1 - 3, row2 , row3 - 2, row4-1, col1+1, col2, col3-1, col4-2]}
                                    ]
                                },
                                {"l_block":
                                    [
                                        {"north": [row1 + 1, row2, row3, row4 - 1, col1 - 1, col2, col3 - 1, col4]},
                                        {"east": [row1 - 1, row2, row3 - 1, row4, col1, col2, col3 - 1, col4 + 1]},
                                        {"south": [row1 + 2, row2 + 2, row3, row4, col1, col2 + 1, col3 + 1, col4]},
                                        {"west": [row1, row2 - 2, row3, row4, col1 - 1, col2 + 1, col3, col4]}
                                    ]
                                },
                                {"reverse_l_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4 - 1, col1 + 1, col2 - 1, col3, col4]},
                                        {"east": [row1, row2 - 2, row3, row4 - 2, col1 + 1, col2 + 1, col3 , col4 ]},
                                        {"south": [row1 + 1, row2 + 1, row3, row4, col1 - 1, col2, col3 , col4 + 1]},
                                        {"west": [row1 + 1, row2, row3 - 1, row4, col1, col2, col3 - 1, col4 - 1]}
                                    ]
                                },
                                {"z_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4, col1 + 1, col2, col3, col4 + 1]},
                                        {"east": [row1, row2, row3, row4 - 2, col1 + 1, col2-1, col3-1, col4-1]},
                                        {"south": [row1 + 2, row2, row3, row4, col1 + 1, col2, col3, col4 + 1]},
                                        {"west": [row1, row2, row3, row4 - 2, col1 + 1, col2-1, col3-1, col4-1]}
                                    ]
                                },
                                {"reverse_z_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4, col1, col2 + 2, col3, col4]},
                                        {"east": [row1, row2, row3-2 , row4, col1, col2-2, col3, col4]},
                                        {"south": [row1 + 2, row2, row3, row4, col1, col2 + 2, col3, col4]},
                                        {"west": [row1, row2, row3-2 , row4, col1, col2-2, col3, col4]}
                                    ]
                                }
                            ]
                        },
                        {"left":
                            [
                                {"t_block":
                                    [
                                        {"north": [row1 + 1, row2, row3, row4, col1 + 1, col2, col3, col4]},
                                        {"east": [row1, row2 - 1, row3, row4 - 2, col1, col2, col3, col4 - 1]},
                                        {"south": [row1 + 2, row2, row3 + 1, row4, col1 - 1, col2, col3, col4]},
                                        {"west": [row1 - 1, row2, row3, row4, col1 + 1, col2, col3, col4]}
                                    ]
                                },
                                {"line_block":
                                    [
                                        {"north": [row1 + 3, row2 + 2, row3 + 1, row4, col1 - 2, col2 - 1, col3 + 1, col4]},
                                        {"east": [row1 - 3, row2 - 2, row3, row4 - 1, col1 + 2, col2 + 1, col3, col4 - 1]},
                                        {"south": [row1 + 3, row2 + 2, row3 + 1, row4, col1 - 2, col2 - 1, col3 + 1, col4]},
                                        {"west": [row1 - 3, row2 - 2, row3, row4 - 1, col1 + 2, col2 + 1, col3, col4 - 1]}
                                    ]
                                },
                                {"l_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4, col1 - 1, col2 + 1, col3, col4]},
                                        {"east": [row1 - 1, row2, row3+1, row4, col1 + 1, col2, col3, col4 + 1]},
                                        {"south": [row1 + 1, row2 + 1, row3, row4, col1, col2 + 1, col3, col4 - 1]},
                                        {"west": [row1 , row2-2, row3, row4-2, col1 - 1, col2, col3, col4 - 1]}
                                    ]
                                },
                                {"reverse_l_block":
                                    [
                                        {"north": [row1 + 1, row2, row3 - 1, row4, col1 + 1, col2, col3, col4 + 1]},
                                        {"east": [row1, row2, row3, row4 - 2, col1 + 1, col2, col3, col4 - 1]},
                                        {"south": [row1 +2, row2 + 2, row3, row4, col1 - 1, col2, col3 - 1, col4]},
                                        {"west": [row1 - 1, row2, row3 - 1, row4, col1 + 1, col2, col3, col4 - 1]}
                                    ]
                                },
                                {"z_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4, col1, col2, col3-2, col4]},
                                        {"east": [row1, row2, row3, row4-2, col1+2, col2, col3, col4]},
                                        {"south": [row1 + 2, row2, row3, row4, col1, col2, col3-2, col4]},
                                        {"west": [row1, row2, row3, row4-2, col1+2, col2, col3, col4]}
                                    ]
                                },
                                {"reverse_z_block":
                                    [
                                        {"north": [row1 + 2, row2, row3, row4, col1, col2, col3, col4 - 2]},
                                        {"east": [row1, row2, row3 - 2, row4, col1+1, col2 -1, col3+1, col4+1]},
                                        {"south": [row1 + 2, row2, row3, row4, col1, col2, col3, col4 - 2]},
                                        {"west": [row1, row2, row3 - 2, row4, col1+1, col2 - 1, col3+1, col4+1]},
                                    ]
                                }
                            ]
                        }
                    ]
                    return row1, row2, row3, row4, col1, col2, col3, col4, rotation


    def make_T_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[1][5] = 1
            self.grid1[2][5] = 1
            self.grid1[2][4] = 1
            self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, PURPLE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_line_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[0][5] = 1
            self.grid1[1][5] = 1
            self.grid1[2][5] = 1
            self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, LIGHT_BLUE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_L_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[1][4] = 1
            self.grid1[2][4] = 1
            self.grid1[3][4] = 1
            self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, ORANGE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_reverse_L_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[1][5] = 1
            self.grid1[2][5] = 1
            self.grid1[3][5] = 1
            self.grid1[3][4] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, BLUE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_Z_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[1][5] = 1
            self.grid1[2][5] = 1
            self.grid1[2][4] = 1
            self.grid1[3][4] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, RED)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_reverse_Z_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[1][4] = 1
            self.grid1[2][4] = 1
            self.grid1[2][5] = 1
            self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, GREEN)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def make_square_block1(self, block_created, main_menu):
        if not block_created:
            self.grid1[2][4] = 1
            self.grid1[2][5] = 1
            self.grid1[3][4] = 1
            self.grid1[3][5] = 1
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    block = Block(row, 0, col, 0, YELLOW)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def place_block(self, block1, block2, block3, block4):
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    if block1 == 1:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 2:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 3:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 4:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 5:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 6:
                        self.grid1[row][col] = block1 + 1
                    elif block1 == 7:
                        self.grid1[row][col] = block1 + 1
        block1 = block2
        block2 = block3
        block3 = block4
        block4 = random.randint(1, 7)
        return block1, block2, block3, block4

    def erase_block(self, block1, block2, block3, block4):
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 1:
                    self.grid1[row][col] = 0
        if block1 == 0:
            block1 = block2
            block2 = block3
            block3 = block4
            block4 = random.randint(1, 7)
        return block1, block2, block3, block4

    def draw_blocks(self, main_menu):
        for row in range (ROWS+4):
            for col in range (COLS):
                if self.grid1[row][col] == 2:
                    block = Block(row, 0, col, 0, PURPLE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 3:
                    block = Block(row, 0, col, 0, LIGHT_BLUE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 4:
                    block = Block(row, 0, col, 0, ORANGE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 5:
                    block = Block(row, 0, col, 0, BLUE)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 6:
                    block = Block(row, 0, col, 0, RED)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 7:
                    block = Block(row, 0, col, 0, GREEN)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)
                elif self.grid1[row][col] == 8:
                    block = Block(row, 0, col, 0, YELLOW)
                    block.calc_pos(main_menu)
                    block.draw1(WIN)

    def check_grid(self):
        lines_cleared = 0
        for row in range (ROWS+4):
            counter = 0
            for col in range (COLS):
                if self.grid1[row][col] != 0:
                    if row < 4:
                        self.grid1 = []
                        return -1
                    counter = counter + 1
                else:
                    pass
            if counter == 10:
                self.grid1.pop(row)
                self.grid1.insert(0, [0,0,0,0,0,0,0,0,0,0])
                lines_cleared += 1
        return lines_cleared
