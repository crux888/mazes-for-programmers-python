from ellers import Ellers
from colored_grid import ColoredGrid

grid = ColoredGrid(40, 40)
algorithm = Ellers()
algorithm.on(grid)

grid.to_png(cell_size = 20)

# Optional code to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(cell_size = 20)