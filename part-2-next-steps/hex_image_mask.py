from mask import Mask
from hex_masked_grid import HexMaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask.from_png("./masks/mask_maze_hex.png")

grid = HexMaskedGrid(mask)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png(size = 30)

# Optional lines to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(size = 30)