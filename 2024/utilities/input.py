import os


# read columns of integers from a file into a list of lists
def read_columns_from_file(path: str, cols) -> list:
    directory = "/2024/input/"
    columns = [[] for i in range(cols)]
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            for i in range(cols):
                columns[i].append(int(line.split()[i]))

    return columns


# read rows of integers from a file into a list of lists
def read_rows_from_file(path: str) -> list:
    directory = "/2024/input/"
    rows = []
    with open(os.getcwd() + directory + path, "r") as f:
        for line in f.readlines():
            rows.append(list(map(int, line.split())))

    return rows
