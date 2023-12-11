import parse

from utilities import input


class SourceRangeMap:
    source_start = None
    dest_start = None
    span = None

    def __init__(self, dest_start: int, source_start: int, span: int) -> None:
        self.source_start = source_start
        self.dest_start = dest_start
        self.span = span

    def range_contains(self, value: int) -> bool:
        if value >= self.source_start and value < (self.source_start + self.span):
            return True
        return False

    def get_destination(self, value: int) -> int:
        if not self.range_contains(value):
            raise ValueError
        else:
            return self.dest_start + (value - self.source_start)


def next_destination(maps: list, map_index: int, value: int):
    next = value
    for r in maps[map_index]:
        if r.range_contains(value):
            next = r.get_destination(value)
            break
    return next


def one(seeds: list, maps: list) -> int:
    locations = []
    for s in seeds:
        for m in range(0, len(maps)):
            s = next_destination(maps, m, s)
        locations.append(s)
    return min(locations)


def two(data: list) -> int:
    return 0


if __name__ == "__main__":
    data = input.str_array_from_list("5.txt")
    l1 = parse.parse("seeds: {}", data[0])
    seeds = [int(seed) for seed in l1[0].split()]

    maps_list = [[] for _ in range(7)]

    maps_index = -1
    for line in data[1:]:
        if line == "":
            continue
        p = parse.parse("{}-to-{} map:", line)
        if p:
            maps_index += 1
            continue
     
        r = [int(x) for x in line.split()]
        maps_list[maps_index].append(SourceRangeMap(r[0], r[1], r[2]))

    print(f"Part 1: {one(seeds, maps_list)}")
    print(f"Part 2: {two(data)}")
