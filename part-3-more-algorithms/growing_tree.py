import random


class GrowingTree:

    def on(self, grid, start_at = None, block = None):
        active = []
        if start_at is None:
            active.append(grid.random_cell())
        else:
            active.append(start_at)

        while active:
            if block:
                cell = block(active)
            else:
                cell = random.choice(active)

            available_neighbors = [neighbor for neighbor in cell.neighbors() if not neighbor.links]
            if available_neighbors:
                neighbor = random.choice(available_neighbors)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)

        return grid