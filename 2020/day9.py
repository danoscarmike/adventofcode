from helpers.input import int_array_from_list


def part1(data, pre_size):
    for i in range(pre_size, len(data)):
        good = False
        for j in range(i - pre_size, i):
            for k in range(i - pre_size + 1, i):
                if data[i] == data[j] + data[k]:
                    good = True
        if not good:
            return data[i]


if __name__ == "__main__":
    data = int_array_from_list("9.txt")
    print(part1(data, 25))
