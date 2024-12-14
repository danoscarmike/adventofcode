import sys

sys.path.append("../utilities")

from utilities.input import read_rows_of_chars


def find_guard(grid) -> tuple:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "^":
                return row, col


def is_valid(grid, row, col) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def patrol(grid, row, col) -> set:
    visited = set()

    dr, dc = -1, 0

    while True:
        visited.add((row, col))

        if not is_valid(grid, row + dr, col + dc):
            break

        if grid[row + dr][col + dc] == "#":
            dr, dc = dc, -dr

        row, col = row + dr, col + dc

    return visited


def check_for_cycle(grid, row, col) -> bool:
    dr, dc = -1, 0
    visited = set()

    while True:

        if (row, col, dr, dc) in visited:
            return True

        visited.add((row, col, dr, dc))

        if not is_valid(grid, row + dr, col + dc):
            return False

        if grid[row + dr][col + dc] == "#":
            dr, dc = dc, -dr
        else:
            row += dr
            col += dc


def trap_patrol(grid, row, col) -> int:
    start_row, start_col = row, col
    cycles = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                continue
            grid[row][col] = "#"
            if check_for_cycle(grid, start_row, start_col):
                cycles += 1
            grid[row][col] = "."

    return cycles


def part_one(grid) -> int:
    row, col = find_guard(grid)
    visited = patrol(grid, row, col)

    return len(visited)


def part_two(grid) -> int:
    row, col = find_guard(grid)
    return trap_patrol(grid, row, col)


if __name__ == "__main__":
    grid = read_rows_of_chars(sys.argv[1])
    print(f"Part One: {part_one(grid)}")
    print(f"Part Two: {part_two(grid)}")
