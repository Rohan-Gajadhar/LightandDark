import pygame as pg

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# Game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

# Tile Settings
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Wall Settings
WALL_IMG = 'tileGreen_39.png'

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'soldier1_stand.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# Gun settings
# BULLET_IMG = bullet.png

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)