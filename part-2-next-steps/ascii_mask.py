from mask import Mask
from masked_grid import MaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask.from_txt("./masks/mask.txt")

grid = MaskedGrid(mask)
algorithm = RecursiveBacktracker()
algorithm.on(grid)

grid.to_s()
grid.to_png()