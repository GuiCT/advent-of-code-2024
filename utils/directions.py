from enum import Enum
from utils.grid import Point


class Direction(Enum):
    TOP = Point(0, -1)
    RIGHT = Point(1, 0)
    BOTTOM = Point(0, 1)
    LEFT = Point(-1, 0)
