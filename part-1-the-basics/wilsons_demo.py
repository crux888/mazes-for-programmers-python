from grid import Grid
from wilsons import Wilsons

grid = Grid(20, 20)
algorithm = Wilsons()
algorithm.on(grid)

grid.to_s()
grid.to_png()