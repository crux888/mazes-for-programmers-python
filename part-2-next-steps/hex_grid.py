from colored_grid import ColoredGrid
from hex_cell import HexCell
from PIL import Image, ImageDraw
import math

DRAW_BACKGROUND = 0


class HexGrid(ColoredGrid):

    def prepare_grid(self):
        return [[HexCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            column = cell.column
            if (column % 2) == 0:
                north_diagonal = row - 1
                south_diagonal = row
            else:
                north_diagonal = row
                south_diagonal = row + 1
            cell.northwest = self[north_diagonal, column - 1]
            cell.north     = self[row - 1, column]
            cell.northeast = self[north_diagonal, column + 1]
            cell.southwest = self[south_diagonal, column - 1]
            cell.south     = self[row + 1, column]
            cell.southeast = self[south_diagonal, column + 1]
 
    def to_png(self, size: int = 10):
        a_size = size / 2.0
        b_size = size * math.sqrt(3) / 2.0
        width  = size * 2
        height = b_size * 2
        img_width = int(3 * a_size * self.columns + a_size + 0.5)
        img_height = int(height * self.rows + b_size + 0.5)
        background = (255, 255, 255)
        wall = (0, 0, 0)
        wall_width = 2
        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)
        for mode in range(2):
            for cell in self.each_cell():
                cx = size + 3 * cell.column * a_size
                cy = b_size + cell.row * height 
                if (cell.column % 2) != 0:
                    cy += b_size
                # f/n = far/near
                # n/s/e/w = north/south/east/west
                x_fw = int(cx - size)
                x_nw = int(cx - a_size)
                x_ne = int(cx + a_size)
                x_fe = int(cx + size)
                # m = middle
                y_n = int(cy - b_size)
                y_m = int(cy)
                y_s = int(cy + b_size)
                if mode == DRAW_BACKGROUND:
                    color = self.background_color_for(cell)
                    if color:
                        draw.polygon([(x_fw, y_m), (x_nw, y_n), (x_ne, y_n), 
                                      (x_fe, y_m), (x_ne, y_s), (x_nw, y_s)], 
                                      fill = color, outline = None)
                else:
                    if not cell.southwest:
                        draw.line([x_fw, y_m, x_nw, y_s], fill = wall, width = wall_width)
                    if not cell.northwest:
                        draw.line([x_fw, y_m, x_nw, y_n], fill = wall, width = wall_width)
                    if not cell.north:
                        draw.line([x_nw, y_n, x_ne, y_n], fill = wall, width = wall_width)
                    if not cell.linked_to(cell.northeast):
                        draw.line([x_ne, y_n, x_fe, y_m], fill = wall, width = wall_width)
                    if not cell.linked_to(cell.southeast):
                        draw.line([x_fe, y_m, x_ne, y_s], fill = wall, width = wall_width)
                    if not cell.linked_to(cell.south):
                        draw.line([x_ne, y_s, x_nw, y_s], fill = wall, width = wall_width)
        img.show()