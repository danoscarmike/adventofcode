from utilities.input import read_rows_of_ints


def get_differences(row: list) -> list:
    differences = []
    for i in range(len(row) - 1):
        differences.append(row[i + 1] - row[i])

    return differences


def report_is_safe(differences: list) -> bool:
    if all([diff > 0 for diff in differences]) or all(
        [diff < 0 for diff in differences]
    ):
        if all([abs(diff) < 4 for diff in differences]):
            return True

    return False


def report_is_tolerable(row: list) -> bool:
    differences = get_differences(row)
    if report_is_safe(differences):
        return True

    for i in range(len(row)):
        new_row = row[0:i] + row[i + 1 : len(row)]
        new_differences = get_differences(new_row)
        if report_is_safe(new_differences):
            return True

    return False


def part_one(reports) -> int:
    safe = 0

    # create a list of the differences between list elements
    for row in reports:
        differences = get_differences(row)
        if report_is_safe(differences):
            safe += 1

    return safe


def part_two(reports) -> int:
    safe = 0

    for row in reports:
        if report_is_tolerable(row):
            safe += 1

    return safe


if __name__ == "__main__":
    reports = read_rows_of_ints("input/2.txt")
    print(f"Part One: {part_one(reports)}")
    print(f"Part Two: {part_two(reports)}")
