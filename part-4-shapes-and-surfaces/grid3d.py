from cell import Cell
from colored_grid import ColoredGrid
from PIL import Image, ImageDraw
import random

DRAW_BACKGROUND = 0
DRAW_WALLS      = 1


class Cell3D(Cell):

    def __init__(self, level, row, column):
        self.level = level
        super().__init__(row, column)

    def neighbors(self):
        list = super().neighbors()
        if self.up:
            list.append(self.up)
        if self.down:
            list.append(self.down)
        return list


class Grid3D(ColoredGrid):
    
    def __init__(self, levels, rows, columns):
        self.levels = levels
        super().__init__(rows, columns)

    def prepare_grid(self):
        return [[[Cell3D(level, row, column) for column in range(self.columns)] for row in range(self.rows)] for level in range(self.levels)]

    def configure_cells(self):
        for cell in self.each_cell():
            level = cell.level
            row = cell.row
            column = cell.column
            cell.north = self[level, row - 1, column]
            cell.south = self[level, row + 1, column]
            cell.east  = self[level, row, column + 1]
            cell.west  = self[level, row, column - 1]
            cell.down  = self[level - 1, row, column]
            cell.up    = self[level + 1, row, column]

    def __getitem__(self, key):
        level, row, column = key
        if level < 0 or level > self.levels - 1:
            return None
        if row < 0 or row > self.rows - 1:
            return None
        if column < 0 or column > self.columns - 1:
            return None
        return self.grid[level][row][column]

    def random_cell(self):
        level  = random.randrange(self.levels)
        row    = random.randrange(len(self.grid[level]))
        column = random.randrange(len(self.grid[level][row]))
        return self[level, row, column]

    def size(self):
        return self.levels * self.rows * self.columns

    def each_level(self):
        for level in range(self.levels):
            yield self.grid[level]

    def each_row(self):
        for level in self.each_level():
            for row in level:
                if row is not None:
                    yield row

    def to_png(self, cell_size = 10, inset = 0, margin = 0):
        if margin == 0:
            margin = cell_size // 2
        
        grid_width  = cell_size * self.columns
        grid_height = cell_size * self.rows

        img_width   = grid_width * self.levels + (self.levels - 1) * margin
        img_height  = grid_height
        
        background = (255, 255, 255)
        wall = (0, 0, 0)
        arrow = (255, 0, 0)

        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)

        for mode in range(2):
            for cell in self.each_cell():
                x = cell.level * (grid_width + margin) + cell.column * cell_size
                y = cell.row * cell_size
                if inset > 0:
                    self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

                if mode == DRAW_WALLS:
                    mid_x = x + cell_size // 2
                    mid_y = y + cell_size // 2

                    # Original code to draw red arrows (but no scaling as cell_size increases)
                    # if cell.linked_to(cell.down):
                    #     draw.line([mid_x - 3, mid_y, mid_x - 1, mid_y + 2], fill = arrow, width = 1)
                    #     draw.line([mid_x - 3, mid_y, mid_x - 1, mid_y - 2], fill = arrow, width = 1)
                    #
                    # if cell.linked_to(cell.up):
                    #     draw.line([mid_x + 3, mid_y, mid_x + 1, mid_y + 2], fill = arrow, width = 1)
                    #     draw.line([mid_x + 3, mid_y, mid_x + 1, mid_y - 2], fill = arrow, width = 1)

                    # Modified code to draw red arrows (with scaling as cell_size increases)
                    arrow_adj = cell_size // 10
                    if arrow_adj < 1:
                        arrow_adj = 1
                    if cell.linked_to(cell.down):
                        draw.line([mid_x - (arrow_adj*3), mid_y, mid_x - (arrow_adj*1), mid_y + (arrow_adj*2)], fill = arrow, width = 1)
                        draw.line([mid_x - (arrow_adj*3), mid_y, mid_x - (arrow_adj*1), mid_y - (arrow_adj*2)], fill = arrow, width = 1)
                    if cell.linked_to(cell.up):
                        draw.line([mid_x + (arrow_adj*3), mid_y, mid_x + (arrow_adj*1), mid_y + (arrow_adj*2)], fill = arrow, width = 1)
                        draw.line([mid_x + (arrow_adj*3), mid_y, mid_x + (arrow_adj*1), mid_y - (arrow_adj*2)], fill = arrow, width = 1)

        img.show()