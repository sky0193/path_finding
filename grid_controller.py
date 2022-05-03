import pygame
from modules.grid import Grid
from path_search_algorithm.path_search_algorithms import A_star_search_algorithm, create_grid
from view_module.view import View
from typing import List
from constants import GRID_CELLS


def main():
    pygame.init()
    clock = pygame.time.Clock()

    done_main_loop: bool = False
    start_path_searching: bool = False
    setup_cells: bool = False

    start_node_coordinates = (0, 0)
    end_node_coordinates = (GRID_CELLS - 1, GRID_CELLS - 1)

    grid_view = View()
    area: Grid = create_grid(GRID_CELLS, GRID_CELLS)
    a_star_search = A_star_search_algorithm(area, start_node_coordinates, end_node_coordinates)

    while not done_main_loop:
        grid_view.update_surface()
        grid_view.create_view_rectangles()
        grid_view.draw_basic_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done_main_loop = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                global_pos = (pos[0], pos[1] - grid_view.mySurface_length)
                for rectangle in grid_view.rectangles:
                    if rectangle.rectangle.collidepoint(global_pos):
                        area.cell_grid[rectangle.i][rectangle.j].obstacle = True
                        pygame.display.flip()

        if(start_path_searching):
            if not(setup_cells):
                a_star_search.setup_A_Stern_setup()
                setup_cells = True

            a_star_search.A_star_step(endNodeKoordinates=end_node_coordinates)
            grid_view.draw_A_star_processing(a_star_search)

        grid_view.draw_obstacles(area)
        grid_view.draw_start_end_node(start_node_coordinates, end_node_coordinates)

        if grid_view.button_start.pressed:
            start_path_searching = True
        if grid_view.button_reset.pressed:
            start_path_searching = False
            setup_cells = False
            a_star_search.reset()

        clock.tick(20)
        pygame.display.update()


if __name__ == "__main__":
    main()
