from colored_grid import ColoredGrid
from triangle_cell import TriangleCell
from PIL import Image, ImageDraw
import math

DRAW_BACKGROUND = 0


class TriangleGrid(ColoredGrid):

    def prepare_grid(self):
        return [[TriangleCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            column = cell.column
            cell.west = self[row, column - 1]
            cell.east = self[row, column + 1]
            if cell.upright():
                cell.south = self[row + 1, column]
            else:
                cell.north = self[row - 1, column]

    def to_png(self, size: int = 16):
        half_width = size / 2.0
        height = size * math.sqrt(3) / 2.0
        half_height = height / 2.0
        img_width = int(size * (self.columns + 1) / 2.0)
        img_height = int(height * self.rows)
        background = (255, 255, 255)
        wall = (0, 0, 0)
        wall_width = 2
        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)
        for mode in range(2):
            for cell in self.each_cell():
                cx = half_width + cell.column * half_width
                cy = half_height + cell.row * height 
                west_x = int(cx - half_width)
                mid_x  = int(cx)
                east_x = int(cx + half_width)
                if cell.upright():
                    apex_y = int(cy - half_height)
                    base_y = int(cy + half_height)
                else:
                    apex_y = int(cy + half_height)
                    base_y = int(cy - half_height)
                if mode == DRAW_BACKGROUND:
                    color = self.background_color_for(cell)
                    if color:
                        draw.polygon([(west_x, base_y), (mid_x, apex_y), (east_x, base_y)], fill=color, outline = None)
                else:
                    if not cell.west:
                        draw.line([west_x, base_y, mid_x, apex_y], fill = wall, width = wall_width)
                    if not cell.linked_to(cell.east):
                        draw.line([east_x, base_y, mid_x, apex_y], fill = wall, width = wall_width)
                    no_south = cell.upright() is True and cell.south is None
                    not_linked = cell.upright() is False and cell.linked_to(cell.north) is False
                    if no_south or not_linked:
                        draw.line([east_x, base_y, west_x, base_y], fill = wall, width = wall_width)                
        img.show()