import os


def array_from_list(path):
    input = []
    with open(os.getcwd() + "/input/" + path, "r") as f:
        for line in f.readlines():
            input.append(int(line.rstrip()))
    return input