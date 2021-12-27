from cell import Cell


class HexCell(Cell):

    def __init__(self, row, column):
        super().__init__(row, column)
        self.northeast = None
        self.northwest = None
        self.southeast = None
        self.southwest = None

    def neighbors(self):
        list=[]
        if self.northwest:
            list.append(self.northwest)
        if self.north:
            list.append(self.north)
        if self.northeast:
            list.append(self.northeast)
        if self.southwest:
            list.append(self.southwest)
        if self.south:
            list.append(self.south)
        if self.southeast:
            list.append(self.southeast)
        return list