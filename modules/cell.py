from typing import List

class Cell:
    def __init__(self, i: int, j: int):
        self.obstacle = False
        self.i: int = i
        self.j: int = j
        self.f: float = 0  # f(n) = g(n) + h(n)
        self.g: float = 0  # g(n), the distance from the start node to n
        self.h: float = 0  # heuristic function h(n), the estimated distance from node n to the goal node
        self.neighbors: List[Cell] = []
        self.previous = 0

    def print_location(self):
        print(f"({self.i} {self.j})", end='')
