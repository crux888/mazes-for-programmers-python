class AldousBroder:
    
    def on(self, grid):
        cell = grid.random_cell()
        unvisited = grid.size() - 1
        while unvisited > 0:
            neighbor = cell.random_neighbour()
            if len(neighbor.links) == 0:
                cell.link(neighbor)
                unvisited -= 1
            cell = neighbor        