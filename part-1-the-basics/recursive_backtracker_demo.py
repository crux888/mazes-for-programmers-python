from grid import Grid
from recursive_backtracker import RecursiveBacktracker

grid = Grid(20, 20)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_s()
grid.to_png()