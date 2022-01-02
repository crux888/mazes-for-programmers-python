from grid import Grid
from cell import Cell
from PIL import Image, ImageDraw
import random

DRAW_BACKGROUND = 0


class CubeCell(Cell):

    def __init__(self, face, row, column):
        self.face = face
        super().__init__(row, column)


class CubeGrid(Grid):

    def __init__(self, dim):
        super().__init__(dim, dim)

    def prepare_grid(self):
        return [[[CubeCell(face, row, column) for column in range(self.columns)] for row in range(self.rows)] for face in range(6)]

    def each_face(self): 
        for face in range(6):
            yield self.grid[face]

    def each_row(self):
        for face in self.each_face():
            for row in face:
                if row is not None:
                    yield row

    def random_cell(self):
        face   = random.randrange(6)
        row    = random.randrange(self.rows)
        column = random.randrange(self.columns)
        return self[face, row, column]

    def size(self):
        return 6 * self.rows * self.columns

    def configure_cells(self):
        for cell in self.each_cell():
            face   = cell.face
            row    = cell.row
            column = cell.column
            cell.west  = self[face, row, column - 1]
            cell.east  = self[face, row, column + 1]
            cell.north = self[face, row - 1, column]
            cell.south = self[face, row + 1, column]

    def __getitem__(self, key):
        face, row, column = key
        if face < 0 or face >= 6:
            return None
        else:
            face, row, column = self.wrap(face, row, column)
            return self.grid[face][row][column]

    def wrap(self, face, row, column):
        n = self.columns - 1

        if row < 0:
            if face == 0: return [4, column, 0]
            if face == 1: return [4, n, column]
            if face == 2: return [4, n - column, n]
            if face == 3: return [4, 0, n - column]
            if face == 4: return [3, 0, n - column]
            if face == 5: return [1, n, column]
        elif row >= self.rows:
            if face == 0: return [5, n - column, 0]
            if face == 1: return [5, 0, column]
            if face == 2: return [5, column, n]
            if face == 3: return [5, n, n - column]
            if face == 4: return [1, 0, column]
            if face == 5: return [3, n, n - column]
        elif column < 0:
            if face == 0: return [3, row, n]
            if face == 1: return [0, row, n]
            if face == 2: return [1, row, n]
            if face == 3: return [2, row, n]
            if face == 4: return [0, 0, row]
            if face == 5: return [0, n, n - row]
        elif column >= self.columns:
           if face == 0: return [1, row, 0]
           if face == 1: return [2, row, 0]
           if face == 2: return [3, row, 0]
           if face == 3: return [0, row, 0]
           if face == 4: return [2, 0, n - row]
           if face == 5: return [2, n, row]
        return [face, row, column]

    def to_png(self, cell_size = 10, inset = 0):
        inset = int(cell_size * inset)
        
        face_width  = cell_size * self.columns
        face_height = cell_size * self.rows

        img_width   = 4 * face_width
        img_height  = 3 * face_height

        offsets = [[0, 1], [1, 1], [2, 1], [3, 1], [1, 0], [1, 2]]
        
        background = (255, 255, 255)
        wall = (0, 0, 0)
        outline = (220, 220, 220)

        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)

        self.draw_outlines(draw, face_width, face_height, outline)

        for mode in range(2):
            for cell in self.each_cell():
                x = offsets[cell.face][0] * face_width  + cell.column * cell_size
                y = offsets[cell.face][1] * face_height + cell.row    * cell_size
                
                if inset > 0:
                    self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

        img.show()

    def draw_outlines(self, draw, width, height, outline):
        # face #0
        draw.rectangle([0, height, width, height * 2], outline = outline, fill = (None), width = 1)

        # faces #2 and 3
        draw.rectangle([width * 2, height, width * 4, height * 2], outline = outline, fill = None, width = 1)
        # line between faces #2 and #3
        draw.line([width * 3, height, width * 3, height * 2], fill = outline, width = 1)

        # face #4
        draw.rectangle([width, 0, width * 2, height], outline = outline, fill = None, width = 1)

        # face #5
        draw.rectangle([width, height * 2, width * 2, height * 3], outline = outline, fill = None, width = 1)
        
    def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y):
        x1 = x 
        y1 = y 
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        if mode == DRAW_BACKGROUND:
            color = self.background_color_for(cell)
            if color:
                draw.rectangle([x1, y1, x2, y2], fill = color)
        else:
            if cell.north.face != cell.face and not cell.north:
                draw.line([x1, y1, x2, y1], fill = wall, width = 1)
            if cell.west.face != cell.face and not cell.west:
                draw.line([x1, y1, x1, y2], fill = wall, width = 1)
            if not cell.linked_to(cell.east):
                draw.line([x2, y1, x2, y2], fill = wall, width = 1)
            if not cell.linked_to(cell.south):
                draw.line([x1, y2, x2, y2], fill = wall, width = 1)

