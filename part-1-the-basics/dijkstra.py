from grid import Grid
from distance_grid import DistanceGrid
from binary_tree import BinaryTree
from sidewinder import Sidewinder
from aldous_broder import AldousBroder

grid = DistanceGrid(10, 10)
algorithm = AldousBroder()
algorithm.on(grid)
grid.to_s()

start = grid[0, 0]
distances = start.distances()

grid.distances = distances
grid.to_s()

grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
grid.to_s()