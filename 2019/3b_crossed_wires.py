import os


def manhattan_distance(port):
    return abs(port[0]) + abs(port[1])


def update_grid(grid, instructions, pos):
    x = 0
    y = 0
    d = 0
    for instr in instructions:
        direction = instr[0]
        steps = int(instr[1 : len(instr)])
        i = 0
        while i < steps:
            i += 1
            d += 1
            port = (None, None)
            if direction == "R":
                port = (x + i, y)
            if direction == "L":
                port = (x - i, y)
            if direction == "U":
                port = (x, y + i)
            if direction == "D":
                port = (x, y - i)

            if port == (0, 0):
                continue
            elif port in grid.keys():
                if grid[port][pos] > d:
                    grid[port][pos] = d
                    if (grid[port][1] < float("inf")) and (
                        grid[port][2] < float("inf")
                    ):
                        grid[port][0] = manhattan_distance(port)
                        grid[port][3] = grid[port][1] + grid[port][2]
            else:
                grid[port] = [float("inf")] * 4
                grid[port][pos] = d

        if direction == "R":
            x += steps
        if direction == "L":
            x -= steps
        if direction == "U":
            y += steps
        if direction == "D":
            y -= steps


if __name__ == "__main__":
    path_to_input = os.getcwd() + "/input"
    with open(path_to_input + "/3.txt", "r") as f:
        lines = f.readlines()
        wire_one = [x.rstrip() for x in lines[0].split(",")]
        wire_two = [x.rstrip() for x in lines[1].split(",")]

    grid = {}
    update_grid(grid, wire_one, 1)
    update_grid(grid, wire_two, 2)

    min_md = float("inf")
    min_distance = float("inf")
    min_md_port = None
    min_dist_port = None

    for port in grid.keys():
        md = grid[port][0]
        combined_distance = grid[port][3]
        if combined_distance < min_distance:
            min_distance = combined_distance
            min_dist_port = port
        if md < min_md:
            min_md = md
            min_md_port = port

    print(f"Minimum MD: {min_md}")
    print(f"Port: {min_md_port}")
    print(f"Minimum distance: {min_distance}")
    print(f"Port: {min_dist_port}")
