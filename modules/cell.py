
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

