import pygame
from path_search_algorithms import A_star_search_algorithm, create_grid
import view_helper.colors
from view_modules.button import Button
from typing import List
from rectangle import Rectangle

WIDTH = 600
HEIGHT = 600
WINDOWSIZE = WIDTH, HEIGHT

GRID_CELLS = 5

LENGTH_FIRST_SURFACE = 100
LENGTH_SECOND_SURFACE = (HEIGHT - LENGTH_FIRST_SURFACE)


# This sets the margin between each cell
MARGIN = 1
MARGIN_WIDTH = MARGIN * GRID_CELLS + 2
MARGIN_LENGTH = MARGIN * GRID_CELLS + 2

WIDTH_CELL = (WIDTH - MARGIN_WIDTH) / GRID_CELLS
HEIGHT_CELL = (LENGTH_SECOND_SURFACE - MARGIN_LENGTH) / GRID_CELLS


def set_up_start_button(mySurface) -> Button:
    button_start_pos_x = 10
    button_start_pos_y = LENGTH_FIRST_SURFACE / 2
    button_start_pos_width = 60
    button_start_pos_heigth = 30
    button_start_elevation = 10
    button_start: Button = Button('Start', button_start_pos_x, button_start_pos_y, button_start_pos_width,
                                  button_start_pos_heigth, button_start_elevation, mySurface)
    return button_start


def set_up_reset_button(mySurface) -> Button:
    button_reset_pos_x = WIDTH / 3
    button_reset_pos_y = LENGTH_FIRST_SURFACE / 2
    button_reset_pos_width = 60
    button_reset_pos_heigth = 30
    button_reset_elevation = 10
    button_reset: Button = Button('Reset', button_reset_pos_x, button_reset_pos_y, button_reset_pos_width,
                                  button_reset_pos_heigth, button_reset_elevation, mySurface)
    return button_reset


def draw_rectangle(i, j, color, surface) -> pygame.Rect:
    return pygame.draw.rect(surface,
                            color,
                            [(MARGIN + WIDTH_CELL) * j + MARGIN,
                             (MARGIN + HEIGHT_CELL) * i + MARGIN,
                             WIDTH_CELL,
                             HEIGHT_CELL])


def draw_obstacles(area, mySurface2) -> None:
    for i in range(0, GRID_CELLS):
        for j in range(0, GRID_CELLS):
            if(area.cell_grid[i][j].obstacle):
                draw_rectangle(i, j, view_helper.colors.BLACK, mySurface2)


def draw_start_end_node(startNodeKoordinates, endNodeKoordinates, mySurface2) -> None:
    draw_rectangle(startNodeKoordinates[0], startNodeKoordinates[1], view_helper.colors.BLUE, mySurface2)
    draw_rectangle(endNodeKoordinates[0], endNodeKoordinates[1], view_helper.colors.BLUE, mySurface2)


def draw_basic_grid(area, mySurface2) -> List[Rectangle]:
    rectangles = []
    for row in range(GRID_CELLS):
        for column in range(GRID_CELLS):
            color = view_helper.colors.WHITE
            if area.cell_grid[row][column] == 1:
                color = view_helper.colors.GREEN
            rec: pygame.Rect = draw_rectangle(row, column, color, mySurface2)
            rectangle = Rectangle(row, column, rec)
            rectangles.append(rectangle)
    return rectangles

def draw_A_star_processing(a_star_search, mySurface2):
    if not(a_star_search.pathFound):
        for cell in a_star_search.openSet:
            draw_rectangle(cell.i, cell.j, view_helper.colors.GREEN, mySurface2)
        for cell in a_star_search.closedSet:
            draw_rectangle(cell.i, cell.j, view_helper.colors.RED, mySurface2)
    else:
        for cell in a_star_search.path:
            draw_rectangle(cell.i, cell.j, view_helper.colors.BLUE_LIGTH, mySurface2)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    displaysurface = pygame.display.set_mode(WINDOWSIZE)

    mySurface_width = WIDTH
    mySurface_length = LENGTH_FIRST_SURFACE
    mySurface = pygame.Surface((mySurface_width, mySurface_length))
    mySurface.fill(view_helper.colors.GREY_LIGHT)

    mySurface2_width = WIDTH
    mySurface2_length = HEIGHT - mySurface_length
    mySurface2 = pygame.Surface((mySurface2_width, mySurface2_length))
    mySurface2.fill(view_helper.colors.GREEN)

    done = False

    button_start = set_up_start_button(mySurface)
    button_reset = set_up_reset_button(mySurface)

    start_algorithm = False
    
    area = create_grid(GRID_CELLS, GRID_CELLS)
    a_star_search = A_star_search_algorithm(area)

    setUPCells = False

    startNodeKoordinates = (0, 0)
    endNodeKoordinates = (GRID_CELLS - 1, GRID_CELLS - 1)

    while not done:
        mySurface_start_x = 0
        mySurface_start_y = 0
        displaysurface.blit(mySurface, (mySurface_start_x, mySurface_start_y))
        displaysurface.blit(mySurface2, (mySurface_start_x, mySurface_length))

        rectangles: List[Rectangle] = draw_basic_grid(area, mySurface2)

        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                global_pos = (pos[0], pos[1] - LENGTH_FIRST_SURFACE)

                # Debug Click Information
                for rectangle in rectangles:
                    if rectangle.rectangle.collidepoint(global_pos):
                        print(f"Pos: {pos} Global: {global_pos} Rect: i [{rectangle.i}] j[{rectangle.j}]")
                        area.cell_grid[rectangle.i][rectangle.j].obstacle = True

                        # Update the screen
                        pygame.display.flip()

        if(start_algorithm):
            if not(setUPCells):
                a_star_search.setup_A_Stern_sets(
                    startNodeKoordinates=startNodeKoordinates)
                setUPCells = True

            a_star_search.A_star(endNodeKoordinates=endNodeKoordinates)
            draw_A_star_processing(a_star_search, mySurface2)

        draw_obstacles(area, mySurface2)
        draw_start_end_node(startNodeKoordinates, endNodeKoordinates, mySurface2)

        mySurface.fill(view_helper.colors.GREY_LIGHT)

        button_start.draw()
        button_reset.draw()

        if(button_start.pressed):
            start_algorithm = True
        if(button_reset.pressed):
            start_algorithm = False
            setUPCells = False
            a_star_search.reset()

        clock.tick(20)
        pygame.display.update()


if __name__ == "__main__":
    main()
