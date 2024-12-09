import re
import numpy as np


# This capture group allows to match overlapped
xmas_regex = re.compile(r"(?=XMAS|SAMX)")
mas_regex = re.compile(r"(?=MAS|SAM)")

with open("04/input.txt", "r") as f:
    lines = f.readlines()

square_size = len(lines)
char_matrix = np.full((square_size, square_size), fill_value='X', dtype=str)

for i in range(square_size):
    for j in range(square_size):
        char_matrix[i, j] = lines[i][j]

found_quantity = 0
for k in range(square_size):
    this_line = "".join(char_matrix[k, :].tolist())
    this_column = "".join(char_matrix[:, k].tolist())
    main_diagonal_1 = "".join(char_matrix.diagonal(k).tolist())
    main_diagonal_2 = "".join(char_matrix.diagonal(-k).tolist())
    inverse_diagonal_1 = "".join(np.fliplr(char_matrix).diagonal(k).tolist())
    inverse_diagonal_2 = "".join(np.fliplr(char_matrix).diagonal(-k).tolist())
    found_quantity += len(xmas_regex.findall(this_line))
    found_quantity += len(xmas_regex.findall(this_column))
    found_quantity += len(xmas_regex.findall(main_diagonal_1))
    found_quantity += len(xmas_regex.findall(inverse_diagonal_1))
    if k != 0:
        found_quantity += len(xmas_regex.findall(main_diagonal_2))
        found_quantity += len(xmas_regex.findall(inverse_diagonal_2))

print("Part 1 result", found_quantity)


def check_if_block_is_x_mas(block: np.ndarray) -> bool:
    # Assume that block is 3x3 char matrix
    main_diag = "".join(block.diagonal().tolist())
    inverse_diag = "".join(np.fliplr(block).diagonal().tolist())
    matches_main = len(mas_regex.findall(main_diag)) == 1
    matches_diag = len(mas_regex.findall(inverse_diag)) == 1
    return matches_main and matches_diag


x_mas_quantity = 0
for i in range(0, square_size - 2):
    for j in range(0, square_size - 2):
        block = char_matrix[i: i + 3, j: j + 3]
        x_mas_quantity += check_if_block_is_x_mas(block) == True

print("Part 2 result", x_mas_quantity)
