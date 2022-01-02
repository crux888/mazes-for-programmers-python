from grid import Grid
from cell import Cell #??
from polar_grid import PolarGrid
from polar_cell import PolarCell
import math
import random
from PIL import Image, ImageDraw


class HemisphereCell(PolarCell):

    def __init__(self, hemisphere, row, column):
        self.hemisphere = hemisphere
        super().__init__(row, column)


class HemisphereGrid(PolarGrid):

    def __init__(self, hemisphere_id, rows):
        self.hemisphere_id = hemisphere_id
        super().__init__(rows)

    def size(self, row):
        return len(self.grid[row])

    def prepare_grid(self):
        grid = [None for _ in range(self.rows)]

        angular_height = math.pi / (2 * self.rows)

        grid[0] = [ HemisphereCell(self.hemisphere_id, 0, 0) ]

        for row in range(1, self.rows):
            theta = (row + 1) * angular_height
            radius = math.sin(theta)
            circumference = 2 * math.pi * radius

            previous_count = len(grid[row - 1])
            estimated_cell_width = circumference / previous_count
            ratio = round(estimated_cell_width / angular_height)

            cells = previous_count * ratio
            grid[row] = [HemisphereCell(self.hemisphere_id, row, col) for col in range(cells)]

        return grid


class SphereGrid(Grid):

    def __init__(self, rows):
        if (rows % 2) != 0:
            raise ValueError("argument must be an even number")
        self.equator = rows // 2
        super().__init__(rows, 1)

    def prepare_grid(self):
        return [HemisphereGrid(hemisphere_id, self.equator) for hemisphere_id in range(2)]

    def configure_cells(self):
        belt = self.equator - 1
        for index in range(self.size(belt)):
            a = self[0, belt, index]
            b = self[1, belt, index]
            #a.outward = b
            #b.outward = a
            a.outward.append(b)   #COMMENT ????????????????
            b.outward.append(a)   #COMMENT ????????????????

    def __getitem__(self, key):
        hemi, row, column = key
        return self.grid[hemi][row, column] # HMMMMMMMMMM.... or [hemi][row, column]

    def size(self, row):
        return self.grid[0].size(row)

    def each_cell(self):
        for hemi in self.grid:
            for cell in hemi.each_cell():
                if cell is not None:
                    yield cell 

    def random_cell(self):
        return self.grid[random.randrange(2)].random_cell()

    def to_png(self, ideal_size = 10):
        img_height = ideal_size * self.rows
        img_width  = self.grid[0].size(self.equator - 1) * ideal_size
        
        background = (255, 255, 255)
        wall = (0, 0, 0)

        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)

        for cell in self.each_cell():
            row_size = self.size(cell.row)
            cell_width = float(img_width) / row_size

            x1 = cell.column * cell_width
            x2 = x1 + cell_width

            y1 = cell.row * ideal_size
            y2 = y1 + ideal_size

            if cell.hemisphere > 0:
                y1 = img_height - y1
                y2 = img_height - y2

            x1 = round(x1)
            y1 = round(y1)
            x2 = round(x2)
            y2 = round(y2)

            if cell.row > 0:
                if not cell.linked_to(cell.cw):
                    draw.line([x2, y1, x2, y2], fill = wall, width = 1)
                if not cell.linked_to(cell.inward):
                    draw.line([x1, y1, x2, y1], fill = wall, width = 1)

            if cell.hemisphere == 0 and cell.row == self.equator - 1:
                if not cell.linked_to(cell.outward[0]):
                    draw.line([x1, y2, x2, y2], fill = wall, width = 1)   

        img.show()