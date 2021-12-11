from grid import Grid
from binary_tree import BinaryTree

grid = Grid(20, 20)
algorithm = BinaryTree()
algorithm.on(grid)

grid.to_s()
grid.to_png()