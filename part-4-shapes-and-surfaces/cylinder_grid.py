from grid import Grid

class CylinderGrid(Grid):

    def __getitem__(self, key):
        row, column = key
        if row < 0 or row > self.rows - 1:
            return None
        column = column % len(self.grid[row])
        return self.grid[row][column]