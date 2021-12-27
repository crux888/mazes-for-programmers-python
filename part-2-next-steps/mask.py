from random import randrange
from PIL import Image


class Mask:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.bits = [[True for _ in range(self.columns)] for _ in range(self.rows)]
        
    def __getitem__(self, key):
        row, column = key
        if 0 <= row <= self.rows - 1 and 0 <= column <= self.columns - 1:
            return self.bits[row][column]
        else:
            return False

    def __setitem__(self, key, is_on):
        row, column = key
        self.bits[row][column] = is_on

    def count(self):
        count = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.bits[row][column]:
                    count += 1
        return count

    def random_location(self):
        while True:
            row = randrange(0, self.rows)
            column = randrange(0, self.columns)
            if self.bits[row][column]:
                return (row, column)

    def from_txt(filename):
        with open(filename) as file:
            lines = [line.strip() for line in file ]
        file.close()
        while len(lines[-1]) < 1:
            lines.pop()
        rows = len(lines)
        columns = len(lines[0])
        mask = Mask(rows, columns)
        for row in range(rows):
            for column in range(columns):
                if lines[row][column] == "X":
                    mask[row, column] = False
                else:
                    mask[row, column] = True
        return mask

    def from_png(filename):
        image = Image.open(filename)
        rows = image.height
        columns = image.width
        mask = Mask(rows, columns)
        for row in range(rows):
            for column in range(columns):
                if image.getpixel((column, row)) == (0, 0, 0, 255): # RGB value for black
                    mask[row, column] = False
                else:
                    mask[row, column] = True
        return mask