from cell import Cell
from random import randrange
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

    def __getitem__(self, key):  # : Key):
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
                # CHAPTER 3 ADDITION
                # {contents_of(cell)} "
                body = " " + self.contents_of(cell) + " "
                # body = "   "
                # CHAPTER 3 ADDITION
                east_boundary = " " if cell.linked_to(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.linked_to(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        print(output)

    def to_png(self, cell_size: int = 10):
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        background = (255, 255, 255)
        wall = (0, 0, 0)
        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)
        for mode in range(2):
            for cell in self.each_cell():
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size
                if mode == DRAW_BACKGROUND:
                    color = self.background_color_for(cell)
                    draw.rectangle((x1, y1, x2, y2), fill=color)
                else:
                    if not cell.north:
                        draw.line([x1, y1, x2, y1], wall, 1, None)
                    if not cell.west:
                        draw.line([x1, y1, x1, y2], wall, 1, None)
                    if not cell.linked_to(cell.east):
                        draw.line([x2, y1, x2, y2], wall, 1, None)
                    if not cell.linked_to(cell.south):
                        draw.line([x1, y2, x2, y2], wall, 1, None)
        img.show()

    def deadends(self):
        return [cell for cell in self.each_cell() if len(cell.links) == 1]
