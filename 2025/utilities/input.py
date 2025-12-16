def read_rows_of_strings(path: str) -> list:
    rows = []
    with open(path, "r") as f:
        for line in f.readlines():
            rows.append(line.strip())

    return rows


def read_line(path: str) -> str:
    with open(path, "r") as f:
        return f.readline().strip()
