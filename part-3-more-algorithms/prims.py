import random


class SimplifiedPrims:

    def on(self, grid, start_at = None):
        active = []
        if start_at is None:
            active.append(grid.random_cell())
        else:
            active.append(start_at)

        while active:
            cell = random.choice(active)
            available_neighbors = [neighbor for neighbor in cell.neighbors() if not neighbor.links]
            if available_neighbors:
                neighbor = random.choice(available_neighbors)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)

        return grid


class TruePrims:

    def on(self, grid, start_at = None):
        active = []
        if start_at is None:
            active.append(grid.random_cell())
        else:
            active.append(start_at)

        costs = {}
        for cell in grid.each_cell():
            costs[cell] = random.randrange(100)

        while active:
            cell = min(active, key=costs.get)
            available_neighbors = [neighbor for neighbor in cell.neighbors() if not neighbor.links]
            if available_neighbors:
                neighbor = min(available_neighbors, key=costs.get)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)

        return grid