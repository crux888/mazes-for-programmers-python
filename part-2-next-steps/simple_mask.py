from mask import Mask
from masked_grid import MaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask(5, 5)

mask[0, 0] = False
mask[2, 2] = False
mask[4, 4] = False

grid = MaskedGrid(mask)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_s()
grid.to_png()