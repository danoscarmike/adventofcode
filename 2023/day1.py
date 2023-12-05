from utilities import input


def one(data: list) -> int:
    calibration_values = []

    for value in data:
        calibration_value = [int(i) for i in value if i.isdigit()]
        calibration_values.append(calibration_value[0] * 10 + calibration_value[-1])

    return sum(calibration_values)


def two(data: list) -> int:
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibration_values = []
    for value in data:
        tens = None
        ones = None
        for i in range(len(value)):
            if value[i].isdigit():
                tens = int(value[i]) * 10
            else:
                for number in numbers:
                    if value[i:].startswith(number):
                        tens = (numbers.index(number) + 1) * 10
            if tens:
                break
        for j in range(len(value) - 1, -1, -1):
            if value[j].isdigit():
                ones = int(value[j])
            else:
                for number in numbers:
                    if value[: j + 1].endswith(number):
                        ones = numbers.index(number) + 1
            if ones:
                break
        calibration_values.append(tens + ones)

    return sum(calibration_values)


if __name__ == "__main__":
    data = input.str_array_from_list("1.txt")
    print(f"Part 1: {one(data)}")
    print(f"Part 2: {two(data)}")
