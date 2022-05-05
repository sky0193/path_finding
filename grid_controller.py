import pygame
from maze_generation.maze_algorithm import MazeRandomDFS
from modules.cell import CellStatus, CellWithWalls
from modules.grid import Grid, GridMaze
from path_search_algorithm.path_search_algorithms import AStarSearchAlgorithm, create_grid, create_grid_Maze
from view_module.view import View
from typing import List
from constants import GRID_CELLS

def main():
    pygame.init()
    clock = pygame.time.Clock()

    done_main_loop: bool = False
    start_path_searching: bool = False
    setup_cells: bool = False


    start_node_coordinates_x = 0
    start_node_coordinates_y = 5
    start_node_coordinates = (start_node_coordinates_x, start_node_coordinates_y)

    grid_view = View()
    areaMaze: GridMaze = create_grid_Maze(GRID_CELLS, GRID_CELLS)

    maze = MazeRandomDFS(areaMaze, (start_node_coordinates_x, start_node_coordinates_y))
    maze.process()
    area = maze.area
    end_node_coordinates = maze.endNodeKoordinates

    a_star_search = AStarSearchAlgorithm(maze.area, start_node_coordinates, end_node_coordinates)


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

        grid_view.draw_start_end_node(start_node_coordinates, end_node_coordinates)
        grid_view.draw_obstacles(area)

        if grid_view.button_start.pressed:
            start_path_searching = True
        if grid_view.button_reset.pressed:
            start_path_searching = False
            setup_cells = False
            a_star_search.reset()
        if grid_view.generate_maze.pressed:
            areaMaze: GridMaze = create_grid_Maze(GRID_CELLS, GRID_CELLS)

            maze = MazeRandomDFS(areaMaze, (start_node_coordinates_x + 1, start_node_coordinates_y))
            maze.process()
            end_node_coordinates = maze.endNodeKoordinates
            a_star_search = AStarSearchAlgorithm(area, start_node_coordinates, end_node_coordinates)
            for i in range(0, areaMaze.rows):
                    for j in range(0, areaMaze.cols):
                        area.cell_grid[i][j].obstacle = areaMaze.cell_grid[i][j].status == CellStatus.Unvisited
            area.cell_grid[start_node_coordinates_x][start_node_coordinates_y].obstacle = False
            area.cell_grid[end_node_coordinates[0]][end_node_coordinates[1]].obstacle = False
            
 
        

        #clock.tick(20)
        pygame.display.update()


if __name__ == "__main__":
    main()
