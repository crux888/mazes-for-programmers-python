import random


class Kruskals:

    class State:

        def __init__(self, grid):
            self.grid = grid
            self.neighbors = []
            self.set_for_cell = {}
            self.cells_in_set = {}
            for cell in self.grid.each_cell():
                cell_set = len(self.set_for_cell)
                self.set_for_cell[cell]     = cell_set 
                self.cells_in_set[cell_set] = [cell]
                if cell.south:
                    self.neighbors.append([cell, cell.south])
                if cell.east:
                    self. neighbors.append([cell, cell.east])

        def can_merge(self, left, right):
            # This will cause a KeyError for undercells that are not in the list
            # return self.set_for_cell[left] != self.set_for_cell[right
            #   loser_set   = self.set_for_cell[right] 
            # Instead, use .get method which returns "None" if key is not in dictionary
            return self.set_for_cell.get(left) != self.set_for_cell.get(right)

        def merge(self, left, right):
            left.link(right)
            # These will cause a KeyError for undercells that are not in the list...
            #   winner_set  = self.set_for_cell[left]  
            #   loser_set   = self.set_for_cell[right] 
            # Instead, use .get method to avoid KeyError and then test for "None"
            winner_set = self.set_for_cell.get(left)
            loser_set = self.set_for_cell.get(right)
            if loser_set is None:
                loser_cells = [right]
            else:
                loser_cells = self.cells_in_set[loser_set]
            for cell in loser_cells:
                self.cells_in_set[winner_set].append([cell][0])
                self.set_for_cell[cell] = winner_set
            if loser_set is not None:
                del self.cells_in_set[loser_set]

        def add_crossing(self, cell):
            if (len(cell.links) > 0 or
                self.can_merge(cell.east, cell.west) == False or 
                self.can_merge(cell.north, cell.south) == False):                
                    return False
            for neighbor in list(self.neighbors):    # Iterate through a copy of the list...
                left, right = neighbor
                if left == cell or right == cell:
                    self.neighbors.remove(neighbor)  # ...while deleting from the original list
            if random.randrange(2) == 0: # Horizontal crossing
                self.merge(cell.west, cell)
                self.merge(cell, cell.east)
                self.grid.tunnel_under(cell)
                self.merge(cell.north, cell.north.south)
                self.merge(cell.south, cell.south.north)
            else:                        # Vertical crossing
                self.merge(cell.north, cell)
                self.merge(cell, cell.south)
                self.grid.tunnel_under(cell)
                self.merge(cell.west, cell.west.east)
                self.merge(cell.east, cell.east.west) 

    def on(self, grid, state = None):
        if state == None:
            state = self.State(grid)
        neighbors = state.neighbors
        random.shuffle(neighbors)
        while neighbors:
            left, right = neighbors.pop()
            if state.can_merge(left, right):
                state.merge(left, right)
        return grid