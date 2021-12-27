from cell import Cell


class TriangleCell(Cell):

    def upright(self):
        if (self.row + self.column) % 2 == 0:
            return True
        else:
            return False

    def neighbors(self):
        list=[]
        if self.west:
            list.append(self.west)
        if self.east:
            list.append(self.east)
        if not self.upright() and self.north:
            list.append(self.north)
        if self.upright() and self.south:
            list.append(self.south)
        return list