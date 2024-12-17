import numpy as np
import re
from typing import NamedTuple
from utils.grid import Point

parse_info_regex = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

with open("14/input.txt", "r") as f:
    lines = f.read().splitlines()

Robot = NamedTuple("Robot", [("position", Point), ("velocity", Point)])
robot_list = list[Robot]()
for l in lines:
    match_res = parse_info_regex.match(l)
    if not match_res:
        continue
    pos = Point(int(match_res.group(1)), int(match_res.group(2)))
    vel = Point(int(match_res.group(3)), int(match_res.group(4)))
    robot = Robot(pos, vel)
    robot_list.append(robot)

row_count = 103
middle_row = row_count // 2
column_count = 101
middle_column = column_count // 2
point_mod = Point(column_count, row_count)
p1_robots = list(map(lambda r: (r.position + 100 * r.velocity) %
                 point_mod, robot_list))
first_quadrant = list(filter(lambda p: (
    0 <= p.x < middle_column) and (0 <= p.y < middle_row), p1_robots))
second_quadrant = list(filter(lambda p: (
    middle_column < p.x < column_count) and (0 <= p.y < middle_row), p1_robots))
third_quadrant = list(filter(lambda p: (
    0 <= p.x < middle_column) and (middle_row < p.y < row_count), p1_robots))
fourth_quadrant = list(filter(lambda p: (
    middle_column < p.x < column_count) and (middle_row < p.y < row_count), p1_robots))

print("Quadrants", len(first_quadrant), len(second_quadrant),
      len(third_quadrant), len(fourth_quadrant))
print("Part 1 (product)", len(first_quadrant) * len(second_quadrant)
      * len(third_quadrant) * len(fourth_quadrant))

# About part 2
# 1. Fuck that
# 2. Gonna assume that the tree is present if there is a tree base, a line with at least 8 robots


def max_crescent_section(filled_columns: np.ndarray):
    sorted_cols = np.sort(filled_columns)

    max_count = 0
    curr_count = 1
    for i in range(1, len(sorted_cols)):
        if sorted_cols[i] == sorted_cols[i - 1] + 1:
            curr_count += 1
            max_count = max(max_count, curr_count)
        else:
            curr_count = 1
    max_count = max(max_count, curr_count)
    return max_count


max_iter = 100000
for it in range(max_iter):
    points = list(
        map(lambda r: (r.position + it * r.velocity) % point_mod, robot_list)
    )
    for i in range(row_count):
        filled_columns = np.sort(np.unique(np.array(list(
            map(lambda p: p.x, filter(lambda p: p.y == i, points))
        ))))  # I love python parenthesis nightmare. No shame.
        line_length = max_crescent_section(filled_columns)
        if line_length >= 8:
            print("Part 2 result", it)
            exit(0)
