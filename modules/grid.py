from typing import List
from modules.cell import Cell

class Grid:
    '''Grid class'''
    def __init__(self, rows: int, col: int):
        '''
        :param rows: number of rows in grid
        :param col: number of colums in grid
        '''
        self.rows: int = rows
        self.cols: int = col
        self.cell_grid: List[List[Cell]] = []

    def initialize_grid(self) -> None:
        self.cell_grid = [[Cell(x, y) for y in range(self.rows)] for x in range(self.cols)]

    def print_grid(self) -> None:
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.cell_grid[i][j].print_location()
            print("\n", end='')

    def fill_neighbors_for_each_cell(self) -> None:
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.add_neighbors(i=i, j=j, rows=self.rows, cols=self.cols)

    # TODO look for better implementation
    def add_neighbors(self, i: int, j: int, rows: int, cols: int) -> None:
        if(self.cell_grid[i][j].obstacle):
            return
        if(i < cols - 1):
            neighbor = self.cell_grid[i + 1][j]
            if not(neighbor.obstacle):
                self.cell_grid[i][j].neighbors.append(neighbor)
        if(i > 0):
            neighbor = self.cell_grid[i - 1][j]
            if not(neighbor.obstacle):
                self.cell_grid[i][j].neighbors.append(neighbor)
        if(j < rows - 1):
            neighbor = self.cell_grid[i][j + 1]
            if not(neighbor.obstacle):
                self.cell_grid[i][j].neighbors.append(neighbor)
        if(j > 0):
            neighbor = self.cell_grid[i][j - 1]
            if not(neighbor.obstacle):
                self.cell_grid[i][j].neighbors.append(neighbor)
