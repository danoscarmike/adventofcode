import os


def manhattan_distance(port):
    """Calculates the Manhattan distance from a
    node to the central port

    Args:
        port ((int,int)): coordinates of the port

    Returns:
        int: the Manhattan distince from the port
        to the central port
    """
    return abs(port[0]) + abs(port[1])


def get_wire_path(instructions):
    """Converts a list of instructions to a set
    of ports visited by a wire

    Args:
        instructions ([str]): List of instructions of
        the form ['R123','U456','L789','D123']

    Returns:
        ((int,int)): Set of coordinates of ports visited
        by the wire
    """
    path = set()
    x = 0
    y = 0
    for instr in instructions:
        direction = instr[0]
        steps = int(instr[1 : len(instr)])
        if direction == "R":
            i = 0
            while i <= steps:
                i += 1
                if (x + i, y) == (0, 0):
                    continue
                else:
                    path.add((x + i, y))
            x += steps
        if direction == "L":
            i = 0
            while i <= steps:
                i += 1
                if (x - i, y) == (0, 0):
                    continue
                else:
                    path.add((x - i, y))
            x -= steps
        if direction == "U":
            j = 0
            while j <= steps:
                j += 1
                if (x, y + j) == (0, 0):
                    continue
                else:
                    path.add((x, y + j))
            y += steps
        if direction == "D":
            j = 0
            while j <= steps:
                j += 1
                if (x, y - j) == (0, 0):
                    continue
                else:
                    path.add((x, y - j))
            y -= steps
    return path


if __name__ == "__main__":
    path_to_input = os.getcwd() + "/input"
    with open(path_to_input + "/3.txt", "r") as f:
        lines = f.readlines()
        wire_one = [x.rstrip() for x in lines[0].split(",")]
        wire_two = [x.rstrip() for x in lines[1].split(",")]

    path_one = get_wire_path(wire_one)
    path_two = get_wire_path(wire_two)
    min_md = float("inf")
    min_port = None

    for port in path_one:
        if port in path_two:
            md = manhattan_distance(port)
            if md < min_md:
                min_md = md
                min_port = port

    print(f"Minimum MD: {min_md}")
    print(f"Port: {min_port}")
