import numpy as np

def parse_line(line: str) -> np.ndarray:
    numbers = line.split(" ")
    return np.array(numbers, dtype=int)


with open("02/input.txt", "r") as f:
    lines = f.readlines()


def diff_is_valid(diff: np.ndarray) -> bool:
    first_is_negative = diff[0] < 0
    if first_is_negative:
        diff = diff * (-1)
    return np.all(diff >= 1) and np.all(diff <= 3)

count_safe = 0
count_safe_one_tolerated = 0
for line in lines:
    report = parse_line(line)
    diff = np.diff(report)
    if diff_is_valid(diff):
        count_safe += 1
        continue
    for i in range(report.size):
        new_report = np.concat([report[:i], report[i + 1:]])
        diff = np.diff(new_report)
        if diff_is_valid(diff):
            count_safe_one_tolerated += 1
            break



print("Part 1 result", count_safe)
print("Part 2 result", count_safe + count_safe_one_tolerated)