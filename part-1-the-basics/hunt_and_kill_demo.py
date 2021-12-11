from grid import Grid
from hunt_and_kill import HuntAndKill

grid = Grid(20, 20)
algorithm = HuntAndKill()
algorithm.on(grid)

grid.to_s()
grid.to_png()