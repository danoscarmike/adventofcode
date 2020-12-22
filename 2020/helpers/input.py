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


def dict_array_from_file(path, test=False, parsing=4):
    directory = get_dir(test)
    data = []
    with open(os.getcwd() + directory + path, "r") as f:
        dictionary = {}
        for line in f.readlines():
            if line == "\n" or "":
                data.append(dictionary)
                dictionary = {}
            elif parsing == 4:
                tokens = line.split(" ")
                for token in tokens:
                    kv_pair = token.split(":")
                    dictionary[kv_pair[0]] = kv_pair[1].rstrip()
            elif parsing == 6:
                if len(dictionary) == 0:
                    dictionary = {"answers": [line.rstrip()]}
                else:
                    dictionary["answers"].append(line.rstrip())
        if len(dictionary) > 0:
            data.append(dictionary)
    return data
