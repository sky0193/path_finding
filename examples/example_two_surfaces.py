import pygame
from pygame.locals import *
import sys

WIDTH = 600
HEIGHT = 600
WINDOWSIZE = WIDTH, HEIGHT

GRID_CELLS = 5

LENGTH_FIRST_SURFACE = 100
LENGTH_SECOND_SURFACE = (HEIGHT - LENGTH_FIRST_SURFACE) 

BLACK = (0, 0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
GREY = (160, 160, 160)


pygame.init()
 
displaysurface = pygame.display.set_mode(WINDOWSIZE)
 

mySurface_width = WIDTH
mySurface_length = LENGTH_FIRST_SURFACE
mySurface = pygame.Surface((mySurface_width, mySurface_length))
mySurface.fill(BLUE)
 
mySurface2_width = WIDTH
mySurface2_length = HEIGHT - mySurface_length
mySurface2 = pygame.Surface((mySurface2_width, mySurface2_length))
mySurface2.fill(GREEN)
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mySurface_start_x=0
    mySurface_start_y=0
    displaysurface.blit(mySurface, (mySurface_start_x, mySurface_start_y))
    displaysurface.blit(mySurface2, (mySurface_start_x, mySurface_length))

 
    pygame.display.update()