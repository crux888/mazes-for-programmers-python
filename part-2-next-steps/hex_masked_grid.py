from hex_grid import HexGrid
from hex_cell import HexCell


class HexMaskedGrid(HexGrid):

    def __init__(self, mask):
        self.mask = mask
        super().__init__(self.mask.rows, self.mask.columns)

    def prepare_grid(self):
        list_of_cells = [[HexCell(row, column) if self.mask.bits[row][column] else None for column in range(self.columns)] for row in range(self.rows)]
        return(list_of_cells)

    def random_cell(self):
        row, column = self.mask.random_location()
        #return row, column
        return self[row, column]

    def size(self):
        return self.mask.count()
