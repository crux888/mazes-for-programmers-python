from cell import Cell
import random
from random import randrange
#from random import randrange, random, shuffle
from PIL import Image, ImageDraw

DRAW_BACKGROUND = 0


class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        return [[Cell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            column = cell.column
            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.east = self[row, column + 1]
            cell.west = self[row, column - 1]

    def __getitem__(self, key):
        row, column = key
        if row < 0 or row > self.rows - 1:
            return None
        if column < 0 or column > self.columns - 1:
            return None
        return self.grid[row][column]

    def random_cell(self):
        row = randrange(0, self.rows)
        column = randrange(0, self.columns)
        return self[row, column]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in range(self.rows):
            yield self.grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if cell is not None:
                    yield cell 

    def cell_at(self, row, column):
        if not (0 <= row < self.rows):
            return None
        if not (0 <= column < self.columns):
            return None
        return self._grid[row][column]

    def contents_of(self, cell):
        return " "

    def background_color_for(self, cell):
        return None

    def to_s(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                if cell is None:
                    # Cell was not substantiated (see masked_grid.py)
                    linked_to_east_cell = False
                    linked_to_south_cell = False
                else:
                    linked_to_east_cell = cell.linked_to(cell.east)
                    linked_to_south_cell = cell.linked_to(cell.south)
                # CHAPTER 3 ADDITION
                # {contents_of(cell)} "
                body = " " + self.contents_of(cell) + " "
                # body = "   "
                # CHAPTER 3 ADDITION
                #east_boundary = " " if cell.linked_to(cell.east) else "|"
                east_boundary = " " if linked_to_east_cell else "|"
                top += body + east_boundary
                south_boundary = "   " if linked_to_south_cell else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        print(output)

    def to_png(self, cell_size: int = 10, inset = 0):
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        inset = int(cell_size * inset)
        background = (255, 255, 255)
        wall = (0, 0, 0)
        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)
        for mode in range(2):
            for cell in self.each_cell():
                x = cell.column * cell_size
                y = cell.row * cell_size
                if inset > 0:
                    self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)
        img.show()

    def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y):
        x1 = x 
        y1 = y 
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        if mode == DRAW_BACKGROUND:
            color = self.background_color_for(cell)
            draw.rectangle((x1, y1, x2, y2), fill = color)
        else:
            if not cell.north:
                draw.line([x1, y1, x2, y1], fill = wall, width = 1)
            if not cell.west:
                draw.line([x1, y1, x1, y2], fill = wall, width = 1)
            if not cell.linked_to(cell.east):
                draw.line([x2, y1, x2, y2], fill = wall, width = 1)
            if not cell.linked_to(cell.south):
                draw.line([x1, y2, x2, y2], fill = wall, width = 1)
        
    def to_png_with_inset(self, draw, cell, mode, cell_size, wall, x, y, inset):
        x1, x2, x3, x4, y1, y2, y3, y4 = self.cell_coordinates_with_inset(x, y, cell_size, inset)
        if mode == DRAW_BACKGROUND:
            color = self.background_color_for(cell)
            draw.rectangle((x2, y2, x3, y3), fill = color)
            if cell.linked_to(cell.north):
                draw.rectangle((x2, y1, x3, y2), fill = color)
            if cell.linked_to(cell.south):
                draw.rectangle((x2, y3, x3, y4), fill = color)
            if cell.linked_to(cell.west):
                draw.rectangle((x1, y2, x2, y3), fill = color)
            if cell.linked_to(cell.east):
                draw.rectangle((x3, y2, x4, y3), fill = color)
        else:
            if cell.linked_to(cell.north):
                draw.line([x2, y1, x2, y2], fill = wall, width = 1)
                draw.line([x3, y1, x3, y2], fill = wall, width = 1)
            else:
                draw.line([x2, y2, x3, y2], fill = wall, width = 1)
            if cell.linked_to(cell.south):
                draw.line([x2, y3, x2, y4], fill = wall, width = 1)
                draw.line([x3, y3, x3, y4], fill = wall, width = 1)
            else:
                draw.line([x2, y3, x3, y3], fill = wall, width = 1)
            if cell.linked_to(cell.west):
                draw.line([x1, y2, x2, y2], fill = wall, width = 1)
                draw.line([x1, y3, x2, y3], fill = wall, width = 1)
            else:
                draw.line([x2, y2, x2, y3], fill = wall, width = 1)
            if cell.linked_to(cell.east):
                draw.line([x3, y2, x4, y2], fill = wall, width = 1)
                draw.line([x3, y3, x4, y3], fill = wall, width = 1)
            else:
                draw.line([x3, y2, x3, y3], fill = wall, width = 1)

    def cell_coordinates_with_inset(self, x, y, cell_size, inset):
        x1 = x
        x4 = x + cell_size
        x2 = x1 + inset
        x3 = x4 - inset 
        y1 = y 
        y4 = y + cell_size
        y2 = y1 + inset 
        y3 = y4 - inset 
        return x1, x2, x3, x4, y1, y2, y3, y4

    def deadends(self):
        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def braid(self, p = 1.0):
        cells = self.deadends()
        random.shuffle(cells)
        for cell in cells:
            if len(cell.links) is 1 and random.random() < p:
                neighbors = [neighbor for neighbor in cell.neighbors() if cell.linked_to(neighbor) is False]
                best = [neighbor for neighbor in neighbors if len(neighbor.links) is 1]
                if not best:
                    best = neighbors
                neighbor = random.choice(best)
                cell.link(neighbor)