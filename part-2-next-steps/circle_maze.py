from polar_grid import PolarGrid
from recursive_backtracker import RecursiveBacktracker

grid = PolarGrid(40)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(cell_size = 20)

# Optional lines to color the maze
start = grid[0, 1]
grid.distances = start.distances()
grid.to_png(cell_size = 20)