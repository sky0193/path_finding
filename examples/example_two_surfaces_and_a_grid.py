import pygame
from pygame.locals import *
import sys

WIDTH = 600
HEIGHT = 600
WINDOWSIZE = WIDTH, HEIGHT

GRID_CELLS = 5

LENGTH_FIRST_SURFACE = 100
LENGTH_SECOND_SURFACE = (HEIGHT - LENGTH_FIRST_SURFACE) 


# This sets the margin between each cell
MARGIN = 5
MARGIN_WIDTH = MARGIN * GRID_CELLS + 2
MARGIN_LENGTH = MARGIN * GRID_CELLS + 2

WIDTH_CELL = (WIDTH - MARGIN_WIDTH)/ GRID_CELLS
HEIGHT_CELL = (LENGTH_SECOND_SURFACE - MARGIN_LENGTH) / GRID_CELLS

BLACK = (0, 0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
GREY = (160, 160, 160)





#---------------------------

grid = []
for row in range(GRID_CELLS):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_CELLS):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][2] = 1

#----------------------------




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




    for row in range(GRID_CELLS):
        for column in range(GRID_CELLS):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(mySurface2,
                             color,
                             [(MARGIN + WIDTH_CELL) * column + MARGIN,
                              (MARGIN + HEIGHT_CELL) * row + MARGIN,
                              WIDTH_CELL,
                              HEIGHT_CELL])
 
    pygame.display.update()