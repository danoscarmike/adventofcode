from helpers.input import int_array_from_list


def part1(data):
    for i in range(0, len(data)):
        a = data[i]
        for j in range(i + 1, len(data)):
            b = data[j]
            if a + b == 2020:
                return a * b
    else:
        return -1


def part2(data):
    for i in range(0, len(data)):
        a = data[i]
        for j in range(i + 1, len(data)):
            b = data[j]
            for k in range(j + 1, len(data)):
                c = data[k]
                if a + b + c == 2020:
                    return a * b * c
    else:
        return -1


if __name__ == "__main__":
    data = int_array_from_list("1.txt")

    product2 = part1(data)
    print(product2)

    product3 = part2(data)
    print(product3)
