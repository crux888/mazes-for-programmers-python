from weave_grid import WeaveGrid
from recursive_backtracker import RecursiveBacktracker

grid = WeaveGrid(20, 20)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(cell_size = 20, inset = 0.1)

# Optional code to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(cell_size = 20, inset = 0.1)