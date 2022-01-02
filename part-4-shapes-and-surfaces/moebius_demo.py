from moebius_grid import MoebiusGrid
from recursive_backtracker import RecursiveBacktracker

grid = MoebiusGrid(5, 50)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(cell_size = 15)