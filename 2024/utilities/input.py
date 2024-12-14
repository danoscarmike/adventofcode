from pathlib import Path


BASE_PATH = "/Users/danielomeara/code/adventofcode/2024/input/"

# read columns of integers from a file into a list of lists
def read_columns_from_file(file_path: str, cols) -> list:
    path = Path(BASE_PATH + file_path)

    columns = [[] for i in range(cols)]
    with open(path, "r") as f:
        for line in f.readlines():
            for i in range(cols):
                columns[i].append(int(line.split()[i]))

    return columns


def read_file_to_string(file_path: str) -> str:
    path = Path(BASE_PATH + file_path)
    with open(path, "r") as f:
        return f.read()


# read rows as strings from a file into a list of lists
def read_rows_of_strings(file_path: str) -> list:
    path = Path(BASE_PATH + file_path)
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(line.strip())

    return rows


# read rows of integers from a file into a list of lists
def read_rows_of_ints(file_path: str) -> list:
    path = Path(BASE_PATH + file_path)
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(list(map(int, line.split())))

    return rows


# read rows of chars from a file into a list of lists
def read_rows_of_chars(file_path: str) -> list:
    path = Path(BASE_PATH + file_path)
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(list(line))

    return rows
