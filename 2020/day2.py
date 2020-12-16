import re

from helpers.input import str_array_from_list


def regex_helper(str):
    text_search = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)", str)
    one = int(text_search.group(1))
    two = int(text_search.group(2))
    three = text_search.group(3)
    four = text_search.group(4)

    return one, two, three, four


def part1(data):
    valid_pw_counter = 0

    for i in range(0, len(data)):
        min, max, char, pw = regex_helper(data[i])
        char_counter = 0
        for c in pw:
            if c == char:
                char_counter += 1

        if char_counter in range(min, max + 1):
            valid_pw_counter += 1

    return valid_pw_counter


def part2(data):
    valid_pw_counter = 0

    for i in range(0, len(data)):
        loc1, loc2, char, pw = regex_helper(data[i])
        if (pw[loc1 - 1] == char) != (pw[loc2 - 1] == char):
            valid_pw_counter += 1

    return valid_pw_counter


if __name__ == "__main__":
    data = str_array_from_list("2.txt")
    print(part1(data))
    print(part2(data))
