import re

from helpers.input import dict_array_from_file


def has_required_fields(passport):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if required <= passport.keys():
        return True


def is_valid_year(year, type):
    type_vars = {
        "byr": {"min": 1920, "max": 2002},
        "iyr": {"min": 2010, "max": 2020},
        "eyr": {"min": 2020, "max": 2030},
    }
    if len(year) != 4:
        return False
    try:
        year_int = int(year)
        if year_int >= type_vars[type]["min"] and year_int <= type_vars[type]["max"]:
            return True
    except ValueError:
        pass
    return False


def is_valid_hgt(hgt):
    regex = r"^(\d+)(cm|in)$"
    search = re.search(regex, hgt)
    if search:
        value = int(search.group(1))
        if search.group(2) == "cm" and value >= 150 and value <= 193:
            return True
        if search.group(2) == "in" and value >= 59 and value <= 76:
            return True
    return False


def is_valid_hcl(hcl):
    regex = r"^(#[0-9a-fA-F]{6})$"
    search = re.search(regex, hcl)
    if search:
        return True
    return False


def is_valid_ecl(ecl):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in valid_ecl:
        return True
    return False


def is_valid_pid(pid):
    regex = r"^([0-9]{9})$"
    search = re.search(regex, pid)
    if search:
        return True
    return False


def part1(data):
    valid = 0
    for passport in data:
        if has_required_fields(passport):
            valid += 1
    return valid


def part2(data):
    valid = 0
    for passport in data:
        if has_required_fields(passport):
            if (
                is_valid_year(passport["byr"], "byr")
                and is_valid_year(passport["iyr"], "iyr")
                and is_valid_year(passport["eyr"], "eyr")
                and is_valid_hgt(passport["hgt"])
                and is_valid_hcl(passport["hcl"])
                and is_valid_ecl(passport["ecl"])
                and is_valid_pid(passport["pid"])
            ):
                valid += 1
    return valid


if __name__ == "__main__":
    data = dict_array_from_file("4.txt")
    print(part1(data))
    print(part2(data))
