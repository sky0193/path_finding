import pygame
from path_search_algorithms import A_star_search_algorithm, create_grid
from view_module.view import View
from typing import List
from constants import GRID_CELLS


def main():
    pygame.init()
    clock = pygame.time.Clock()

    grid_view = View()

    done = False
    start_algorithm = False

    area = create_grid(GRID_CELLS, GRID_CELLS)

    startNodeKoordinates = (0, 0)
    endNodeKoordinates = (GRID_CELLS - 1, GRID_CELLS - 1)
    a_star_search = A_star_search_algorithm(area, startNodeKoordinates, endNodeKoordinates)

    setUPCells = False

    while not done:
        grid_view.update_surface()
        grid_view.create_view_rectangles()
        grid_view.draw_basic_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                global_pos = (pos[0], pos[1] - grid_view.mySurface_length)
                for rectangle in grid_view.rectangles:
                    if rectangle.rectangle.collidepoint(global_pos):
                        area.cell_grid[rectangle.i][rectangle.j].obstacle = True
                        pygame.display.flip()

        if(start_algorithm):
            if not(setUPCells):
                a_star_search.setup_A_Stern_setup()
                setUPCells = True

            a_star_search.A_star_step(endNodeKoordinates=endNodeKoordinates)
            grid_view.draw_A_star_processing(a_star_search)

        grid_view.draw_obstacles(area)
        grid_view.draw_start_end_node(startNodeKoordinates, endNodeKoordinates)

        if grid_view.button_start.pressed:
            start_algorithm = True
        if grid_view.button_reset.pressed:
            start_algorithm = False
            setUPCells = False
            a_star_search.reset()

        clock.tick(20)
        pygame.display.update()


if __name__ == "__main__":
    main()
