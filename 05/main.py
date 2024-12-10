import numpy as np
import re
from functools import cmp_to_key


parse_precedence_rule = re.compile(r"(\d+)\|(\d+)")


with open("05/input.txt", "r") as f:
    lines = f.readlines()

precedences = dict[int, list[int]]()


def validate_precedence(key: int, after: int):
    stored_precedences = precedences.get(key, list())
    return after not in stored_precedences


cmp = cmp_to_key(lambda k, a: 1 - 2 * validate_precedence(k, a))

i = 0
while True:
    regex_match = parse_precedence_rule.match(lines[i])
    if not regex_match:
        break
    before = int(regex_match.group(1))
    after = int(regex_match.group(2))
    stored_precedences = precedences.get(after, list())
    stored_precedences.append(before)
    precedences[after] = stored_precedences
    i += 1

i += 1
valid_middle_pages = list[int]()
middle_after_invalid_sort = list[int]()
while i < len(lines):
    number_list = list(map(lambda n: int(n), lines[i].split(',')))
    valid_record = True
    for k in range(len(number_list)):
        key = number_list[k]
        tail = number_list[k + 1:]
        all_valid = all(map(lambda a: validate_precedence(key, a), tail))
        if not all_valid:
            valid_record = False
            break
    if valid_record:
        valid_middle_pages.append(number_list[len(number_list) // 2])
    else:
        sorted = list(number_list)
        sorted.sort(key=cmp)
        middle_after_invalid_sort.append(sorted[len(sorted) // 2])
    i += 1

print("Part 1 result", sum(valid_middle_pages))
print("Part 2 result", sum(middle_after_invalid_sort))
