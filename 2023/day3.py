import re

from utilities import input


def is_symbol(test: str) -> bool:
    match = re.search(r"[^\.a-zA-Z0-9]+", test)
    if match and match.group() != ".":
        return True

    return False


def is_star(test: str) -> bool:
    match = re.find(r'\*', test)
    if match:
        return True
    
    return False


def get_adjacents(line: int, start: int, end: int, data: list) -> str:
    n = len(data)
    m = len(data[0])
    adjacents = ""
    for dx in range(-1 if (line > 0) else 0, 2 if (line < (n-1)) else 1):
        for dy in range(-1 if (start > 0) else 0, end-start+1 if (end < (m-1)) else end-start):
            if (dx != 0 or (dy < 0 or dy >= end-start)):
                adjacents += data[line + dx][start + dy]
    
    return adjacents


def get_adjacent_numbers(line: int, index: int, data: list) -> list:
    n = len(data)
    numbers = []
    for dx in range(-1 if (line > 0) else 0, 2 if (line < (n-1)) else 1):
        for match in re.finditer(r'\d+', data[line + dx]):
            if index >= match.start() - 1 and index <= match.end():
                numbers.append(int(match.group()))
    
    return numbers


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
    gears = []
    line_number = 0
    for line in data:
        for match in re.finditer(r'\*', line):
            numbers = get_adjacent_numbers(line_number, match.start(), data)
            if len(numbers) == 2:
                gears.append(numbers[0] * numbers[1])
        line_number += 1
    
    return sum(gears)


if __name__ == "__main__":
    data = input.str_array_from_list("3.txt")
    test = input.str_array_from_list("3_test.txt")

    print(f"Part 1: {one(data)}")
    print(f"Part 2: {two(data)}")
