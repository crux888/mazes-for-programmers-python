class Distances:
    
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0
        
    def __getitem__(self, cell):
        if cell in self.cells.keys():
            return self.cells[cell]
        return None
        
    def __setitem__(self, cell, distance):
        self.cells[cell] = distance
        
    def cells(self):
        return cells.keys
        # return list(self._cells.keys())
        
    def path_to(self, goal):
        current = goal
        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]
        while current != self.root:
            for neighbor in current.links:
                if neighbor == self.root:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break
                elif self.cells[neighbor] < self.cells[current]:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break
        return breadcrumbs
        
    def max(self):
        max_distance = 0
        max_cell = self.root
        for cell in self.cells:
            if self.cells[cell] > max_distance:
                max_cell = cell
                max_distance = self.cells[cell]
        return max_cell, max_distance