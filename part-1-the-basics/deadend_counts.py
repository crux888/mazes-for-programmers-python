from grid import Grid
from binary_tree import BinaryTree
from sidewinder import Sidewinder
from aldous_broder import AldousBroder
from wilsons import Wilsons
from hunt_and_kill import HuntAndKill
from recursive_backtracker import RecursiveBacktracker

ALGORITHMS = [BinaryTree, Sidewinder, AldousBroder, Wilsons, HuntAndKill, RecursiveBacktracker]

tries = 10
size = 20

averages = {}

for algorithm in ALGORITHMS:
    print("Running {}...".format(algorithm.__name__))
    deadend_counts = []
    for _ in range(tries):
        grid = Grid(size, size)
        algorithm().on(grid)
        deadend_counts.append(len(grid.deadends()))
    total_deadends = sum(deadend_counts)
    averages[algorithm] = total_deadends / len(deadend_counts)

total_cells = size * size
print("Average dead-ends per {}x{} maze ({} cells):".format(size, size, total_cells))

sorted_averages = sorted(averages.items(), key=lambda x: -x[1])
for algorithm, average in sorted_averages:
    percentage = average * 100.0 / total_cells
    print(" {:>20}: {:>3.0f}/{:>3d} ({:.0f}%)".format(algorithm.__name__, average, total_cells, percentage))