from grid import Grid
from recursive_backtracker import RecursiveBacktracker

grid = Grid(5, 5)

grid[0, 0].east.west = None
grid[0, 0].south.north = None

grid[4, 4].west.east = None
grid[4, 4].north.south = None

algorithm = RecursiveBacktracker()
algorithm.on(grid, start_at=grid[1, 1])

grid.to_s()
grid.to_png()