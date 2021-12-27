from distance_grid import DistanceGrid
from recursive_backtracker import RecursiveBacktracker

grid = DistanceGrid(5, 5)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.braid(1)

grid.to_s()

start = grid[0, 0]
distances = start.distances()

grid.distances = distances
grid.to_s()

grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
grid.to_s()