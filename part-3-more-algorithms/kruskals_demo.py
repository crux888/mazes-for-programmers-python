from kruskals import Kruskals
from colored_grid import ColoredGrid

grid = ColoredGrid(40, 40)
algorithm = Kruskals()
algorithm.on(grid)

grid.to_png(cell_size = 20)

# Optional lines to color the maze
start = grid[grid.rows // 2, grid.columns // 2]
grid.distances = start.distances()
grid.to_png(cell_size = 20)