import pygame as pg

# defines colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Light&Dark"
BGCOLOR = BROWN

# tile settings
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_358.png'

# player settings
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'soldier1_stand.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# Mob settings
MOB_IMG = 'zombie1_machine.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)