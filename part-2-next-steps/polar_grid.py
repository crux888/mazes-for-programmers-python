from colored_grid import ColoredGrid
from polar_cell import PolarCell
from random import randrange
from PIL import Image, ImageDraw
import math

DRAW_BACKGROUND = 0


class PolarGrid(ColoredGrid):

    def __init__(self, rows):
        super().__init__(rows, 1)

    def prepare_grid(self):
        rows = [None for _ in range(self.rows)]
        row_height = 1.0 / self.rows
        rows[0] = [PolarCell(0, 0)]
        for row in range(1, self.rows):
            radius = float(row) / self.rows
            circumference = 2 * math.pi * radius 
            previous_count = len(rows[row - 1])
            estimated_cell_width = circumference / previous_count
            ratio = round(estimated_cell_width / row_height)
            cells = previous_count * ratio
            rows[row] = [PolarCell(row, column) for column in range(cells)]
        return rows

    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            column = cell.column
            if row > 0:
                cell.cw = self[row, column + 1]
                cell.ccw = self[row, column - 1]
                ratio = len(self.grid[row]) / len(self.grid[row - 1])
                parent = self.grid[row - 1][int(column / ratio)]
                parent.outward = cell
                cell.inward = parent 
                
    def __getitem__(self, key):
        row, column = key
        if row < 0 or row > self.rows - 1:
            return None
        return self.grid[row][column % len(self.grid[row])]

    def random_cell(self):
        row = randrange(0, self.rows)
        column = randrange(0, len(self.grid[row]))
        return self.grid[row][column]

    def to_png(self, cell_size: int = 10):
        img_size = 2 * self.rows * cell_size
        background = (255, 255, 255)
        wall = (0, 0, 0)
        wall_width = 1
        img = Image.new("RGBA", (img_size + 1, img_size + 1), background)
        draw = ImageDraw.Draw(img)
        center = img_size / 2
        for mode in range(2):
            for cell in self.each_cell():
                if cell.row != 0:
                    theta = 2 * math.pi / len(self.grid[cell.row])
                    inner_radius = cell.row * cell_size
                    outer_radius = (cell.row + 1) * cell_size
                    theta_ccw    = cell.column * theta
                    theta_cw     = (cell.column + 1) * theta
                    ax = int(center + (inner_radius * math.cos(theta_ccw)))
                    ay = int(center + (inner_radius * math.sin(theta_ccw)))
                    bx = int(center + (outer_radius * math.cos(theta_ccw)))
                    by = int(center + (outer_radius * math.sin(theta_ccw)))
                    cx = int(center + (inner_radius * math.cos(theta_cw)))
                    cy = int(center + (inner_radius * math.sin(theta_cw)))
                    dx = int(center + (outer_radius * math.cos(theta_cw)))
                    dy = int(center + (outer_radius * math.sin(theta_cw)))
                    if mode == DRAW_BACKGROUND:
                        color = self.background_color_for(cell)
                        draw.polygon([(ax, ay), (cx, cy), (dx, dy), (bx, by)],
                                      fill = color, outline = color)
                    else:
                        if not cell.linked_to(cell.inward):
                            draw.line([ax, ay, cx, cy], fill = wall, width = wall_width)
                        if not cell.linked_to(cell.cw):
                            draw.line([cx, cy, dx, dy], fill = wall, width = wall_width)
        draw.ellipse([0, 0, img_size, img_size], outline = wall, fill = None, width = wall_width)
        img.show()