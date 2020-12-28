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


def part2(data, target):
    sum = 0
    summands = []
    i = 0
    while i < len(data):
        if data[i] > target:
            sum = 0
            summands = []
            i += 1
        elif sum + data[i] > target:
            sum += data[i]
            summands.append(data[i])
            while sum > target:
                sum -= summands[0]
                summands.pop(0)
            i += 1
        elif sum + data[i] < target:
            sum += data[i]
            summands.append(data[i])
            i += 1
        if sum == target:
            return max(summands) + min(summands)
    return -1


if __name__ == "__main__":
    data = int_array_from_list("9.txt")
    target = part1(data, 25)
    print(target)
    print(part2(data, target))
