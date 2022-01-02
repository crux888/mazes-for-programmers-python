from sphere_grid import SphereGrid
from recursive_backtracker import RecursiveBacktracker

grid = SphereGrid(20) 
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png()