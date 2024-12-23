from collections import defaultdict
from utils.grid import Grid, Point
from utils.directions import Direction
import numpy as np
from multiprocessing import Pool

with open("06/input.txt", "r") as f:
    lines = f.read().splitlines()

row_count = len(lines)
column_count = len(lines[0])
char_matrix = np.full((row_count, column_count), '.', dtype=str)
char_grid = Grid(char_matrix)

starting_position = None
starting_direction = Point(0, 0)
for i, l in enumerate(lines):
    char_matrix[i, :] = np.array(list(l))
    if starting_position is None:
        for start in "^><v":
            found_pos = l.find(start)
            if found_pos != -1:
                starting_position = Point(found_pos, i)
                match start:
                    case '^':
                        starting_direction = Direction.TOP.value
                    case '>':
                        starting_direction = Direction.RIGHT.value
                    case '<':
                        starting_direction = Direction.LEFT.value
                    case 'v':
                        starting_direction = Direction.BOTTOM.value
                    case _:
                        raise ValueError("Invalid marker")
                break

# Part 1 - Walk through it
visited_matrix = np.full_like(char_matrix, '.')
visited_grid = Grid(visited_matrix)
current_position = starting_position
current_direction = starting_direction
visited_grid.set(current_position, '#')
is_within_bounds = True
while is_within_bounds:
    found_wall = False
    while not found_wall:
        new_position = current_position + current_direction
        is_within_bounds = char_grid.is_within(new_position)
        if not is_within_bounds:
            break
        else:
            next_char = char_grid.get(new_position, '.')
            if next_char == '#':
                found_wall = True
            else:
                current_position = new_position
                visited_grid.set(current_position, '#')
    else:
        # Complex numbers are great to represent rotation xD
        rotated_direction = current_direction.to_complex() / (0 - 1j)
        current_direction = Point.from_complex(rotated_direction)

print("Part 1 result", np.count_nonzero(visited_matrix == '#'))

# Part 2: candidates to change
y_candidate, x_candidate = np.where(char_matrix == '.')
points_candidates = [Point(int(x), int(y))
                     for x, y in zip(x_candidate, y_candidate)]
amount_of_candidates = len(points_candidates)

possible_changes = 0


def process_possibility(p: Point) -> bool:
    new_char_matrix = char_matrix.copy()  # Avoid changing the original
    new_char_grid = Grid(new_char_matrix)
    new_char_grid.set(p, '#')
    # Part 1 copy paste, but save direction as well as visited
    # If we found revisit a specific place with the same direction,
    # a loop was formed.
    current_position = starting_position
    current_direction = starting_direction
    is_within_bounds = True
    visited_places = defaultdict[Point, set[Point]](set[Point])
    visited_places[current_position].add(current_direction)
    loop_formed = False
    while is_within_bounds and not loop_formed:
        found_wall = False
        while not found_wall:
            new_position = current_position + current_direction
            is_within_bounds = new_char_grid.is_within(new_position)
            if not is_within_bounds:
                break
            else:
                loop_formed = current_direction in visited_places[new_position]
                if loop_formed:
                    break
                next_char = new_char_grid.get(new_position, '.')
                if next_char == '#':
                    found_wall = True
                else:
                    current_position = new_position
                    visited_places[current_position].add(current_direction)
        else:
            # Complex numbers are great to represent rotation xD
            rotated_direction = current_direction.to_complex() / (0 - 1j)
            current_direction = Point.from_complex(rotated_direction)
    return loop_formed


# DUMB! Brute force! But.
# Multiprocessing :DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDdd
with Pool(12) as p:
    res = p.map(process_possibility, points_candidates)

print("Part 2 result", sum(res))
