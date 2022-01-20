import tensorflow as tf, pygame, os, random

try:
    os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4/bin")
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
except AttributeError:
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))
pygame.init()

from tetris.constants import WIDTH, HEIGHT, DARK_GREY, GREY, RED, GREEN, PURPLE, LIGHT_BLUE, BLUE, ORANGE, YELLOW, WHITE, BLACK, ROWS, SQUARE_SIZE, SMALL_FONT, BIG_FONT
from tetris.grid import Grid
from tetris.blocks import Block
from tetris.text import quit, options, play, singleplayer, pve, pvp, back, game_over, replay

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NAE Tetris Project")


grid = Grid()

grid_created = False
FPS = 60

global block1
global block2
global block3
global block4
block1 = random.randint(1, 7)
block2 = random.randint(1, 7)
block3 = random.randint(1, 7)
block4 = random.randint(1, 7)


def draw_window(main_menu, grid_created, block_created, level1, score1, lines_cleared1, hold1, holda):
    WIN.fill(DARK_GREY)
    current_level1 = BIG_FONT.render('Level ' + str(level1), True, WHITE)
    current_score1 = BIG_FONT.render('Score ' + str(score1), True, WHITE)
    current_lines1 = BIG_FONT.render('Lines Cleared ' + str(lines_cleared1), True, WHITE)
    if main_menu == 1:
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, (HEIGHT / 4) - 35, 500, 70))
        WIN.blit(play, ((WIDTH / 2) - 250, (HEIGHT / 4) - 25))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, (HEIGHT / 2) - 35, 500, 70))
        WIN.blit(options, ((WIDTH / 2) - 250, (HEIGHT / 2) - 25))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 35, 500, 70))
        WIN.blit(quit, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 25))
    elif main_menu == 2:
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, (HEIGHT / 4) - 35, 500, 70))
        WIN.blit(singleplayer, ((WIDTH / 2) - 250, (HEIGHT / 4) - 25))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, (HEIGHT / 2) - 35, 500, 70))
        WIN.blit(pve, ((WIDTH / 2) - 250, (HEIGHT / 2) - 25))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 35, 500, 70))
        WIN.blit(pvp, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 25))
        pygame.draw.rect(WIN, RED, (20, 20, 150, 70))
        WIN.blit(back, (20, 30))
    elif main_menu == 3:
        grid.draw_grid(WIN)
        if not grid_created:
            grid.create_grid()
        if block1 == 1:
            grid.make_T_block1(block_created, main_menu)
        elif block1 == 2:
            grid.make_line_block1(block_created, main_menu)
        elif block1 == 3:
            grid.make_L_block1(block_created, main_menu)
        elif block1 == 4:
            grid.make_reverse_L_block1(block_created, main_menu)
        elif block1 == 5:
            grid.make_Z_block1(block_created, main_menu)
        elif block1 == 6:
            grid.make_reverse_Z_block1(block_created, main_menu)
        elif block1 == 7:
            grid.make_square_block1(block_created, main_menu)
        grid.draw_blocks(main_menu)
        pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, (HEIGHT / 2) - (ROWS * SQUARE_SIZE) / 2))
        if holda == False:
            pygame.draw.rect(WIN, GREY, (WIDTH / 2 - SQUARE_SIZE * 8, HEIGHT / 4 - SQUARE_SIZE * 5 + 30, SQUARE_SIZE * 2 + 30, SQUARE_SIZE * 2 + 30))
        else:
            pygame.draw.rect(WIN, BLACK, (WIDTH / 2 - SQUARE_SIZE * 8, HEIGHT / 4 - SQUARE_SIZE * 5 + 30, SQUARE_SIZE * 2 + 30, SQUARE_SIZE * 2 + 30))
        pygame.draw.rect(WIN, GREY, (WIDTH / 2 + SQUARE_SIZE * 6 - 30, HEIGHT / 4 - SQUARE_SIZE * 5 + 30, SQUARE_SIZE * 2 + 30, SQUARE_SIZE * 6 + 90))
        if hold1 == 1:
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 - SQUARE_SIZE * 7 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif hold1 == 2:
            pygame.draw.rect(WIN, LIGHT_BLUE, (WIDTH / 2 - SQUARE_SIZE * 7.25 + 15, HEIGHT / 2 - SQUARE_SIZE * 10 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 2))
        elif hold1 == 3:
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 - SQUARE_SIZE * 7 + 15, HEIGHT / 2 - SQUARE_SIZE * 8.75 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif hold1 == 4:
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 - SQUARE_SIZE * 7 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 8.75 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif hold1 == 5:
            pygame.draw.rect(WIN, RED, (WIDTH / 2 - SQUARE_SIZE * 7 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, RED, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif hold1 == 6:
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 - SQUARE_SIZE * 7 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif hold1 == 7:
            pygame.draw.rect(WIN, YELLOW, (WIDTH / 2 - SQUARE_SIZE * 7.5 + 15, HEIGHT / 2 - SQUARE_SIZE * 9.5 +15, SQUARE_SIZE, SQUARE_SIZE))
        if block2 == 1:
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block2 == 2:
            pygame.draw.rect(WIN, LIGHT_BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.75 - 15, HEIGHT / 2 - SQUARE_SIZE * 10 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 2))
        elif block2 == 3:
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 8.75 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block2 == 4:
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 8.75 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block2 == 5:
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block2 == 6:
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.75 +15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.25 + 15, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block2 == 7:
            pygame.draw.rect(WIN, YELLOW, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 9.5 +15, SQUARE_SIZE, SQUARE_SIZE))
        if block3 == 1:
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.25 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block3 == 2:
            pygame.draw.rect(WIN, LIGHT_BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.75 - 15, HEIGHT / 2 - SQUARE_SIZE * 8 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 2))
        elif block3 == 3:
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 6.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block3 == 4:
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 6.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block3 == 5:
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.25 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block3 == 6:
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.75 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.25 + 45, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block3 == 7:
            pygame.draw.rect(WIN, YELLOW, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 7.5 + 45, SQUARE_SIZE, SQUARE_SIZE))
        if block4 == 1:
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, PURPLE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.25 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block4 == 2:
            pygame.draw.rect(WIN, LIGHT_BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.75 - 15, HEIGHT / 2 - SQUARE_SIZE * 6 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 2))
        elif block4 == 3:
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, ORANGE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 4.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block4 == 4:
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1.5))
            pygame.draw.rect(WIN, BLUE, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 4.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        elif block4 == 5:
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, RED, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.25 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block4 == 6:
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.75 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
            pygame.draw.rect(WIN, GREEN, (WIDTH / 2 + SQUARE_SIZE * 7 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.25 + 75, SQUARE_SIZE * 0.5, SQUARE_SIZE * 1))
        elif block4 == 7:
            pygame.draw.rect(WIN, YELLOW, (WIDTH / 2 + SQUARE_SIZE * 6.5 - 15, HEIGHT / 2 - SQUARE_SIZE * 5.5 + 75, SQUARE_SIZE, SQUARE_SIZE))
        WIN.blit(current_level1, (0, 0))
        WIN.blit(current_score1, (0, 50))
        WIN.blit(current_lines1, (0, 100))
    elif main_menu == 4:
        grid.draw_double_grid(WIN)
        if not grid_created:
            grid.create_double_grid()
        pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, (HEIGHT / 2) - (ROWS * SQUARE_SIZE) / 2))
    elif main_menu == 5:
        WIN.blit(game_over, ((WIDTH / 2) - 450, ((HEIGHT / 4) - 100)))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, (HEIGHT / 2) - 35, 500, 70))
        WIN.blit(replay, ((WIDTH / 2) - 250, (HEIGHT / 2) - 25))
        pygame.draw.rect(WIN, GREY, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 35, 500, 70))
        WIN.blit(quit, ((WIDTH / 2) - 250, ((HEIGHT / 4) * 3) - 25))
    pygame.display.update()


