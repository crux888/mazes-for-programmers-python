from grid import Grid


class DistanceGrid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None

    def contents_of(self, cell):
        if self.distances is not None and self.distances[cell] is not None:
            return (str_base(self.distances[cell], 36))
        else:
            return super().contents_of(cell)


# Additional code to format cell distance as base 36
# (from https://stackoverflow.com/questions/2063425)

def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    else:
        (d, m) = divmod(number, base)
        if d:
            return str_base(d, base) + digit_to_char(m)
        else:
            return digit_to_char(m)


def digit_to_char(digit):
    if digit < 10:
        return chr(ord('0') + digit)
    else:
        return chr(ord('a') + digit - 10)
