from pickle import TRUE
import numpy as np
from typing import List
from modules.cell import Cell

from modules.grid import Grid


def create_grid(rows, cols):
    ''' '''
    area: Grid = Grid(rows, cols)
    area.initialize_grid()
    area.print_grid()

    return area


class A_star_search_algorithm:
    def __init__(self, area: Grid):
        self.area = area
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False

    def setup_A_Stern_sets(self, startNodeKoordinates):

        for i in range(0, self.area.rows):
            for j in range(0, self.area.cols):
                self.area.cell_grid[i][j].add_neighbors(self.area.cell_grid, self.area.rows, self.area.cols)

        # A_star_setup
        # Nodes that still needs to be evaluated
        self.openSet = [self.area.cell_grid[startNodeKoordinates[0]][startNodeKoordinates[1]]]

    def heuristic(self, point_a_x: float, point_a_y: float, point_b_x: float, point_b_y: float):
        return np.sqrt(float((point_a_x - point_b_x)**2 + (point_a_y - point_b_y)**2))

    # One Step of A_star_algoithm
    def A_star(self, endNodeKoordinates):
        endNode = self.area.cell_grid[endNodeKoordinates[0]][endNodeKoordinates[1]]
        lowestIndex: int = 0
        for i in range(0, len(self.openSet)):
            if(self.openSet[i].f < self.openSet[lowestIndex].f):
                lowestIndex = i

        if(len(self.openSet) == 0):
            self.noPathExist = True
            return
        current: Cell = self.openSet[lowestIndex]
        if(current == endNode):
            self.pathFound = True
            self.path = [endNode]
            temp: Cell = current
            while(temp.previous):
                self.path.append(temp.previous)
                temp = temp.previous
            return

        self.openSet.remove(current)
        self.closedSet.append(current)

        neighbors: List[Cell] = current.neighbors
        for neighbor in neighbors:
            if not(neighbor in self.closedSet):
                g_from_current: float = current.g + 1
                if(neighbor in self.openSet):
                    if(g_from_current < neighbor.g):
                        neighbor.g = g_from_current
                        neighbor.h = self.heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.previous = current
                else:
                    neighbor.g = g_from_current
                    neighbor.h = self.heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
                    self.openSet.append(neighbor)
        return

    def reset(self):
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False
        self.area.initialize_grid()
