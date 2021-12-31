import random

class Ellers:

    class RowState:

        def __init__(self, columns = 0, starting_set = 0):
            self.cells_in_set = {}
            self.set_for_cell = [None] * columns
            # Ruby allows you to add an item to a list using an index that doesn't exist
            # (and then inserts Nil values for any missing items in that list)... Python
            # doesn't work like this approach, so we need to make sure the set_for_cell 
            # list is initialised with [None] * grid.columns
            self.next_set = starting_set

        def record(self, cell_set, cell):
            self.set_for_cell[cell.column] = cell_set
            if not cell_set in self.cells_in_set:
                self.cells_in_set[cell_set] = []
            self.cells_in_set[cell_set].append(cell)

        def set_for(self, cell):
            if self.set_for_cell[cell.column] is None:
                self.record(self.next_set, cell)
                self.next_set += 1
            return self.set_for_cell[cell.column]

        def merge(self, winner_set, loser_set):
            for cell in self.cells_in_set[loser_set]:
                self.set_for_cell[cell.column] = winner_set
                self.cells_in_set[winner_set].append(cell)
            if loser_set in self.cells_in_set:
                del self.cells_in_set[loser_set]

        def each_set(self):
            return [_ for _ in self.cells_in_set.items()]


    def on(self, grid):
        row_state = self.RowState(columns = grid.columns)
        # See __init__ comment re: needing to add the "columns" parameter

        for row in grid.each_row():
            for cell in row:
                if cell.west:
                    cell_set = row_state.set_for(cell)
                    prior_cell_set = row_state.set_for(cell.west)

                    should_link = cell_set != prior_cell_set and (cell.south is None or random.randrange(2) == 0)
                    
                    if should_link:
                        cell.link(cell.west)
                        row_state.merge(prior_cell_set, cell_set)

            if row[0].south:
                next_row = self.RowState(columns = grid.columns, starting_set = row_state.next_set) 
                # See __init__ comment re: needing to add the "columns" parameter
                
                for cell_set, list_of_cells in row_state.each_set():
                    random.shuffle(list_of_cells)
                    index = 0
                    for cell in list_of_cells:
                        if index == 0 or random.randrange(3) == 0:
                            cell.link(cell.south)
                            next_row.record(row_state.set_for(cell), cell.south)
                        index += 1

                row_state = next_row