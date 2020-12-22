import re

from helpers.input import str_array_from_list


def unwrap_the_bag(data, color, valid_outers):
    regex = r"^([\w\s]+)bags contain(.*)$"
    for rule in data:
        search = re.search(regex, rule)
        if search:
            outer_bag = search.group(1)
            if color in search.group(2):
                valid_outers.add(outer_bag)
                unwrap_the_bag(data, outer_bag, valid_outers)
    return valid_outers


def part1(data, color):
    valid_outers = set()
    valid_outers = unwrap_the_bag(data, color, valid_outers)
    return len(valid_outers)


def part2(data):
    return -1


if __name__ == "__main__":
    data = str_array_from_list("7.txt")
    print(part1(data, "shiny gold"))
    print(part2(data))
