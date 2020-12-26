import re

from helpers.input import str_array_from_list


def get_all_bags(data):
    all_bags = {}
    for rule in data:
        tokens = rule.split(" ")
        outer_bag = tokens[0] + " " + tokens[1]
        all_bags[outer_bag] = []
        pointer = 4
        while pointer < (len(tokens) - 2):
            try:
                bag_count = int(tokens[pointer])
                bag_color = tokens[pointer+1] + " " + tokens[pointer+2]
                all_bags[outer_bag].append((bag_color, bag_count))
            except:
                if tokens[pointer] == "no":
                    pass
            pointer += 4
    return all_bags


def unwrap_the_bag(data, color, valid_outers):
    regex = r"^(\b[\w\s]+\b)bags contain(.*)$"
    for rule in data:
        search = re.search(regex, rule)
        if search:
            outer_bag = search.group(1)
            if color in search.group(2):
                valid_outers.add(outer_bag)
                unwrap_the_bag(data, outer_bag, valid_outers)
    return valid_outers


def count_inner_bags(bags, color):
    total = 0
    if len(bags[color]) > 0:
        for bag in bags[color]:
            total += bag[1] + bag[1]*count_inner_bags(bags, bag[0])
    return total


def part1(data, color):
    valid_outers = set()
    valid_outers = unwrap_the_bag(data, color, valid_outers)
    return len(valid_outers)


def part2(data, color):
    all_bags = get_all_bags(data)
    return count_inner_bags(all_bags, color)


if __name__ == "__main__":
    data = str_array_from_list("7.txt")
    print(part1(data, "shiny gold"))
    print(part2(data, "shiny gold"))
