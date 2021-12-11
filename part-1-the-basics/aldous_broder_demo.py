from grid import Grid
from aldous_broder import AldousBroder

grid = Grid(20, 20)
algorithm = AldousBroder()
algorithm.on(grid)

grid.to_s()
grid.to_png()