# Massive thanks to this guy
# https://github.com/derailed-dash/Advent-of-Code/tree/master/src/AoC_2024
# His solutions are very detailed and helped me to understand how to properly use BFS here.
# The use of the Point namedtuple is also his idea
# I've adapted some things, i am allergic to OOP in a way

import numpy as np
from collections import deque, defaultdict
from utils.directions import Direction
from utils.grid import Grid, Point

with open("10/input.txt", "r") as f:
    lines = f.read().splitlines()

row_count = len(lines)
column_count = len(lines[0])
char_matrix = np.full((row_count, column_count), 0, dtype=int)
for i, l in enumerate(lines):
    char_matrix[i, :] = np.array(list(l.replace('.', '0')), dtype=int)
char_grid = Grid(char_matrix)


def get_trails_from_this_origin(origin: Point) -> tuple[
    set[Point],
    dict[Point, set[Point]]
]:
    tree = deque[Point]()
    tree.append(origin)
    trailends = set[Point]()
    precedings = defaultdict[Point, set[Point]](set[Point])
    precedings[origin] = set[Point]()

    while tree:
        curr_pos: Point = tree.popleft()
        curr_val = char_grid.get(curr_pos)

        if curr_val == 9:
            trailends.add(curr_pos)
            continue

        for d in Direction:
            next_pos = curr_pos + d.value
            next_val = char_grid.get(next_pos)
            valid_number = next_val == curr_val + 1
            visited = next_pos in precedings
            if valid_number:
                if not visited:
                    tree.append(next_pos)
                precedings[next_pos].add(curr_pos)

    return trailends, precedings


def get_paths_to_trailends(
    origin: Point,
    trailends: set[Point],
    precedings: dict[Point, set[Point]]
) -> list:
    paths = list[Point]()
    stack = list[tuple[Point, list[Point]]]()

    # Fill stack with trailends
    for trailend in trailends:
        stack.append((trailend, [trailend]))

    while stack:
        current, path = stack.pop()

        # Found origin -> Reverse path and get the full trail
        if current == origin:
            paths.append(path[::-1])
            continue

        # Push all predecessors of the current point onto the stack
        for predecessor in precedings.get(current, set()):
            stack.append((predecessor, path + [predecessor]))

    return paths


scores_p1_sum = 0
scores_p2_sum = 0
for (i, j) in zip(*np.where(char_matrix == 0)):
    origin = Point(j, i)
    trailends, precedings = get_trails_from_this_origin(origin)
    scores_p1_sum += len(trailends)
    paths = get_paths_to_trailends(origin, trailends, precedings)
    scores_p2_sum += len(paths)


print("Part 1 result", scores_p1_sum)
print("Part 2 result", scores_p2_sum)
