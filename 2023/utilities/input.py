import os

def get_dir(test):
    if test:
        return "/test_data/"
    return "/input/"


def int_array_from_list(path: str, test: bool=False) -> list:
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            data.append(int(line.rstrip()))
    return data


def str_array_from_list(path: str, test: bool=False) -> list:
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            data.append(line.rstrip())
    return data