from typing import Callable, List
from utilities.input import read_line


def detect_dupe(id: int) -> bool:
    id_len = len(str(id))
    if id_len % 2 != 0:
        return False
    if str(id)[0 : (id_len // 2)] == str(id)[(id_len // 2) :]:
        return True
    return False


def detect_dupe_two(id: int) -> bool:
    id_str = str(id)
    id_len = len(id_str)

    # Try each possible segment length from 1 to half the ID length
    # (we need at least 2 repetitions, so segment can't be longer than half)
    for segment_len in range(1, id_len // 2 + 1):
        # Check if the ID length is divisible by the segment length
        if id_len % segment_len != 0:
            continue

        # Calculate number of repetitions
        num_repetitions = id_len // segment_len

        # Need at least 2 repetitions
        if num_repetitions < 2:
            continue

        # Extract the first segment
        first_segment = id_str[:segment_len]

        # Check if all segments are identical
        all_same = True
        for i in range(1, num_repetitions):
            segment = id_str[i * segment_len : (i + 1) * segment_len]
            if segment != first_segment:
                all_same = False
                break

        # If all segments are the same, this ID is invalid
        if all_same:
            return True

    return False


def solve(ranges: List[List[int]], detect_dupe_func: Callable[[int], bool]) -> int:
    sum_of_invalid_ids = 0
    for r in ranges:
        for id in range(r[0], r[1] + 1):
            if detect_dupe_func(id):
                sum_of_invalid_ids += id
    return sum_of_invalid_ids


if __name__ == "__main__":
    input = read_line("input/2.txt")
    ranges = [list(map(int, entry.split("-"))) for entry in input.split(",")]

    print(solve(ranges, detect_dupe))
    print(solve(ranges, detect_dupe_two))
