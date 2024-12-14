import re

from collections import defaultdict

from utilities.input import read_rows_of_strings


def read_input(file_name: str) -> tuple:
    rules = []
    updates = []
    input = read_rows_of_strings(file_name)
    for line in input:
        pattern = r"(\d+)\|(\d+)"
        match = re.search(pattern, line)
        if match:
            rules.append((int(match.group(1)), int(match.group(2))))
        elif line == "":
            pass
        else:
            updates.append([int(x) for x in line.split(",")])

    rule_dict = defaultdict(set)
    for rule in rules:
        rule_dict[rule[0]].add(rule[1])

    return rule_dict, updates


def is_valid_page_order(rule_dict: defaultdict, update: list) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rule_dict[update[i]]:
                return False

    return True


def triage_updates(rule_dict: defaultdict, updates: list) -> tuple:
    good_updates = []
    bad_updates = []

    for update in updates:
        if is_valid_page_order(rule_dict, update):
            good_updates.append(update)
        else:
            bad_updates.append(update)

    return good_updates, bad_updates


def sort_update(rule_dict: defaultdict, update: list) -> list:
    if is_valid_page_order(rule_dict, update):
        return update

    sorted_update = update.copy()
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rule_dict[update[i]]:
                new_i = sorted_update.pop(j)
                sorted_update.insert(i, new_i)
                return sort_update(rule_dict, sorted_update)


def part_one(good_updates) -> int:
    total = 0

    for update in good_updates:
        total += update[len(update) // 2]

    return total


def part_two(rules, bad_updates) -> int:
    total = 0

    sorted_updates = [sort_update(rules, update) for update in bad_updates]

    for update in sorted_updates:
        total += update[len(update) // 2]

    return total


if __name__ == "__main__":
    rules, updates = read_input("input/5.txt")
    good_updates, bad_updates = triage_updates(rules, updates)
    print(f"Part One: {part_one(good_updates)}")
    print(f"Part Two: {part_two(rules, bad_updates)}")
