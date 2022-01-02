from grid3d import Cell3D, Grid3D
from recursive_backtracker import RecursiveBacktracker

grid = Grid3D (5, 5, 5)
algorithm = RecursiveBacktracker()
algorithm.on(grid)
grid.to_png(cell_size = 50)

# Optional lines to color the whole maze
start = grid[grid.levels // 2, grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(cell_size = 50)

# Optional lines to color a solution the maze
start = grid[0, 0, 0]
finish = grid[grid.levels - 1, grid.rows - 1, grid.columns - 1]
distances = start.distances()
grid.distances = distances
grid.distances = distances.path_to(finish)
grid.to_png(cell_size = 50)