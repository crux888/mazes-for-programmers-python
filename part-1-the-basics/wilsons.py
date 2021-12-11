from random import choice


class Wilsons:

    def on(self, grid):
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        first = choice(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            cell = choice(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = cell.random_neighbour()
                try:
                    position = path.index(cell)
                    path = path[:position + 1]
                except ValueError:
                    path.append(cell)

            for index in range(len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])