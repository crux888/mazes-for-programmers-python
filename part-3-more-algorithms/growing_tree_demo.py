from growing_tree import GrowingTree
from colored_grid import ColoredGrid
import random

rows = 40
columns = 40
start_row = rows // 2
start_column = columns // 2

# Growing Tree (random)
grid = ColoredGrid(rows, columns)
algorithm = GrowingTree()
start = grid[start_row, start_column]
algorithm.on(grid, start_at = start, block = lambda x:random.choice(x)) # Random value
grid.distances = start.distances()
grid.to_png(cell_size = 20)

# Growing Tree (last)
grid = ColoredGrid(rows, columns)
algorithm = GrowingTree()
start = grid[start_row, start_column]
algorithm.on(grid, start_at = start, block = lambda x:x[-1]) # Last value
grid.distances = start.distances()
grid.to_png(cell_size = 20)

# Growing Tree (mixed)
grid = ColoredGrid(rows, columns)
algorithm = GrowingTree()
start = grid[start_row, start_column]
algorithm.on(grid, start_at = start, block = lambda x: random.choice(x) if random.randrange(2) == 0 else x[-1]) # Mixed
grid.distances = start.distances()
grid.to_png(cell_size = 20)


