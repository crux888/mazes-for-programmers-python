from triangle_grid import TriangleGrid
from recursive_backtracker import RecursiveBacktracker

grid = TriangleGrid(20, 34)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(size = 50)

# Optional code to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(size = 50)