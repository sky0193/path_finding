﻿import numpy as np
import view_helper

def main():
    rows_size, col_size = view_helper.GRID_CELLS, view_helper.GRID_CELLS
    area = Grid(rows_size, col_size )
    print(area.grid)

    source = (0, 5)
    dest = ()

class Grid:
    '''Grid class'''
    def __init__(self, rows_size, col_size):
        self.rows = rows_size
        self.cols = col_size
        self.grid = [["" for y in range(self.rows)] for x in range(self.cols)]
    pass


    
if __name__ == '__main__':
    main()