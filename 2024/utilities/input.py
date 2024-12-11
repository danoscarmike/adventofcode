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


# read rows of integers from a file into a list of lists
def read_rows_from_file(file_path: str, int: bool = True) -> list:
    path = Path(BASE_PATH + file_path)
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            if int:
                rows.append(list(map(int, line.split())))
            else:
                rows.append(line.strip())

    return rows
