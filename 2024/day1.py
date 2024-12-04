from utilities.input import read_columns_from_file


(col1, col2) = read_columns_from_file("1.txt", 2)


def part_one() -> int:
    left = col1.copy()
    right = col2.copy()

    list_distance = 0

    for _ in range(len(left)):
        left_min = left.pop(min(enumerate(left), key=lambda v: v[1])[0])
        right_min = right.pop(min(enumerate(right), key=lambda v: v[1])[0])
        list_distance += abs(left_min - right_min)

    return list_distance


def part_two() -> int:
    left = col1.copy()
    right = col2.copy()
    
    similarity = 0
    
    for element in left:
        similarity += right.count(element) * element

    return similarity


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
