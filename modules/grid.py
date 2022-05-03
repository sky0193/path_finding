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
        
        self.cell_grid = []

    def initialize_grid(self):
        self.cell_grid = [[Cell(x, y) for y in range(self.rows)] for x in range(self.cols)]

    def print_grid(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.cell_grid[i][j].print_location()
            print("\n", end='')
