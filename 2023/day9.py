from typing import List

from utilities import input


def next_value(seq: List[int]) -> List[int]:
    if all([i == 0 for i in seq]):
        return 0
    else:
        return seq[-1] + next_value(
            [seq[i + 1] - seq[i] for i in range(0, len(seq) - 1)]
        )


def prev_value(seq: List[int]) -> List[int]:
    if all([i == 0 for i in seq]):
        return 0
    else:
        return seq[0] - prev_value(
            [seq[i + 1] - seq[i] for i in range(0, len(seq) - 1)]
        )


def one(seqs: List[List[int]]) -> int:
    next_values = []
    for s in seqs:
        next_values.append(next_value(s))
    return sum(next_values)


def two(data: List[str]) -> int:
    prev_values = []
    for s in seqs:
        prev_values.append(prev_value(s))
    return sum(prev_values)


if __name__ == "__main__":
    data = input.str_array_from_list("9.txt")
    seqs = [[int(x) for x in line.split()] for line in data]

    print(f"Part 1: {one(seqs)}")
    print(f"Part 2: {two(data)}")
