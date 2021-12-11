from grid import Grid
from sidewinder import Sidewinder

grid = Grid(20, 20)
algorithm = Sidewinder()
algorithm.on(grid)

grid.to_s()
grid.to_png()