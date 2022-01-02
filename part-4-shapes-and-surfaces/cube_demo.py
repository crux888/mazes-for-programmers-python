from cube_grid import CubeGrid
from recursive_backtracker import RecursiveBacktracker

grid = CubeGrid(10)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(cell_size = 20)