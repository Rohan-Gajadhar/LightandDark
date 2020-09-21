import pygame as pg

# defines colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Light&Dark"
BGCOLOR = DARKGREY

# tile settings
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 150
PLAYER_IMG = 'soldier1_stand.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
