# read columns of integers from a file into a list of lists
def read_columns_from_file(path: str, cols) -> list:
    columns = [[] for i in range(cols)]
    with open(path, "r") as f:
        for line in f.readlines():
            for i in range(cols):
                columns[i].append(int(line.split()[i]))

    return columns


def read_file_to_string(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


# read rows as strings from a file into a list of lists
def read_rows_of_strings(path: str) -> list:
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(line.strip())

    return rows


# read rows of integers from a file into a list of lists
def read_rows_of_ints(path: str) -> list:
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(list(map(int, line.split())))

    return rows


# read rows of chars from a file into a list of lists
def read_rows_of_chars(path: str) -> list:
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(list(line))

    return rows
