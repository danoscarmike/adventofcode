import itertools
import sys

from collections import defaultdict

sys.path.append("../utilities")

from utilities.input import read_rows_of_chars


def is_valid_location(grid, location):
    return 0 <= location[0] < len(grid) and 0 <= location[1] < len(grid[0])


def find_similar_antennas(grid):
    antennas = defaultdict(list)
    for row in grid:
        for cell in row:
            if cell == "." or cell in antennas.keys():
                continue
            else:
                 antenna_locations = []
                 for i, line in enumerate(grid):
                    for j, col in enumerate(line):
                        if col == cell:
                            antenna_locations.append((i, j))             
                
            antennas[cell] = antenna_locations
    
    return antennas


def find_all_antinodes(grid, antenna_pair, harmonics=False):
    antinodes = []
    offset = (antenna_pair[1][0] - antenna_pair[0][0], antenna_pair[1][1] - antenna_pair[0][1])
    up_antinode = (antenna_pair[0][0] - offset[0], antenna_pair[0][1] - offset[1])
    if is_valid_location(grid, up_antinode):
        antinodes.append(up_antinode)
    down_antinode = (antenna_pair[1][0] + offset[0], antenna_pair[1][1] + offset[1])
    if is_valid_location(grid, down_antinode):
        antinodes.append(down_antinode)
    if not harmonics:
        return antinodes
    else:
        # Check for additional antinodes (upward)
        on_grid = True
        while on_grid:
            next_up_antinode = up_antinode[0] - offset[0], up_antinode[1] - offset[1]
            if is_valid_location(grid, next_up_antinode):
                antinodes.append(next_up_antinode)
                up_antinode = next_up_antinode
            else:
                on_grid = False
        
        # Check for additional antinodes (downward)
        on_grid = True
        while on_grid:
            next_down_antinode = down_antinode[0] + offset[0], down_antinode[1] + offset[1]
            if is_valid_location(grid, next_down_antinode):
                antinodes.append(next_down_antinode)
                down_antinode = next_down_antinode
            else:
                on_grid = False
    
    return antinodes


def part_one(grid) -> int:
    antennas = find_similar_antennas(grid)
    antinodes = set()

    for antenna in antennas.keys():
        for pair in itertools.combinations(antennas[antenna], 2):
            antinodes.update(find_all_antinodes(grid, pair))

    return len(antinodes)


def part_two(grid) -> int:
    antennas = find_similar_antennas(grid)
    antinodes = set()

    for antenna in antennas.keys():
        for pair in itertools.combinations(antennas[antenna], 2):
            antinodes.update(pair)
            antinodes.update(find_all_antinodes(grid, pair, True))

    return len(antinodes)


if __name__ == "__main__":
    grid = read_rows_of_chars(sys.argv[1])
    print(f"Part One: {part_one(grid)}")
    print(f"Part Two: {part_two(grid)}")