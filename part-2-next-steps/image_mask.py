from mask import Mask
from masked_grid import MaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask.from_png("./masks/mask_maze_star_small.png")

grid = MaskedGrid(mask)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_png()

# Optional code to color the maze
# Start coloring from the center of the maze
start = grid[grid.rows // 2, grid.columns // 2]
# Start coloring from a random point in the maze
# start = grid.random_cell()  
grid.distances = start.distances()
grid.to_png()