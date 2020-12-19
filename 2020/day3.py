import math

from helpers.input import str_array_from_list


def tree_strikes(slope, data):
    width = len(data[0]) # 31
    row = 0
    col = 0
    tree_count = 0
    right = slope[0]
    down = slope[1]
    while row < len(data) - 1:
        row += down
        if col >= width - right:
            col = right - (width % col)
        else:
            col += right
        if data[row][col] == "#":
            tree_count += 1
    return tree_count


def part1(data):
    return tree_strikes((3,1),data)


def part2(data):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    trees = []
    for slope in slopes:
        trees.append(tree_strikes(slope,data))
    return math.prod(trees)


if __name__ == "__main__":
    data = str_array_from_list("3.txt")
    print(part1(data))
    print(part2(data))