def main():
    global block1
    global block2
    global block3
    global block4
    level1 = 0
    score1 = 0
    rotated = False
    direction = ""
    block_type = ""
    orientation1 = 1
    orientation2 = 1
    hold1 = 0
    hold2 = 0
    holda = False
    holdb = False
    counter1 = 5
    counter2 = 5
    total_lines_cleared = 0
    drop_rate1 = 48
    drop_ratea = 48
    drop_counter1 = 0
    grid_created = False
    block_created = False
    key_down = False
    d_down = False
    a_down = False
    clock = pygame.time.Clock()
    run = True
    main_menu = 1
    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if main_menu == 3 or main_menu == 4:
            grid_created = True
            block_created = True
        if main_menu == 1 or main_menu == 2:
            score1 = 0
            total_lines_cleared = 0
            level1 = 0
            hold1 = 0
        elif main_menu == 5:
            pass
        else:
            if drop_counter1 >= drop_rate1:
                drop_counter1 = 0
                if drop_rate1 == 0:
                    score1 += 1
                try:
                    piece = grid.get_square_position()
                    grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0]+1, piece[1]+1, piece[2]+1, piece[3]+1, piece[4], piece[5], piece[6], piece[7], main_menu, block1)
                except:
                    block_created = False
                    blocks = grid.place_block(block1, block2, block3, block4)
                    block1, block2, block3, block4 = blocks[0], blocks[1], blocks[2], blocks[3]
                    lines_cleared = grid.check_grid()
                    orientation1 = 1
                    holda = False
                    if lines_cleared == -1:
                        main_menu = 5
                        grid_created = False
                    else:
                        total_lines_cleared += lines_cleared
                        level1 = total_lines_cleared // 10
                    if lines_cleared == 1:
                        score1 = score1 + 40 * (level1 + 1)
                    elif lines_cleared == 2:
                        score1 = score1 + 100 * (level1 + 1)
                    elif lines_cleared == 3:
                        score1 = score1 + 300 * (level1 + 1)
                    elif lines_cleared == 4:
                        score1 = score1 + 1200 * (level1 + 1)
                    if lines_cleared > 0:
                        if level1 == 0:
                            drop_rate1 = 48
                            drop_ratea = 48
                        elif level1 == 1:
                            drop_rate1 = 43
                            drop_ratea = 43
                        elif level1 == 2:
                            drop_rate1 = 38
                            drop_ratea = 38
                        elif level1 == 3:
                            drop_rate1 = 33
                            drop_ratea = 33
                        elif level1 == 4:
                            drop_rate1 = 28
                            drop_ratea = 28
                        elif level1 == 5:
                            drop_rate1 = 23
                            drop_ratea = 23
                        elif level1 == 6:
                            drop_rate1 = 18
                            drop_ratea = 18
                        elif level1 == 7:
                            drop_rate1 = 13
                            drop_ratea = 13
                        elif level1 == 8:
                            drop_rate1 = 8
                            drop_ratea = 8
                        elif level1 == 9:
                            drop_rate1 = 6
                            drop_ratea = 6
                        elif 10 <= level1 <= 12:
                            drop_rate1 = 5
                            drop_ratea = 5
                        elif 13 <= level1 <= 15:
                            drop_rate1 = 4
                            drop_ratea = 4
                        elif 13 <= level1 <= 15:
                            drop_rate1 = 4
                            drop_ratea = 4
                        elif 16 <= level1 <= 18:
                            drop_rate1 = 3
                            drop_ratea = 3
                        elif 19 <= level1 <= 28:
                            drop_rate1 = 2
                            drop_ratea = 2
                        else:
                            drop_rate1 = 1
                            drop_ratea = 1
            else:
                drop_counter1 = drop_counter1 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (WIDTH / 2) - 250 <= mouse[0] <= (WIDTH / 2) + 250 and ((HEIGHT / 4) * 3) - 35 <= mouse[1] <= (
                        (HEIGHT / 4) * 3) + 35:
                    if main_menu == 1 or main_menu == 5:
                        run = False
                    elif main_menu == 2:
                        main_menu = 4
                elif (WIDTH / 2) - 250 <= mouse[0] <= (WIDTH / 2) + 250 and (HEIGHT / 4) - 35 <= mouse[1] <= (
                        HEIGHT / 4) + 35:
                    if main_menu == 1:
                        main_menu = 2
                    elif main_menu == 2:
                        main_menu = 3
                elif (WIDTH / 2) - 250 <= mouse[0] <= (WIDTH / 2) + 250 and (HEIGHT / 2) - 35 <= mouse[1] <= (
                        HEIGHT / 2) + 35:
                    if main_menu == 1:
                        pass
                    elif main_menu == 2:
                        main_menu = 4
                    elif main_menu == 5:
                        main_menu = 1
                elif 20 <= mouse[0] <= 170 and 20 <= mouse[1] <= 90:
                    if main_menu == 1:
                        pass
                    elif main_menu == 2:
                        main_menu = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if main_menu == 1 or main_menu == 2 or main_menu == 5:
                        pass
                    elif holda == False:
                        hold1, block1 = block1, hold1
                        blocks = grid.erase_block(block1, block2, block3, block4)
                        block1, block2, block3, block4 = blocks[0], blocks[1], blocks[2], blocks[3]
                        block_created = False
                        holda = True
                if event.key == pygame.K_d:
                    if key_down == False:
                        d_down = True
                    else:
                        pass
                if event.key == pygame.K_a:
                    if key_down == False:
                        a_down = True
                    else:
                        pass
                if event.key == pygame.K_s:
                    drop_rate1 = 0
                if event.key == pygame.K_e:
                    if main_menu == 1 or main_menu == 2 or block1 == 7:
                        pass
                    else:
                        if orientation1 == 1:
                            direction = "north"
                        elif orientation1 == 2:
                            direction = "east"
                        elif orientation1 == 3:
                            direction = "south"
                        elif orientation1 == 4:
                            direction = "west"
                        if block1 == 1:
                            block_type = "t_block"
                        if block1 == 2:
                            block_type = "line_block"
                        if block1 == 3:
                            block_type = "l_block"
                        if block1 == 4:
                            block_type = "reverse_l_block"
                        if block1 == 5:
                            block_type = "z_block"
                        if block1 == 6:
                            block_type = "reverse_z_block"
                        x = 0
                        y = 0
                        rotation_attempts = 0
                        while rotated == False:
                            try:
                                piece = grid.get_square_position()
                                grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6],
                                           piece[7],
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][0]+x,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][1]+x,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][2]+x,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][3]+x,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][4]+y,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][5]+y,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][6]+y,
                                           piece[8][0]["right"][block1-1][block_type][orientation1-1][direction][7]+y,
                                           main_menu,
                                           block1)
                                orientation1 += 1
                                if orientation1 > 4:
                                    orientation1 = 1
                                rotated = True
                            except:
                                if rotation_attempts == 0:
                                    y = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 1:
                                    y = -1
                                    rotation_attempts += 1
                                elif rotation_attempts == 2:
                                    y = 2
                                    rotation_attempts += 1
                                elif rotation_attempts == 3:
                                    y = -2
                                    rotation_attempts += 1
                                elif rotation_attempts == 4:
                                    y = 0
                                    x = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 5:
                                    y = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 6:
                                    y = -1
                                    rotation_attempts += 1
                                else:
                                    x = 0
                                    y = 0
                                    rotation_attempts = 0
                                    rotated = True
                        rotated = False
                if event.key == pygame.K_q:
                    if main_menu == 1 or main_menu == 2 or block1 == 7:
                        pass
                    else:
                        if orientation1 == 1:
                            direction = "north"
                        elif orientation1 == 2:
                            direction = "east"
                        elif orientation1 == 3:
                            direction = "south"
                        elif orientation1 == 4:
                            direction = "west"
                        if block1 == 1:
                            block_type = "t_block"
                        if block1 == 2:
                            block_type = "line_block"
                        if block1 == 3:
                            block_type = "l_block"
                        if block1 == 4:
                            block_type = "reverse_l_block"
                        if block1 == 5:
                            block_type = "z_block"
                        if block1 == 6:
                            block_type = "reverse_z_block"
                        x = 0
                        y = 0
                        rotation_attempts = 0
                        while rotated == False:
                            try:
                                piece = grid.get_square_position()
                                grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6],
                                           piece[7],
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][0]+x,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][1]+x,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][2]+x,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][3]+x,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][4]+y,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][5]+y,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][6]+y,
                                           piece[8][1]["left"][block1-1][block_type][orientation1-1][direction][7]+y,
                                           main_menu,
                                           block1)
                                orientation1 -= 1
                                if orientation1 < 1:
                                    orientation1 = 4
                                rotated = True
                            except:
                                if rotation_attempts == 0:
                                    y = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 1:
                                    y = -1
                                    rotation_attempts += 1
                                elif rotation_attempts == 2:
                                    y = 0
                                    x = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 3:
                                    y = 1
                                    rotation_attempts += 1
                                elif rotation_attempts == 4:
                                    y = -1
                                    rotation_attempts += 1
                                elif rotation_attempts == 5:
                                    x = 0
                                    y = 2
                                    rotation_attempts += 1
                                elif rotation_attempts == 6:
                                    y = -2
                                    rotation_attempts += 1
                                else:
                                    x = 0
                                    y = 0
                                    rotation_attempts = 0
                                    rotated = True
                        rotated = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    d_down = False
                    key_down = False
                if event.key == pygame.K_a:
                    a_down = False
                    key_down = False
                if event.key == pygame.K_s:
                    drop_rate1 = drop_ratea

            if d_down == True:
                if counter1 < 5:
                    pass
                else:
                    if main_menu == 1 or main_menu == 2:
                        pass
                    else:
                        try:
                            piece = grid.get_square_position()
                            grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0], piece[1], piece[2], piece[3], piece[4]+1, piece[5]+1, piece[6]+1, piece[7]+1, main_menu, block1)
                            counter1 = 0
                        except:
                            pass

            if a_down == True:
                if counter1 < 5:
                    pass
                else:
                    if main_menu == 1 or main_menu == 2:
                        pass
                    else:
                        try:
                            piece = grid.get_square_position()
                            grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0], piece[1], piece[2], piece[3], piece[4]-1, piece[5]-1, piece[6]-1, piece[7]-1, main_menu, block1)
                            counter1 = 0
                        except:
                            pass

        if counter1 < 5:
            counter1 = counter1 + 1

        draw_window(main_menu, grid_created, block_created, level1, score1, total_lines_cleared, hold1, holda)

    pygame.quit()


if __name__ == "__main__":
    main()
