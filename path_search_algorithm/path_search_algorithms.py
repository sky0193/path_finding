from pickle import TRUE
import numpy as np
from typing import List

from py import process
from modules.cell import Cell

from modules.grid import Grid


def create_grid(rows, cols):
    ''' '''
    area: Grid = Grid(rows, cols)
    area.initialize_grid()
    area.print_grid()
    return area


class A_star_search_algorithm:
    def __init__(self, area: Grid, startNodeKoordinates, endNodeKoordinates):
        self.area = area
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False
        self.startNodeKoordinates = startNodeKoordinates
        self.endNodeKoordinates = endNodeKoordinates
        self.step_cost = 1

    def setup_A_Stern_setup(self):
        self.area.fill_neighbors_for_each_cell()
        self.openSet = [self.area.cell_grid[self.startNodeKoordinates[0]][self.startNodeKoordinates[1]]]

    def heuristic(self, point_a_x: float, point_a_y: float, point_b_x: float, point_b_y: float):
        return np.sqrt(float((point_a_x - point_b_x)**2 + (point_a_y - point_b_y)**2))

    def backtrack_path(self, endNode):
        self.path = [endNode]
        temp: Cell = endNode
        while(temp.previous):
            self.path.append(temp.previous)
            temp = temp.previous

    def set_more_optimal_neighbor(self, current, neighbor, g_from_current, heuristic):
        neighbor.g = g_from_current
        neighbor.h = heuristic
        neighbor.f = neighbor.g + neighbor.h
        neighbor.previous = current

    def process_current_node(self, current: Cell, endNode: Cell):
        self.openSet.remove(current)
        self.closedSet.append(current)
        neighbors: List[Cell] = current.neighbors

        for neighbor in neighbors:
            if not(neighbor in self.closedSet):
                g_from_current: float = current.g + self.step_cost
                if(g_from_current < neighbor.g):
                    heuristic_value = self.heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                    self.set_more_optimal_neighbor(current, neighbor, g_from_current, heuristic_value)
                if not(neighbor in self.openSet):
                    heuristic_value = self.heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                    self.set_more_optimal_neighbor(current, neighbor, g_from_current, heuristic_value)
                    self.openSet.append(neighbor)

    def check_no_path_exists(self):
        if(len(self.openSet) == 0):
            self.noPathExist = True
            return True

    def A_star_step(self, endNodeKoordinates):
        endNode = self.area.cell_grid[endNodeKoordinates[0]][endNodeKoordinates[1]]
        lowestIndex: int = 0
        for i in range(0, len(self.openSet)):
            if(self.openSet[i].f < self.openSet[lowestIndex].f):
                lowestIndex = i

        if(self.check_no_path_exists()):
            return

        current: Cell = self.openSet[lowestIndex]
        if(current == endNode):
            self.pathFound = True
            self.backtrack_path(endNode)
            return

        self.process_current_node(current, endNode)

    def reset(self):
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False
        self.area.initialize_grid()
