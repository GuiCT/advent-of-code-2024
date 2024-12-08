from typing import Tuple
import numpy as np


def parse_line(line: str) -> Tuple[int, int]:
    first, second = line.split("   ")
    return (int(first), int(second))


with open("input.txt", "r") as f:
    lines = f.readlines()


first_list = np.zeros(len(lines), dtype=int)
second_list = np.zeros_like(first_list, dtype=int)
for i in range(len(lines)):
    first_column, second_column = parse_line(lines[i])
    first_list[i] = first_column
    second_list[i] = second_column

first_list_sorted = np.sort(first_list)
second_list_sorted = np.sort(second_list)
distances_sum = np.sum(np.abs(first_list_sorted - second_list_sorted))
print("Part 1 result", distances_sum)

similarities = np.zeros_like(first_list_sorted)
for i in range(len(lines)):
    count_second_list = np.count_nonzero(second_list == first_list[i])
    similarities[i] = first_list[i] * count_second_list

similarities_sum = np.sum(similarities)
print("Part 2 result", similarities_sum)
