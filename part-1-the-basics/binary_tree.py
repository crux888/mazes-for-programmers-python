from grid import Grid
from random import choice


class BinaryTree:

    def on(self, grid: Grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)
                
            if len(neighbors) > 0:
                neighbor = choice(neighbors)
                cell.link(neighbor)