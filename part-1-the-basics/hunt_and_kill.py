from random import choice


class HuntAndKill:

    def on(self, grid):
        current_cell = grid.random_cell()
        while current_cell is not None:
            unvisited_neighbors = [neighbor for neighbor in current_cell.neighbors() if len(neighbor.links) == 0]
            if len(unvisited_neighbors) > 0:
                neighbor = choice(unvisited_neighbors)
                current_cell.link(neighbor)
                current_cell = neighbor
            else:
                current_cell = None
                for cell in grid.each_cell():
                    visited_neighbors = [neighbor for neighbor in cell.neighbors() if len(neighbor.links) > 0]
                    if len(cell.links) == 0 and len(visited_neighbors) > 0:
                        current_cell = cell
                        neighbor = choice(visited_neighbors)
                        current_cell.link(neighbor)
                        break