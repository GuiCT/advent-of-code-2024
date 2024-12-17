from typing import NamedTuple
import numpy as np

Point = NamedTuple("Point", [("x", int), ("y", int)])
Point.__add__ = lambda self, other: Point(self.x + other.x, self.y + other.y)
Point.__sub__ = lambda self, other: Point(self.x - other.x, self.y - other.y)
Point.__mul__ = lambda self, scalar: Point(self.x * scalar, self.y * scalar)
Point.__rmul__ = lambda self, scalar: self * scalar
Point.__mod__ = lambda self, other: Point(self.x % other.x, self.y % other.y)


class Grid:
    def __init__(self, array: np.ndarray):
        self.array = array

    def get(self, point: Point, default=None):
        max_x, max_y = self.array.shape
        x_within = 0 <= point.x < max_x
        y_within = 0 <= point.y < max_y
        within = x_within and y_within
        if not within:
            return default
        return self.array[point.x, point.y]

    def get_from_complex(self, idx: complex, default=None):
        return self.get(int(idx.real), int(idx.imag), default)
