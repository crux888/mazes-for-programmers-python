from grid import Grid
from random import choice, randint


class Sidewinder:

    def on(self, grid: Grid):
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                
                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None
                                                
                should_close_out = at_eastern_boundary or (not at_northern_boundary and randint(0, 1) == 0)
                
                if should_close_out:
                    member = choice(run)
                    if member.north:
                        member.link(member.north)
                    run.clear()
                else:
                    cell.link(cell.east)
                
                
