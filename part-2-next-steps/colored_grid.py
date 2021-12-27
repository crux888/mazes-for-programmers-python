from grid import Grid


class ColoredGrid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None
        self.maximum = 0

    def background_color_for(self, cell):
        if self.distances is not None and self.distances[cell] is not None:
            if self.maximum == 0:
                farthest, self.maximum = self.distances.max()
            distance = self.distances[cell]
            intensity = float((self.maximum - distance)) / self.maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            return dark, bright, dark #green
            #return dark, dark, bright #blue
            #return bright, dark, bright #purple
            #return bright, bright, dark #greenish
            #return dark, bright, bright #teal
            #return bright, dark, dark #red
            #return bright, bright, bright #grey
        else:
            return None