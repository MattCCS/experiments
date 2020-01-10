
import math
import random


class DynamicGrid:
    """Represents a finite, but growable, 2D grid"""

    def __init__(self):
        self.grid = set()
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def insert(self, coord, value=1):
        (x, y) = coord
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.max_x = max(self.max_x, x + 1)
        self.max_y = max(self.max_y, y + 1)
        self.grid.add(coord)

    def size(self):
        return (self.max_x - self.min_x, self.max_y - self.min_y)

    def __repr__(self):
        rows = []
        for y in range(self.min_y, self.max_y):
            x_range = range(self.min_x, self.max_x)
            rows.append(" ".join("O" if (x, y) in self.grid else "." for x in x_range))
        return f"Grid: {repr(self.size())}" + "\n" + "\n".join(rows)


class GrowingGrid(DynamicGrid):

    def __init__(self, growth_function):
        super().__init__()
        self.insert((0, 0))
        self.growth_function = growth_function

    def grow(self):
        new_coords = self.growth_function(self.grid)
        for coord in new_coords:
            self.insert(coord)

    def simulate(self, iterations):
        for i in range(iterations):
            self.grow()
            print(self)


def around_4(coord):
    (x, y) = coord
    return set([
        (x, y + 1),
        (x, y - 1),
        (x + 1, y),
        (x - 1, y),
    ])


def around_8(coord):
    (x, y) = coord
    return around_4(coord) | set([
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ])


def around_random(coord):
    return set(random.sample(around_8(coord), 4))


def grow_trivial(grid, decider_func):
    new = set()
    for coord in grid:
        new |= decider_func(coord)
    return new - grid


def grow_random_percent(percent=0.50):
    def grow_random_percent_wrapped(grid):
        potential = grow_trivial(grid, around_4)
        return set(random.sample(potential, math.ceil(len(potential) * percent)))
    return grow_random_percent_wrapped


d = DynamicGrid()
print(d)

d.insert((0, 0))
print(d)

d.insert((8, -3))
print(d)


g = GrowingGrid(grow_random_percent(0.25))
print(g)

g.simulate(20)
