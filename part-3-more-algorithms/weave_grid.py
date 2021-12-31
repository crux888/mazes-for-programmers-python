from colored_grid import ColoredGrid
from weave_cells import OverCell, UnderCell

DRAW_BACKGROUND = 0


class WeaveGrid(ColoredGrid):

    def __init__(self, rows, columns):
        self.under_cells = []
        super().__init__(rows, columns)

    def prepare_grid(self):
        return [[OverCell(row, column, self) for column in range(self.columns)] for row in range(self.rows)]

    def tunnel_under(self, over_cell):
        under_cell = UnderCell(over_cell)
        self.under_cells.append(under_cell)

    def each_cell(self):
        list_of_cells = []
        for row in self.each_row():
            for cell in row:
                if cell is not None:
                    list_of_cells.append(cell)
        for cell in self.under_cells:
            if cell is not None:
                list_of_cells.append(cell)
        return(list_of_cells)

    def to_png(self, cell_size: int = 10, inset = 0):
        if inset == 0:
            inset = 0.1
        super().to_png(cell_size = cell_size, inset = inset)
        
    def to_png_with_inset(self, draw, cell, mode, cell_size, wall, x, y, inset):
        if isinstance(cell, OverCell):
            super().to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
            x1, x2, x3, x4, y1, y2, y3, y4 = self.cell_coordinates_with_inset(x, y, cell_size, inset)
            if mode == DRAW_BACKGROUND:
                color = self.background_color_for(cell)
                if cell.vertical_passage():
                    draw.rectangle((x2, y1, x3, y2), fill = color)
                    draw.rectangle((x2, y3, x3, y4), fill = color)
                else:
                    draw.rectangle((x1, y2, x2, y3), fill = color)
                    draw.rectangle((x3, y2, x4, y3), fill = color)
            else:
                if cell.vertical_passage():
                    draw.line([x2, y1, x2, y2], fill = wall, width = 1)
                    draw.line([x3, y1, x3, y2], fill = wall, width = 1)
                    draw.line([x2, y3, x2, y4], fill = wall, width = 1)
                    draw.line([x3, y3, x3, y4], fill = wall, width = 1)
                else:
                    draw.line([x1, y2, x2, y2], fill = wall, width = 1)
                    draw.line([x1, y3, x2, y3], fill = wall, width = 1)
                    draw.line([x3, y2, x4, y2], fill = wall, width = 1)
                    draw.line([x3, y3, x4, y3], fill = wall, width = 1)