import parse

from utilities import input


def get_matches(w: list, d: list) -> int:
    matches = 0
    for j in range(0, len(w)):
        if w[j] in d:
            matches += 1
    return matches


def one(winners: list, drawn: list) -> int:
    grand_total = 0
    for i in range(0, len(winners)):
        matches = get_matches(winners[i], drawn[i]) 
        if matches > 0:
            card_value = pow(2, matches - 1)
            grand_total += card_value
    return grand_total


def two(winners: list, drawn: list) -> int:
    copies = [1] * len(winners)
    for i in range(0, len(copies)):
        matches = get_matches(winners[i], drawn[i])
        for j in range(1, matches+1):
            copies[i+j] += (1 * copies[i])

    return sum(copies)


if __name__ == "__main__":
    data = input.str_array_from_list("4.txt")
    winners = []
    drawn = []
    for line in data:
        tokens = parse.parse("Card {}:{}|{}", line)
        winners.append([int(t) for t in tokens[1].split()])
        drawn.append([int(t) for t in tokens[2].split()])

    print(f"Part 1: {one(winners, drawn)}")
    print(f"Part 2: {two(winners, drawn)}")
