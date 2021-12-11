from distance_grid import DistanceGrid
from binary_tree import BinaryTree
from sidewinder import Sidewinder
from aldous_broder import AldousBroder
from wilsons import Wilsons
from recursive_backtracker import RecursiveBacktracker

grid = DistanceGrid(8, 8)
algorithm = BinaryTree()
algorithm.on(grid)
grid.to_s()

start = grid[0, 0]

distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

grid.distances = new_distances.path_to(goal)
grid.to_s()