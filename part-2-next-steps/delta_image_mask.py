from mask import Mask
from triangle_masked_grid import TriangleMaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask.from_png("./masks/mask_maze_triangle.png")

grid = TriangleMaskedGrid(mask)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(size = 30)

# Optional code to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(size = 30)