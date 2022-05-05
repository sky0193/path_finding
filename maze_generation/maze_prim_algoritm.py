
import random

from torch import true_divide
from modules.cell import CellMaze, CellStatus
from modules.grid import Grid, GridMaze
from typing import Tuple, List


class MazeRandomPrim:
    def __init__(self, area: GridMaze, startNodeKoordinates: Tuple[int, int], endNodeKoordinates: Tuple[int, int]):
        self.area = area

        self.startNodeKoordinates: Tuple[int, int] = startNodeKoordinates
        self.endNodeKoordinates: Tuple[int, int] = endNodeKoordinates

        self.start_Node = self.area.cell_grid[startNodeKoordinates[0]][startNodeKoordinates[1]]
        self.end_Node = self.area.cell_grid[endNodeKoordinates[0]][endNodeKoordinates[1]]

        self.stack: List(CellMaze) = [self.start_Node]

    def process(self):
        self.area.fill_neighbors_for_each_cell()

        starting_height = random.randint(1, self.area.cols)
        starting_width = random.randint(1, self.area.rows)

        self.area[starting_height][starting_width].status = CellStatus.Free
        walls = []

        walls.append([starting_height-1, starting_width])
        walls.append([starting_height, starting_width-1])
        walls.append([starting_height, starting_width+1])
        walls.append([starting_height+1, starting_width])

        self.area[starting_height-1, starting_width].status = CellStatus.Wall
        self.area[starting_height, starting_width-1].status = CellStatus.Wall
        self.area[starting_height, starting_width+1].status = CellStatus.Wall
        self.area[starting_height+1, starting_width].status = CellStatus.Wall
        
        while(len(walls) > 0):
            current: CellMaze = self.stack.pop()
            rand_wall = walls[int(random.random()*len(walls))-1]
            if rand_wall[1] != 0:
                if self.area[rand_wall[0]][rand_wall[1] - 1].status == CellStatus.Unvisited and \
                   self.area[rand_wall[0]][rand_wall[1] + 1].status == CellStatus.Free:

            if rand_wall[0] != 0:  
                if self.area[rand_wall[0]-1][rand_wall[1]].status == CellStatus.Unvisited and \
                   self.area[rand_wall[0]+1][rand_wall[1]+1].status == CellStatus.Free:

            if rand_wall[0] != self.area.cols-1:
                if self.area[rand_wall[0]+1][rand_wall[1]].status == CellStatus.Unvisited and \
                   self.area[rand_wall[0]-1][rand_wall[1]].status == CellStatus.Free:

            if rand_wall[1] != self.area.rows-1:
                if self.area[rand_wall[0]][rand_wall[1]+1].status == CellStatus.Unvisited and \
                       self.area[rand_wall[0]][rand_wall[1]-1].status == CellStatus.Free:

#            if current and not current.visited :
#                current.visited = True
#
#                next = get_random_neighbor(current)
#                current = next
#                self.stack.append(next)
#
            self.area.print_dfs_grid()
            print("\n\n")

                               

    def surroundingCells(self, rand_wall):
        s_cells = 0
        if (self.area[rand_wall[0]-1][rand_wall[1]].status == 'c'):
            s_cells += 1
        if (self.area[rand_wall[0]+1][rand_wall[1]].status == 'c'):
            s_cells += 1
        if (self.area[rand_wall[0]][rand_wall[1]-1] == 'c'):
            s_cells +=1
        if (self.area[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells += 1    
            return s_cells




def get_random_neighbor(current):
    unvisited_neighbors: List[CellMaze] = [neighbor for neighbor in current.neighbors if not neighbor.visited]
    if(unvisited_neighbors):
        return random.choice(unvisited_neighbors) 