from itertools import product


class Equation:
    PART_1_OPERATIONS = "+*"
    PART_2_OPERATIONS = "+*|"

    def __init__(self, target: int, number_list: list[int], part_2: bool = False):
        self.target = target
        self.number_list = number_list
        size_of_num_list = len(number_list)
        used_operations = Equation.PART_1_OPERATIONS if not part_2 else Equation.PART_2_OPERATIONS
        self.possible_combinations = product(
            used_operations, repeat=size_of_num_list - 1)
        self.is_valid = None

    def try_combinations(self) -> bool:
        for c in self.possible_combinations:
            is_valid = self.try_one_combination(c)
            if is_valid:
                self.is_valid = True
                return True
        self.is_valid = False
        return False

    def try_one_combination(self, operations: tuple[str, ...]) -> bool:
        curr = self.number_list[0]
        for i in range(len(operations)):
            op = operations[i]
            second_number = self.number_list[i + 1]
            match op:
                case '+':
                    curr = curr + second_number
                case '*':
                    curr = curr * second_number
                case '|':
                    digits_of_second_number = len(str(second_number))
                    curr = (curr * (10 ** digits_of_second_number)) + \
                        second_number
                case _:
                    raise ValueError("Invalid operator")
        return curr == self.target


with open("07/input.txt", "r") as f:
    lines = f.read().splitlines()


def line_to_equation(line: str, part_2: bool = False) -> Equation:
    target, tail = line.split(": ")
    number_list = tail.split(" ")
    int_number_list = list(map(int, number_list))
    return Equation(int(target), int_number_list, part_2)


equations = list(map(lambda l: line_to_equation(l, False), lines))
total_sum = 0
for e in equations:
    e.try_combinations()
    if e.is_valid:
        total_sum += e.target

print("Part 1 result", total_sum)

equations_p2 = list(map(lambda l: line_to_equation(l, True), lines))
total_sum_p2 = 0
for e in equations_p2:
    e.try_combinations()
    if e.is_valid:
        total_sum_p2 += e.target
print("Part 2 result", total_sum_p2)
