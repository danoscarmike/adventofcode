from helpers.input import dict_array_from_file, str_array_from_list


def part1(data):
    total_yes = 0
    for group in data:
        group_set = set()
        for answers in group["answers"]:
            for c in answers:
                group_set.add(c)
        total_yes += len(group_set)
    return total_yes


def part2(data):
    total_yes = 0
    for group in data:
        group_size = len(group["answers"])
        if group_size == 1:
            total_yes += len(group["answers"][0])
        else:
            ans_count = {}
            for i in range(0, group_size):
                for c in group["answers"][i]:
                    if c in ans_count.keys():
                        ans_count[c] += 1
                    else:
                        ans_count[c] = 1
            yes = 0
            for ans_count in ans_count.values():
                if ans_count == group_size:
                    yes += 1
            total_yes += yes
    return total_yes


if __name__ == "__main__":
    data = dict_array_from_file("6.txt", parsing=6)
    print(part1(data))
    print(part2(data))
