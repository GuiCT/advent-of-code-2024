from typing import NamedTuple, Any
import numpy as np


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self: 'Point', other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self: 'Point', other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self: 'Point', scalar) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self: 'Point', scalar) -> 'Point':
        return self * scalar

    def __mod__(self: 'Point', other: 'Point') -> 'Point':
        return Point(self.x % other.x, self.y % other.y)

    def __eq__(self: 'Point', other: 'Point') -> 'Point':
        return self.x == other.x and self.y == other.y

    def to_complex(self: 'Point') -> complex:
        return self.x + self.y * 1j

    @staticmethod
    def from_complex(number: complex) -> 'Point':
        return Point(int(number.real), int(number.imag))


class Grid:
    def __init__(self, array: np.ndarray):
        self.array = array

    def is_within(self, point: Point) -> bool:
        max_y, max_x = self.array.shape
        x_within = 0 <= point.x < max_x
        y_within = 0 <= point.y < max_y
        within = x_within and y_within
        return within

    def get(self, point: Point, default=None):
        if not self.is_within(point):
            return default
        return self.array[point.y, point.x]

    def set(self, point: Point, fill_value: Any):
        self.array[point.y, point.x] = fill_value
