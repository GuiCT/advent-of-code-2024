import numpy as np
import itertools
from collections import defaultdict
from utils.grid import Grid, Point
from math import gcd

with open("08/input.txt", "r") as f:
    lines = f.read().splitlines()

row_count = len(lines)
column_count = len(lines[0])
pL = Point(column_count, row_count)
char_matrix = np.full((column_count, row_count), '.')
for i in range(len(lines)):
    char_matrix[i, :] = list(lines[i])

char_grid = Grid(char_matrix)

# Resolve for all positions where c != '.'
filled_by_symbol = defaultdict[str, list[Point]](list[Point])
for (i, j) in zip(*np.where(char_matrix != '.')):
    points = Point(int(j), int(i))
    value = char_grid.get(points)
    filled_by_symbol[str(value)].append(points)

generated_antinodes_part_1 = set[Point]()
generated_antinodes_part_2 = set[Point]()
for sym, points in filled_by_symbol.items():
    amount_of_symbols = len(points)
    pairs = itertools.combinations(points, 2)
    for (p1, p2) in pairs:
        dP = p2 - p1
        a1 = p1 - dP
        a2 = p2 + dP
        a1 = a1 if a1 == a1 % pL else None
        a2 = a2 if a2 == a2 % pL else None
        generated_antinodes_part_1.add(a1)
        generated_antinodes_part_1.add(a2)
        generated_antinodes_part_2.add(p1)
        generated_antinodes_part_2.add(p2)
        generated_antinodes_part_1.add(a1)
        generated_antinodes_part_1.add(a2)
        both_valid = a1 is not None or a2 is not None
        multiplier = 1
        dx, dy = dP
        gcd_dxy = gcd(dx, dy)
        if gcd_dxy != 1:
            dx = dx // gcd_dxy
            dy = dy // gcd_dxy
        dP = Point(dx, dy)
        while both_valid:
            a1 = p1 - multiplier * dP
            a2 = p2 + multiplier * dP
            a1 = a1 if a1 == a1 % pL else None
            a2 = a2 if a2 == a2 % pL else None
            generated_antinodes_part_2.add(a1)
            generated_antinodes_part_2.add(a2)
            both_valid = a1 is not None or a2 is not None
            multiplier += 1


generated_antinodes_part_1.remove(None)
generated_antinodes_part_2.remove(None)
print("Part 1 result", len(generated_antinodes_part_1))
print("Part 2 result", len(generated_antinodes_part_2))
