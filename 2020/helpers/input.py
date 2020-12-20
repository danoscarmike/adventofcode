import os


def get_dir(test):
    if test:
        return "/test_data/"
    return "/input/"


def int_array_from_list(path, test=False):
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            data.append(int(line.rstrip()))
    return data


def str_array_from_list(path, test=False):
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            data.append(line.rstrip())
    return data


def dict_array_from_file(path, test=False):
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        passport = {}
        for line in f.readlines():
            if line == "\n" or "":
                data.append(passport)
                passport = {}
            else:
                tokens = line.split(" ")
                for token in tokens:
                    kv_pair = token.split(":")
                    passport[kv_pair[0]] = kv_pair[1].rstrip()
        if len(passport) > 0:
            data.append(passport)
    return data

