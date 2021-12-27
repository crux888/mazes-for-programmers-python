from grid import Grid
from weighted_cell import WeightedCell


class WeightedGrid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None
        self.maximum = 0

    def prepare_grid(self):
        return [[WeightedCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def background_color_for(self, cell):
        if cell.weight > 1:
            return (255, 0, 0)
        elif self.distances is not None and self.distances[cell] is not None:
            if self.maximum == 0:
                farthest, self.maximum = self.distances.max()
            distance = self.distances[cell]
            intensity = int(64 + 191 * (self.maximum - distance) / self.maximum)
            return (intensity, intensity, 0)
        else:
            return None