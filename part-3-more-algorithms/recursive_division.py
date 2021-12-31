import random


class RecursiveDivision:

    def on(self, grid):
        self.grid = grid
        for cell in self.grid.each_cell():
            for neighbor in cell.neighbors():
                cell.link(neighbor, False)
        self.divide(0, 0, grid.rows, grid.columns)

    def divide(self, row, column, height, width):
        if height > 1 and width > 1:
            if height > width:
                self.divide_horizontally(row, column, height, width)
            else:
                self.divide_vertically(row, column, height, width)

    def divide_horizontally(self, row, column, height, width):
        divide_south_of = random.randrange(height - 1)
        passage_at = random.randrange(width)
        for x in range(width):
            if x != passage_at:
                cell = self.grid[row + divide_south_of, column + x]
                cell.unlink(cell.south)
        self.divide(row, column, divide_south_of + 1, width)
        self.divide(row +  divide_south_of + 1, column, 
            height - divide_south_of -1, width)

    def divide_vertically(self, row, column, height, width):
        divide_east_of = random.randrange(width - 1)
        passage_at = random.randrange(height)
        for y in range(height):
            if y != passage_at:
                cell = self.grid[row + y, column + divide_east_of]
                cell.unlink(cell.east)
        self.divide(row, column, height, divide_east_of + 1)
        self.divide(row, column + divide_east_of + 1,
            height, width - divide_east_of - 1)