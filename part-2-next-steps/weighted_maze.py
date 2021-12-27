from weighted_grid import WeightedGrid
from recursive_backtracker import RecursiveBacktracker
import random

grid = WeightedGrid(20, 20)
algorithm = RecursiveBacktracker()
algorithm.on(grid)
grid.braid(0.5)
grid.to_png()

start = grid[0, 0]
finish = grid[grid.rows - 1, grid.columns - 1]

distances = start.distances() 
max_cell, grid.maximum = distances.max()
grid.distances = distances.path_to(finish)
grid.to_png()

lava = (random.choice(list(grid.distances.cells)))
lava.weight = 50

distances = start.distances() 
max_cell, grid.maximum = distances.max()
grid.distances = distances.path_to(finish)
grid.to_png()