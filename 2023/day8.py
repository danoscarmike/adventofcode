from collections import defaultdict
from itertools import cycle
from math import lcm
from parse import parse
from typing import DefaultDict, List

from utilities import input


def one(directions: List[int], nodes: DefaultDict[str, List[str]]) -> int:
    count = 0
    found = False
    current_node = 'AAA'
    while not found:
        for step in directions:
            count += 1
            current_node = nodes[current_node][step]
            if current_node == "ZZZ":
                found = True
                break

    return count


def two(directions: List[int], nodes: DefaultDict[str, List[str]]) -> int:
    current_nodes = [n for n in nodes if n.endswith('A')]
    required_steps = []
    for n in current_nodes:
        for count, step in enumerate(cycle(directions), start=1):
            n = nodes[n][step]
            if n.endswith('Z'):
                required_steps.append(count)
                break

    return lcm(*required_steps)


if __name__ == "__main__":
    data = input.str_array_from_list("8.txt")

    directions = [1 if step == "R" else 0 for step in data[0]]
    nodes = defaultdict(list)

    for line in data[1:]:
        p = parse("{} = ({}, {})", line)
        if p:
            nodes[p[0]].append(p[1])
            nodes[p[0]].append(p[2])

    print(f"Part 1: {one(directions, nodes)}")
    print(f"Part 2: {two(directions, nodes)}")
