from pickle import TRUE
import numpy as np
from typing import List

class Grid:
    '''Grid class'''
    def __init__(self, rows: int, col: int):
        self.rows: int = rows
        self.cols: int = col
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False
        self.cell_grid = []

    def initialize_grid(self):
        self.cell_grid = [["" for y in range(self.rows)] for x in range(self.cols)]
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.cell_grid[i][j] = Cell(i, j)

    def print_grid(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.cell_grid[i][j].print_location()
            print("\n", end='')

    def reset(self):
        self.openSet: List[Cell] = []
        self.closedSet: List[Cell] = []
        self.path: List[Cell] = []
        self.pathFound: bool = False
        self.noPathExist: bool = False
        self.initialize_grid()


class Cell:
    def __init__(self, i, j):
        self.obstacle = False
        self.i: int = i
        self.j: int = j
        self.f: float = 0  # f(n) = g(n) + h(n)
        self.g: float = 0  # g(n), the distance from the start node to n
        self.h: float = 0  # heuristic function h(n), the estimated distance from node n to the goal node
        self.neighbors = []
        self.previous = 0

    def print_location(self):
        print(f"({self.i} {self.j})", end='')

    # TODO
    def add_neighbors(self, area_grid, rows, cols):

        if(self.obstacle):
            return

        i = self.i
        j = self.j
        if(i < cols - 1):
            neighbor = area_grid[i + 1][j]
            if not(neighbor.obstacle):
                self.neighbors.append(neighbor)
        if(i > 0):
            neighbor = area_grid[i - 1][j]
            if not(neighbor.obstacle):
                self.neighbors.append(neighbor)
        if(j < rows - 1):
            neighbor = area_grid[i][j + 1]
            if not(neighbor.obstacle):
                self.neighbors.append(neighbor)
        if(j > 0):
            neighbor = area_grid[i][j - 1]
            if not(neighbor.obstacle):
                self.neighbors.append(neighbor)


def create_grid(rows, cols):
    ''' '''
    area: Grid = Grid(rows, cols)
    area.initialize_grid()
    area.print_grid()
    return area

def setup_A_Stern_sets(area, startNodeKoordinates):

    for i in range(0, area.rows):
        for j in range(0, area.cols):
            area.cell_grid[i][j].add_neighbors(area.cell_grid, area.rows, area.cols)

    # A_star_setup
    # Nodes that still needs to be evaluated
    area.openSet = [area.cell_grid[startNodeKoordinates[0]][startNodeKoordinates[1]]]

def heuristic(point_a_x: float, point_a_y: float, point_b_x: float, point_b_y: float):
    return np.sqrt(float((point_a_x - point_b_x)**2 + (point_a_y - point_b_y)**2))

# One Step of A_star_algoithm
def A_star(area: Grid, endNodeKoordinates):
    endNode = area.cell_grid[endNodeKoordinates[0]][endNodeKoordinates[1]]
    lowestIndex: int = 0
    for i in range(0, len(area.openSet)):
        if(area.openSet[i].f < area.openSet[lowestIndex].f):
            lowestIndex = i

    if(len(area.openSet) == 0):
        area.noPathExist = True
        return
    current: Cell = area.openSet[lowestIndex]
    if(current == endNode):
        area.pathFound = True
        area.path = [endNode]
        temp: Cell = current
        while(temp.previous):
            area.path.append(temp.previous)
            temp = temp.previous
        return

    area.openSet.remove(current)
    area.closedSet.append(current)

    neighbors: List[Cell] = current.neighbors
    for neighbor in neighbors:
        if not(neighbor in area.closedSet):
            g_from_current: float = current.g + 1
            if(neighbor in area.openSet):
                if(g_from_current < neighbor.g):
                    neighbor.g = g_from_current
                    neighbor.h = heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
            else:
                neighbor.g = g_from_current
                neighbor.h = heuristic(neighbor.i, neighbor.j, endNode.i, endNode.j)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current
                area.openSet.append(neighbor)
    return
