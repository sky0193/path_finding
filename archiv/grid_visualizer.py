import sys
import pygame
from pygame.locals import KEYDOWN, K_q

import constants
import archiv.grid as grid


import path_search_algorithms

# CONSTANTS:
WINDOWSIZE = WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
GREY = (160, 160, 160)

GRID_WIDTH_HEIGHT = 600

# VARS:
_VARS = {'surf': False}


#    |   1   2  3 . . .                     m
# ---------------------------------------------> x
#  1 |
#  2 |
#  . |
#  . |
#  . |
#    |
#    |
#    |
#    |
#  n |
#   y



def main():
    area, openSet, closedSet, endNode = path_search_algorithms.setup(constants.GRID_CELLS, constants.GRID_CELLS)
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(WINDOWSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawGrid(constants.GRID_CELLS)

        #for i in range(0, constants.GRID_CELLS):
        #  for j in range(0, constants.GRID_CELLS):
        #    if area_as_grid.grid[i][j] == 1:
        #        drawRect(i,j)
        open_set, closedSet, path = path_search_algorithms.A_star(openSet, closedSet, endNode)
        if(path is None):
          for cell in open_set:
            drawRect(cell.i,cell.j, GREEN)
          for cell in closedSet:
            drawRect(cell.i,cell.j, RED)
        else:
          for cell in path:
            drawRect(cell.i,cell.j, BLUE)
        for i in range(0, constants.GRID_CELLS):
          for j in range(0, constants.GRID_CELLS):
              if(area.cell_grid[i][j].obstacle):
                drawRect(i, j, BLACK)

        pygame.display.update()



def drawRect(i,j, color):

    width = GRID_WIDTH_HEIGHT / constants.GRID_CELLS
    height = GRID_WIDTH_HEIGHT / constants.GRID_CELLS


    #    | 0   1   2  3 . . .   5                  m
    # ---------------------------------------------> x
    #  0 |                   i=0 j=5
    #  1 |
    #  2 |                   i=2 j=5
    #    |            
    #  . |
    #  . |
    #  . |
    #  5 |                    
    #    |
    #    |
    #    |
    #  n |
    #   y

    pos_x = j * width
    pos_y = i * height

    pygame.draw.rect(
     _VARS['surf'], color,
     (pos_x, pos_y, width, height)
    )


def drawGrid(divisions):

    cont_x, cont_y = 0, 0  # Offset TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (GRID_WIDTH_HEIGHT + cont_x, cont_y), 2)

    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, GRID_WIDTH_HEIGHT + cont_y),
      (GRID_WIDTH_HEIGHT + cont_x, GRID_WIDTH_HEIGHT + cont_y), 2)

    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + GRID_WIDTH_HEIGHT), 2)

    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (GRID_WIDTH_HEIGHT + cont_x, cont_y),
      (GRID_WIDTH_HEIGHT + cont_x, GRID_WIDTH_HEIGHT + cont_y), 2)

    # Get cell size, just one since its a square grid.
    cellSize = GRID_WIDTH_HEIGHT/divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
           _VARS['surf'], BLACK,
           (cont_x + (cellSize * x), cont_y),
           (cont_x + (cellSize * x), GRID_WIDTH_HEIGHT + cont_y), 2)

    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
          _VARS['surf'], BLACK,
          (cont_x, cont_y + (cellSize*x)),
          (cont_x + GRID_WIDTH_HEIGHT, cont_y + (cellSize*x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()