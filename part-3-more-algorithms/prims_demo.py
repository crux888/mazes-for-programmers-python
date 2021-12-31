from prims import SimplifiedPrims, TruePrims
from colored_grid import ColoredGrid

rows = 40
columns = 40
start_row = rows // 2
start_column = columns // 2

# Simplified Prims
grid = ColoredGrid(rows, columns)
algorithm = SimplifiedPrims()
start = grid[start_row, start_column]
algorithm.on(grid, start_at = start)
grid.to_png(cell_size = 20)
grid.distances = start.distances()
grid.to_png(cell_size = 20)

# True Prims
grid = ColoredGrid(rows, columns)
algorithm = TruePrims()
start = grid[start_row, start_column]
algorithm.on(grid, start_at = start)
grid.to_png(cell_size = 20)
grid.distances = start.distances()
grid.to_png(cell_size = 20)