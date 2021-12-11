from distances import Distances
from random import choice


class Cell:
 
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self._links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True):
        self._links[cell] = True
        if (bidi):
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi=True):
        del self._links[cell]
        if (bidi):
            cell.unlink(self, False)
        return self

    @property
    def links(self):
        return list(self._links.keys())

    def linked_to(self, cell):
        return cell in self._links

    def neighbors(self):
        list=[]
        if self.north:
            list.append(self.north)
        if self.south:
            list.append(self.south)
        if self.east:
            list.append(self.east)
        if self.west:
            list.append(self.west)
        return list
        
    def random_neighbour(self):
        if len(self.neighbors()) == 0:
            return None
        else:
            return choice(self.neighbors())
        
    #CHAPTER 3 ADDITION
    def distances(self):
        distances = Distances(self)
        frontier = [self]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links:
                    if distances[linked_cell] is None and distances[cell] is not None:
                        distances[linked_cell] = distances[cell] + 1
                        new_frontier.append(linked_cell)
            frontier = new_frontier
        return distances