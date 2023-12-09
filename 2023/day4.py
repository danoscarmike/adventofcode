import parse

from utilities import input


def one(winners: list, drawn: list) -> int:
    grand_total = 0
    for i in range(0, len(winners)):
        matches = 0
        for j in range(0, len(winners[i])):
            if winners[i][j] in drawn[i]:
                matches += 1
        if matches > 0:
            card_value = pow(2, matches - 1)
            grand_total += card_value
    return grand_total


def two(data: list) -> int:

    return 0


if __name__ == "__main__":
    data = input.str_array_from_list("4.txt")
    winners = []
    drawn = []
    for line in data:
        tokens = parse.parse("Card {}:{}|{}", line)
        winners.append([int(t) for t in tokens[1].split()])
        drawn.append([int(t) for t in tokens[2].split()])

    print(f"Part 1: {one(winners, drawn)}")
    print(f"Part 2: {two(data)}")
