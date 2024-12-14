from utilities.input import read_rows_of_strings


def part_one(grid, word) -> int:
    total = 0
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # up-right
        (-1, -1),  # up-left
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
    ]

    def valid_direction(grid, dx, dy, row, col, target):
        for i in range(len(target)):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            if grid[row][col] != target[i]:
                return False
            row += dy
            col += dx
        return True

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for direction in directions:
                if valid_direction(grid, direction[0], direction[1], row, col, word):
                    total += 1
    return total


def part_two(grid) -> int:
    total = 0
    axes = [
        [  # nw_se
            (-1, -1),
            (1, 1),
        ],
        [  # ne_sw
            (-1, 1),
            (1, -1),
        ],
    ]

    # for each cell in the inner grid check if it's an 'A'
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if grid[row][col] == "A":
                # if it is, check if the two axes are either 'M' and 'S' or 'S' and 'M'
                if (
                    grid[row + axes[0][0][0]][col + axes[0][0][1]] == "M"
                    and grid[row + axes[0][1][0]][col + axes[0][1][1]] == "S"
                ) or (
                    grid[row + axes[0][0][0]][col + axes[0][0][1]] == "S"
                    and grid[row + axes[0][1][0]][col + axes[0][1][1]] == "M"
                ):
                    if (
                        grid[row + axes[1][0][0]][col + axes[1][0][1]] == "M"
                        and grid[row + axes[1][1][0]][col + axes[1][1][1]] == "S"
                    ) or (
                        grid[row + axes[1][0][0]][col + axes[1][0][1]] == "S"
                        and grid[row + axes[1][1][0]][col + axes[1][1][1]] == "M"
                    ):
                        total += 1

    return total


if __name__ == "__main__":
    grid = read_rows_of_strings("input/4.txt")
    print(f"Part One: {part_one(grid, "XMAS")}")
    print(f"Part Two: {part_two(grid)}")
