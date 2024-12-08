import re


mul_or_block_regex = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")

with open("03/input.txt", "r") as f:
    total_string = f.read().replace("\n", "")


# This guy is a hero https://www.reddit.com/r/adventofcode/comments/1h5frsp/comment/m05of6n/
# I tried to use separate regexes to detect do(), don't(), create blocks and then parse the mul
# instructions inside them, however, reading this guys solution, i realized you can just iterate
# over the union of those. Pretty smart, give'em some love. 
sum_part_1 = sum_part_2 = 0
currently_enabled = True
for first_number, second_number, do, dont in re.findall(mul_or_block_regex, total_string):
    if do or dont:
        currently_enabled = bool(do)
    else:
        x = int(first_number) * int(second_number)
        sum_part_1 += x
        sum_part_2 += x * currently_enabled

print("Part 1 result", sum_part_1)
print("Part 2 result", sum_part_2)
