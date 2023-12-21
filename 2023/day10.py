from typing import List

from utilities import input

_north_bound = 'JL|'
_east_bound = '-F'
_south_bound = '7F|'
_west_bound = '-7'


def compute_s_node(vertices: List[List], v) -> str:
    north = vertices[v[0]-1][v[1]]
    east = vertices[v[0]][v[1]+1]
    south = vertices[v[0]+1][v[1]]
    west = vertices[v[0]][v[1]-1]

    if south in _north_bound:
        if east in _west_bound:
            return 'F'
        if north in _south_bound:
            return '|'
        if west in _east_bound:
            return '7'
    if east in _west_bound:
        if north in _south_bound:
            return 'L'
        if west in _east_bound:
            return '-'
    
    return 'J'


def list_s_adjacents(s: tuple[int], s_node: str) -> List:
    adjacents = []
    if s_node in _north_bound:
        adjacents.append((s[0]-1, s[1]))
    if s_node in _east_bound:
        adjacents.append((s[0], s[1] + 1))
    if s_node in _south_bound:
        adjacents.append((s[0]+1, s[1]))
    if s_node in _west_bound:
        adjacents.append((s[0], s[1] - 1))

    return adjacents


def one(vertices: List[List], rows: int, cols: int) -> int:
    graph = {}
    
    for r in range(0, rows):
        for c in range(0, cols):
            v = vertices[r][c]
            adjacent = []
            if v in '-J7':
                adjacent.append((r, c - 1))
            if v in '-FL':
                adjacent.append((r, c + 1))
            if v in '|JL':
                adjacent.append((r - 1, c))
            if v in '|7F':
                adjacent.append((r + 1, c))
            if v == 'S':
                s = (r,c)
                s_node = compute_s_node(vertices, s)
                adjacent = list_s_adjacents(s, s_node)
            
            graph[(r,c)] = adjacent
    
    length = 0
    visited = set([s])
    q = set([s])

    while q:
        next_nodes = set()
        for v in q:
            for n in graph[v]:
                if n not in visited and v in graph.get(n, []):
                    # v and the current node are connected (mutually adjacent)
                    visited.add(n)
                    next_nodes.add(n)
        # step out one in each direction from S
        length += 1
        q = next_nodes

    # S is at 0
    return length - 1


def two(data: List[str]) -> int:
    
    return 0


if __name__ == "__main__":
    data = input.str_array_from_list("10.txt")
    rows = len(data)
    cols = len(data[0])
    nodes = rows * cols
    vertices = []

    for i in range(0, len(data)):
        line = data[i]
        vertices.append([])
        for j in range(0, len(line)):
            vertices[i].append(line[j])

    

    print(f"Part 1: {one(vertices, rows, cols)}")
    # print(f"Part 2: {two(data)}")
