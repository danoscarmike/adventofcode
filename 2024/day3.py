import re

from utilities.input import read_file_to_string


memory = read_file_to_string("3.txt")


def find_muls(string: str) -> list:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, string)


def part_one() -> int:
    total = 0

    matches = find_muls(memory)

    for mul in matches:
        pattern = r"(\d+),(\d+)"
        match = re.search(pattern, mul)
        total += int(match.group(1)) * int(match.group(2))

    return total


def part_two() -> int:
    total = 0

    pattern_groups = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"
    group_matches = re.findall(pattern_groups, memory)

    do = True

    for match in group_matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                pattern = r"(\d+),(\d+)"
                mul_match = re.search(pattern, match)
                total += int(mul_match.group(1)) * int(mul_match.group(2))    

    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
