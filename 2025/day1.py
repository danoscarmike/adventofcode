from utilities.input import read_rows_of_strings


class Dial:
    def __init__(self, min: int, max: int, start: int):
        self.min = min
        self.max = max
        self.length = max - min + 1
        self.position = start
        self.zero_crossings = 0

    def turn(self, row: str) -> None:
        if row.startswith("L"):
            for _ in range(int(row[1:])):
                self.position -= 1
                if self.position < 0:
                    self.position = 99
                if self.position == 0:
                    self.zero_crossings += 1
        elif row.startswith("R"):
            for _ in range(int(row[1:])):
                self.position += 1
                if self.position > 99:
                    self.position = 0
                if self.position == 0:
                    self.zero_crossings += 1


def part_one(rows: list) -> int:
    dial = Dial(0, 99, 50)
    password = 0
    for row in rows:
        dial.turn(row)
        if dial.position == 0:
            password += 1
    return password


def part_two(rows: list) -> int:
    dial = Dial(0, 99, 50)
    for row in rows:
        dial.turn(row)
    return dial.zero_crossings


if __name__ == "__main__":
    rows = read_rows_of_strings("input/1.txt")
    print(part_one(rows))
    print(part_two(rows))
