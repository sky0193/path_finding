
import random
from sklearn import neighbors

from modules.cell import CellMaze, CellStatus
from modules.grid import Grid, GridMaze
from typing import Tuple, List

class MazeRandomDFS:
    def __init__(self, area: GridMaze, startNodeKoordinates: Tuple[int, int]):
        self.area = area

        self.startNodeKoordinates: Tuple[int, int] = startNodeKoordinates
        self.endNodeKoordinates: Tuple[int, int] = [0,0]


        self.start_Node_initial = self.area.cell_grid[startNodeKoordinates[0]][startNodeKoordinates[1]]
        self.start_Node = self.area.cell_grid[startNodeKoordinates[0]+1][startNodeKoordinates[1]]

        self.start_Node.status = CellStatus.Free
        self.stack: List(CellMaze) = [self.start_Node]

    def process(self):
        got_end_cell = False
        while(len(self.stack) > 0):
            current: CellMaze = self.stack.pop()
 
            next = get_random_neighbor(self.area, current)
            if next:
                self.stack.append(current)
                remove_wall(current, next, self.area)
                self.stack.append(next)
                next.status = CellStatus.Free
            else:
                if not(got_end_cell):
                    self.area.print_dfs_grid()
                    print("\n\n")
                    if(current.i + 2 == self.area.rows):
                        got_end_cell = True
                        self.endNodeKoordinates = [current.i +1, current.j]
                    if(current.j + 2 == self.area.cols):
                        got_end_cell = True
                        self.endNodeKoordinates = [current.i, current.j+1]
            self.set_obstacles_to_unvisited_cells()


    def set_obstacles_to_unvisited_cells(self):
        for i in range(0, self.area.rows):
                for j in range(0, self.area.cols):
                    self.area.cell_grid[i][j].obstacle = self.area.cell_grid[i][j].status == CellStatus.Unvisited
        self.area.cell_grid[self.start_Node_initial.i][self.start_Node_initial.j].obstacle = False
        self.area.cell_grid[self.endNodeKoordinates[0]][self.endNodeKoordinates[1]].obstacle = False

def remove_wall(current: CellMaze, next: CellMaze, area: GridMaze):
    middle_position_i = int((current.i + next.i)/2)
    middle_position_j = int((current.j + next.j)/2)

    area.cell_grid[middle_position_i][middle_position_j].status = CellStatus.Free

def get_random_neighbor(area: GridMaze,current: CellMaze):
    unvisited_neighbors: List[CellMaze] = []

    if(current.i+2 < area.rows):
        neighbor = area.cell_grid[current.i+2][current.j]
        if neighbor.status == CellStatus.Unvisited:
            unvisited_neighbors.append(neighbor) 
    if(current.i-2 > 0):
        neighbor = area.cell_grid[current.i-2][current.j]
        if neighbor.status == CellStatus.Unvisited:
            unvisited_neighbors.append(neighbor)
    if(current.j+2 < area.cols):
        neighbor = area.cell_grid[current.i][current.j+2]
        if neighbor.status == CellStatus.Unvisited:
            unvisited_neighbors.append(neighbor)
    if(current.j-2 > 0):
        neighbor = area.cell_grid[current.i][current.j-2]
        if neighbor.status == CellStatus.Unvisited:
            unvisited_neighbors.append(neighbor)
    if(unvisited_neighbors):
        return random.choice(unvisited_neighbors) 
