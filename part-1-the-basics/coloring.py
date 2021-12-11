from colored_grid import ColoredGrid
from binary_tree import BinaryTree
from sidewinder import Sidewinder
from aldous_broder import AldousBroder
from wilsons import Wilsons
from hunt_and_kill import HuntAndKill
from recursive_backtracker import RecursiveBacktracker


grid = ColoredGrid(37, 37)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()

grid.to_s()
grid.to_png()
