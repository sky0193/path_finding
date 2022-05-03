from typing import List
from enum import Enum


class Cell:
    def __init__(self, i: int, j: int):
        self.obstacle = False
        self.i: int = i
        self.j: int = j
        self.f: float = 0  # f(n) = g(n) + h(n)
        self.g: float = 0  # g(n), the distance from the start node to n
        self.h: float = 0  # heuristic function h(n), the estimated distance from node n to the goal node
        self.neighbors: List[Cell] = []
        self.previous: Cell = None

    def print_location(self):
        print(f"({self.i} {self.j})", end='')

class CellWithWalls(Cell):
    def __init__(self, i: int, j: int):
        Cell.__init__(self=self, i=i, j=j)
        self.wall_left = False
        self.wall_rigth = False
        self.wall_top = True
        self.wall_bottom = True

class CellStatus(Enum):
    Unvisited = 1
    Wall = 2
    Free = 3

class CellMaze(Cell):
    def __init__(self, i: int, j: int):
        Cell.__init__(self=self, i=i, j=j)
        self.status = CellStatus.Unvisited
    
    def print(self):
        if(self.status == CellStatus.Unvisited):
            print("u", end='')
        if(self.status == CellStatus.Wall):
            print("w", end='')
        if(self.status == CellStatus.Free):
            print("f", end='')
