import os


def int_array_from_list(path):
    input = []
    with open(os.getcwd() + "/input/" + path, "r") as f:
        for line in f.readlines():
            input.append(int(line.rstrip()))
    return input


def str_array_from_list(path):
    input = []
    with open(os.getcwd() + "/input/" + path, "r") as f:
        for line in f.readlines():
            input.append(line.rstrip())
    return input
