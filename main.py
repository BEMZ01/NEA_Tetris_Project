import tensorflow as tf, pygame, os, random
os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4/bin")
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
pygame.init()

from tetris.constants import WIDTH, HEIGHT, DARK_GREY, GREY, RED, ROWS, SQUARE_SIZE
from tetris.grid import Grid
from tetris.blocks import Block
from tetris.text import quit, options, play, singleplayer, pve, pvp, back

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NAE Tetris Project")

FPS = 60

block1 = random.randint(1, 7)
block2 = random.randint(1, 7)
block3 = random.randint(1, 7)
block4 = random.randint(1, 7)

def draw_window(main_menu):
    WIN.fill(DARK_GREY)
    grid = Grid()
    if main_menu == 1:
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,(HEIGHT/4)-35,500,70))
        WIN.blit(play,((WIDTH/2)-250,(HEIGHT/4)-25))
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,(HEIGHT/2)-35,500,70))
        WIN.blit(options,((WIDTH/2)-250,(HEIGHT/2)-25))
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,((HEIGHT/4)*3)-35,500,70))
        WIN.blit(quit,((WIDTH/2)-250,((HEIGHT/4)*3)-25))
    elif main_menu == 2:
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,(HEIGHT/4)-35,500,70))
        WIN.blit(singleplayer,((WIDTH/2)-250,(HEIGHT/4)-25))
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,(HEIGHT/2)-35,500,70))
        WIN.blit(pve,((WIDTH/2)-250,(HEIGHT/2)-25))
        pygame.draw.rect(WIN,GREY,((WIDTH/2)-250,((HEIGHT/4)*3)-35,500,70))
        WIN.blit(pvp,((WIDTH/2)-250,((HEIGHT/4)*3)-25))
        pygame.draw.rect(WIN,RED,(20,20,150,70))
        WIN.blit(back,(20,30))
    elif main_menu == 3:
        grid.draw_grid(WIN)
        grid.create_grid()
        if block1 == 1:
            grid.make_T_block1()
        elif block1 == 2:
            grid.make_line_block1()
        elif block1 == 3:
            grid.make_L_block1()
        elif block1 == 4:
            grid.make_reverse_L_block1()
        elif block1 == 5:
            grid.make_Z_block1()
        elif block1 == 6:
            grid.make_reverse_Z_block1()
        elif block1 == 7:
            grid.make_square_block1()
        pygame.draw.rect(WIN,DARK_GREY,(0,0,WIDTH,(HEIGHT/2)-(ROWS*SQUARE_SIZE)/2))
    elif main_menu == 4:
        grid.draw_double_grid(WIN)
        grid.create_double_grid()
        pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, (HEIGHT / 2) - (ROWS * SQUARE_SIZE) / 2))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    main_menu = 1
    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (WIDTH/2)-250 <= mouse[0] <= (WIDTH/2)+250 and ((HEIGHT/4)*3)-35 <= mouse[1] <= ((HEIGHT/4)*3)+35:
                    if main_menu == 1:
                        run = False
                    elif main_menu == 2:
                        main_menu = 4
                elif (WIDTH/2)-250 <= mouse[0] <= (WIDTH/2)+250 and (HEIGHT/4)-35 <= mouse[1] <= (HEIGHT/4)+35:
                    if main_menu == 1:
                        main_menu = 2
                    elif main_menu == 2:
                        main_menu = 3
                elif (WIDTH/2)-250 <= mouse[0] <= (WIDTH/2)+250 and (HEIGHT/2)-35 <= mouse[1] <= (HEIGHT/2)+35:
                    if main_menu == 1:
                        pass
                    elif main_menu == 2:
                        main_menu = 4
                elif 20 <= mouse[0] <= 170 and 20 <= mouse[1] <= 90:
                    if main_menu == 1:
                        pass
                    elif main_menu == 2:
                        main_menu = 1

        draw_window(main_menu)

    pygame.quit()

if __name__ == "__main__":
    main()