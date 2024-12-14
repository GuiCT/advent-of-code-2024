from functools import cache

with open("11/input.txt", "r") as f:
    file_input = f.read().splitlines()[0]


@cache
def advance_number(num: int) -> list[int]:
    """Make the split, cached"""
    num_as_str = str(num)
    digit_count = len(num_as_str)
    even_digit_count = digit_count % 2 == 0
    if even_digit_count:
        result = [int(num_as_str[:digit_count // 2]),
                  int(num_as_str[digit_count // 2:])]
        return result
    elif num == 0:
        return [1]
    else:
        return [num * 2024]


def amount_numbers_generated_by_list(numbers: list[int], blinks: int) -> int:
    count = 0
    for n in numbers:
        count += recursive_for_number(n, blinks)

    return count


@cache
def recursive_for_number(num: int, blinks: int):
    """
    Recursiveness works here because the numbers are independent and deterministic.

    Caching makes the second part feasible
    """
    if blinks == 0:
        return 1

    count = 0
    generated_numbers = advance_number(num)
    for n in generated_numbers:
        count += recursive_for_number(n, blinks - 1)

    return count


number_list_at_start = list(map(int, file_input.split()))
print("Part 1 result", amount_numbers_generated_by_list(number_list_at_start, 25))
print("Part 2 result", amount_numbers_generated_by_list(number_list_at_start, 75))
