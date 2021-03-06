import pygame
from tetris.constants import WHITE, RED, BIG_FONT, SMALL_FONT, GIANT_FONT

quit = BIG_FONT.render('Quit', True, WHITE)
options = BIG_FONT.render('Options', True, WHITE)
play = BIG_FONT.render('Play', True, WHITE)
singleplayer = BIG_FONT.render('Single Player', True, WHITE)
pve = BIG_FONT.render('Player vs AI', True, WHITE)
pvp = BIG_FONT.render('Player vs Player', True, WHITE)
back = BIG_FONT.render('Back', True, WHITE)
game_over = GIANT_FONT.render('Game Over', True, RED)
replay = BIG_FONT.render('Replay', True, WHITE)