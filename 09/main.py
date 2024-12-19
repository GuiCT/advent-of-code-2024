"""
Heavily guided by this one
https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/9.py
The different form of representing part 1 and 2 makes it so much easier.
I just changed some portions that were hard to read
"""

with open("09/input.txt", "r") as f:
    sectors_specs = f.read().splitlines()[0]


def prepare_defrag(represent_file_as_blocks: bool) -> tuple[
    list[tuple[int, int, int]],
    list[tuple[int, int]],
    list[int | None]
]:
    files = list[tuple[int, int, int]]()
    spaces = list[tuple[int, int]]()
    file_id = 0
    resulting_list = list[int | None]()
    pos = 0
    for i, c in enumerate(sectors_specs):
        if i % 2 == 0:  # Files
            resulting_list.extend([file_id] * int(c))
            if not represent_file_as_blocks:
                new_files = [(pos + i, 1, file_id) for i in range(int(c))]
                files.extend(new_files)
                # Files are treated as 1-wide elements
                # Part 2 however, will represent files as blocks
            else:
                files.append((pos, int(c), file_id))
                # Here, we include a whole block instead of
                # a file that occupies one position only.
            file_id += 1
        else:  # Spaces
            spaces.append((pos, int(c)))
            resulting_list.extend([None] * int(c))
        pos += int(c)
    return files, spaces, resulting_list


def execute_defrag(files, spaces, final_list):
    for (file_position, file_size, file_id) in reversed(files):
        for space_i, (space_position, space_size) in enumerate(spaces):
            if space_position < file_position and file_size <= space_size:
                for i in range(file_size):
                    assert final_list[file_position +
                                      i] == file_id, f'{final_list[file_position+i]=}'
                    final_list[file_position+i] = None
                    final_list[space_position+i] = file_id
                spaces[space_i] = (space_position + file_size,
                                   space_size - file_size)
                break

    return final_list


ans_p1 = ans_p2 = 0
result_list_p1 = execute_defrag(*prepare_defrag(False))
for i, c in enumerate(result_list_p1):
    if c is not None:
        ans_p1 += i*c

print("Part 1 result", ans_p1)

result_list_p2 = execute_defrag(*prepare_defrag(True))
for i, c in enumerate(result_list_p2):
    if c is not None:
        ans_p2 += i*c

print("Part 2 result", ans_p2)
