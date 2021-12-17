import tensorflow as tf, pygame, os, random

try:
    os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4/bin")
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
except AttributeError:
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))
pygame.init()

from tetris.constants import WIDTH, HEIGHT, DARK_GREY, GREY, RED, ROWS, SQUARE_SIZE
from tetris.grid import Grid
from tetris.blocks import Block
from tetris.text import quit, options, play, singleplayer, pve, pvp, back

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


def draw_window(main_menu, grid_created, block_created):
    WIN.fill(DARK_GREY)
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
    elif main_menu == 4:
        grid.draw_double_grid(WIN)
        if not grid_created:
            grid.create_double_grid()
        pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, (HEIGHT / 2) - (ROWS * SQUARE_SIZE) / 2))
    pygame.display.update()


def main():
    global block1
    global block2
    global block3
    global block4
    counter1 = 5
    counter2 = 5
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
            pass
        else:
            if drop_counter1 >= drop_rate1:
                drop_counter1 = 0
                try:
                    piece = grid.get_square_position()
                    grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0]+1, piece[1]+1, piece[2]+1, piece[3]+1, piece[4], piece[5], piece[6], piece[7], main_menu)
                except:
                    block_created = False
                    blocks = grid.place_block(block1, block2, block3, block4)
                    block1, block2, block3, block4 = blocks[0], blocks[1], blocks[2], blocks[3]
            else:
                drop_counter1 = drop_counter1 + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (WIDTH / 2) - 250 <= mouse[0] <= (WIDTH / 2) + 250 and ((HEIGHT / 4) * 3) - 35 <= mouse[1] <= (
                        (HEIGHT / 4) * 3) + 35:
                    if main_menu == 1:
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
                elif 20 <= mouse[0] <= 170 and 20 <= mouse[1] <= 90:
                    if main_menu == 1:
                        pass
                    elif main_menu == 2:
                        main_menu = 1

            if event.type == pygame.KEYDOWN:
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
                            grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0], piece[1], piece[2], piece[3], piece[4]+1, piece[5]+1, piece[6]+1, piece[7]+1, main_menu)
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
                            grid.move1(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6], piece[7], piece[0], piece[1], piece[2], piece[3], piece[4]-1, piece[5]-1, piece[6]-1, piece[7]-1, main_menu)
                            counter1 = 0
                        except:
                            pass

        if counter1 < 5:
            counter1 = counter1 + 1

        draw_window(main_menu, grid_created, block_created)

    pygame.quit()


if __name__ == "__main__":
    main()
