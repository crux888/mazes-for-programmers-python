from random import choice


class RecursiveBacktracker:

    def on(self, grid, start_at = None):
        stack = []
        if start_at is None:
            stack.append(grid.random_cell())
        else:
            stack.append(start_at)

        while stack:
            current_cell = stack[-1]
            unvisited_neighbors = [neighbor for neighbor in current_cell.neighbors() if not neighbor.links]
            if not unvisited_neighbors:
                stack.pop()
            else:
                neighbor = choice(unvisited_neighbors)
                current_cell.link(neighbor)
                stack.append(neighbor)