with open("22/input.txt", "r") as f:
    numbers = list(map(int, f.read().splitlines()))


def advance_secret_number(num: int) -> int:
    curr = num
    curr = (curr ^ (curr << 6)) & 0xFFFFFF
    curr = (curr ^ (curr >> 5)) & 0xFFFFFF
    curr = (curr ^ (curr << 11)) & 0xFFFFFF
    return curr


def advance_2000_times(num: int) -> int:
    for _ in range(2000):
        num = advance_secret_number(num)
    return num


numbers_after_2000 = list(map(advance_2000_times, numbers))
print("Part 1 result", sum(numbers_after_2000))
