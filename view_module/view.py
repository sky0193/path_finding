import pygame
import view_helper.colors
from view_module.button import Button
from typing import List
from view_module.rectangle import Rectangle

from constants import GRID_CELLS
from view_helper.view_constants import WIDTH, HEIGHT, WINDOWSIZE, MARGIN, LENGTH_FIRST_SURFACE, LENGTH_SECOND_SURFACE


def set_up_start_button(mySurface) -> Button:
    button_start_pos_x: int = 10
    button_start_pos_y: int = int(LENGTH_FIRST_SURFACE / 2)
    button_start_pos_width: int = 60
    button_start_pos_heigth = 30
    button_start_elevation = 10
    button_start: Button = Button(text='Start',
                                  pos_x=button_start_pos_x,
                                  pos_y=button_start_pos_y,
                                  width=button_start_pos_width,
                                  height=button_start_pos_heigth,
                                  elevation=button_start_elevation,
                                  mySurface=mySurface)
    return button_start


def set_up_reset_button(mySurface) -> Button:
    button_reset_pos_x = int(WIDTH / 3)
    button_reset_pos_y = int(LENGTH_FIRST_SURFACE / 2)
    button_reset_pos_width = 60
    button_reset_pos_heigth = 30
    button_reset_elevation = 10
    button_reset: Button = Button('Reset',
                                  pos_x=button_reset_pos_x,
                                  pos_y=button_reset_pos_y,
                                  width=button_reset_pos_width,
                                  height=button_reset_pos_heigth,
                                  elevation=button_reset_elevation,
                                  mySurface=mySurface)
    return button_reset


class View:
    def __init__(self):
        self.displaysurface = pygame.display.set_mode(WINDOWSIZE)

        self.margin_width = MARGIN * GRID_CELLS + 2
        self.margin_length = MARGIN * GRID_CELLS + 2

        self.width_cell = (WIDTH - self.margin_width) / GRID_CELLS
        self.height_cell = (LENGTH_SECOND_SURFACE - self.margin_length) / GRID_CELLS

        self.mySurface_width = WIDTH
        self.mySurface_length = LENGTH_FIRST_SURFACE
        self.mySurface = pygame.Surface((self.mySurface_width, self.mySurface_length))
        self.mySurface.fill(view_helper.colors.GREY_LIGHT)

        self.mySurface2_width = WIDTH
        self.mySurface2_length = HEIGHT - self.mySurface_length
        self.mySurface2 = pygame.Surface((self.mySurface2_width, self.mySurface2_length))

        self.button_start = set_up_start_button(self.mySurface)
        self.button_reset = set_up_reset_button(self.mySurface)

        self.rectangles = []

    def update_surface(self):
        mySurface_start_x = 0
        mySurface_start_y = 0
        self.displaysurface.blit(self.mySurface, (mySurface_start_x, mySurface_start_y))
        self.displaysurface.blit(self.mySurface2, (mySurface_start_x, self.mySurface_length))
        self.mySurface.fill(view_helper.colors.GREY_LIGHT)
        self.mySurface2.fill(view_helper.colors.GREEN)

        self.button_start.draw()
        self.button_reset.draw()

    def draw_rectangle(self, i, j, color, surface) -> pygame.rect.Rect:
        return pygame.draw.rect(surface,
                                color,
                                [(MARGIN + self.width_cell) * j + MARGIN,
                                 (MARGIN + self.height_cell) * i + MARGIN,
                                 self.width_cell,
                                 self.height_cell])

    def draw_obstacles(self, area) -> None:
        for i in range(0, GRID_CELLS):
            for j in range(0, GRID_CELLS):
                if(area.cell_grid[i][j].obstacle):
                    self.draw_rectangle(i, j, view_helper.colors.BLACK, self.mySurface2)

    def draw_start_end_node(self, startNodeKoordinates, endNodeKoordinates) -> None:
        self.draw_rectangle(startNodeKoordinates[0], startNodeKoordinates[1], view_helper.colors.BLUE, self.mySurface2)
        self.draw_rectangle(endNodeKoordinates[0], endNodeKoordinates[1], view_helper.colors.BLUE, self.mySurface2)

    def draw_A_star_processing(self, a_star_search):
        if not(a_star_search.pathFound):
            for cell in a_star_search.openSet:
                self.draw_rectangle(cell.i, cell.j, view_helper.colors.GREEN, self.mySurface2)
            for cell in a_star_search.closedSet:
                self.draw_rectangle(cell.i, cell.j, view_helper.colors.RED, self.mySurface2)
        else:
            for cell in a_star_search.path:
                self.draw_rectangle(cell.i, cell.j, view_helper.colors.BLUE_LIGTH, self.mySurface2)

    def draw_basic_grid(self):
        for rectangle in self.rectangles:
            pygame.draw.rect(self.mySurface2,
                             view_helper.colors.WHITE,
                             rectangle.rectangle)

    def create_view_rectangles(self):
        for row in range(GRID_CELLS):
            for column in range(GRID_CELLS):
                rec: pygame.Rect = pygame.Rect((MARGIN + self.width_cell) * column + MARGIN,
                                               (MARGIN + self.height_cell) * row + MARGIN,
                                               self.width_cell,
                                               self.height_cell)
                rectangle = Rectangle(row, column, rec)
                self.rectangles.append(rectangle)
