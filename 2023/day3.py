import re

from utilities import input


def is_symbol(test: str) -> bool:
    match = re.search(r"[^\.a-zA-Z0-9]+", test)
    if match and match.group() != ".":
        return True

    return False


def one(data: list) -> int:
    grand_total = 0
    line_number = 0
    for line in data:
        for match in re.finditer(r'\d+', line):
            if is_symbol(get_adjacents(line_number, match.start(), match.end(), data)):
                grand_total += int(match.group())
        line_number += 1
    
    return grand_total


def two(data: list) -> int:
    return 0


def get_adjacents(line: int, start: int, end: int, data: list) -> str:
    n = len(data)
    m = len(data[0])
    adjacents = ""
    for dx in range(-1 if (line > 0) else 0, 2 if (line < (n-1)) else 1):
        for dy in range(-1 if (start > 0) else 0, end-start+1 if (end < (m-1)) else end-start):
            if (dx != 0 or (dy < 0 or dy >= end-start)):
                adjacents += data[line + dx][start + dy]
    
    return adjacents


if __name__ == "__main__":
    data = input.str_array_from_list("3.txt")
    test = input.str_array_from_list("3_test.txt")

    print(f"Part 1: {one(data)}")
    print(f"Part 2: {two(data)}")

    test_result = one(test)
    print(test_result, test_result == 1924)
