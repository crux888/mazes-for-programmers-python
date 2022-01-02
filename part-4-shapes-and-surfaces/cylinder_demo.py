from cylinder_grid import CylinderGrid
from recursive_backtracker import RecursiveBacktracker

grid = CylinderGrid(7, 16)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(cell_size = 10)