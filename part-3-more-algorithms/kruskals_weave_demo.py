from kruskals import Kruskals
from weave_grid import WeaveGrid
from weave_cells import OverCell, UnderCell
import random


class SimpleOverCell(OverCell):

    def neighbors(self):
        list=[]
        if self.north:
            list.append(self.north)
        if self.south:
            list.append(self.south)
        if self.east:
            list.append(self.east)
        if self.west:
            list.append(self.west)
        return list


class PreconfiguredGrid(WeaveGrid):

    def prepare_grid(self):
        return [[SimpleOverCell(row, column, self) for column in range(self.columns)] for row in range(self.rows)]


grid = PreconfiguredGrid(40, 40)
state = Kruskals.State(grid)

for _ in range(grid.size()):
    row = 1 + random.randrange(grid.rows - 2)
    column = 1 + random.randrange(grid.columns - 2)
    state.add_crossing(grid[row, column])

algorithm = Kruskals()
algorithm.on(grid, state)

grid.to_png(cell_size = 20, inset = 0.2)

# Optional lines to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(cell_size = 20, inset = 0.2)