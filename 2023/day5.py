import parse

from typing import List

from utilities import input


def one(seeds: list, maps: list) -> int:
    locations = []
    for s in seeds:
        for m in range(0, len(maps)):
            for r in maps[m]:
                if s >= r[1] and s < (r[1] + r[2]):
                    s = (r[0] + s - r[1])
                    break
        locations.append(s)
    return min(locations)


def transform(start: int, end: int, new_seeds: list[tuple[int]], seeds: list[tuple[int]], map: list[int]) -> int:
    for dest, source, range_length in map:
        # Check if the ranges overlap
        overlap_start = max(start, source)
        overlap_end = min(end, source + range_length)

        if overlap_start < overlap_end:
            new_seeds.append(
                (
                    dest + (overlap_start - source),
                    dest + (overlap_end - source)
                )
            )

            if start < overlap_start:
                seeds.append((start, overlap_start))

            if overlap_end < end:
                seeds.append((overlap_end, end))

            break
    else:
        # No overlap so add the original seed range to the "new seeds"
        new_seeds.append((start, end))

    return new_seeds, seeds


def two(seeds: List[tuple[int]], maps: list) -> int:
    for m in maps:
        new_seeds = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            new_seeds, seeds = transform(start, end, new_seeds, seeds, m)
        seeds = new_seeds
    return min(seeds)[0]


if __name__ == "__main__":
    data = input.str_array_from_list("5.txt")
    l1 = parse.parse("seeds: {}", data[0])
    seeds = [int(seed) for seed in l1[0].split()]
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = [[] for _ in range(7)]

    maps_index = -1
    for line in data[1:]:
        if line == "":
            continue
        p = parse.parse("{}-to-{} map:", line)
        if p:
            maps_index += 1
            continue
        r = [int(x) for x in line.split()]
        maps[maps_index].append([r[0], r[1], r[2]])

    print(f"Part 1: {one(seeds, maps)}")
    print(f"Part 2: {two(seed_ranges, maps)}")
