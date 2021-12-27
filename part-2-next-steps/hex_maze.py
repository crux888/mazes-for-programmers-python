from hex_grid import HexGrid
from recursive_backtracker import RecursiveBacktracker

grid = HexGrid(20, 20)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(size = 30)

# Optional lines to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(size = 30)