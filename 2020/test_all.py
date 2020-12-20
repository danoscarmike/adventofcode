import day1, day2, day3, day4

from helpers.input import *

data1 = int_array_from_list("1.txt", test=True)
data2 = str_array_from_list("2.txt", True)
data3 = str_array_from_list("3.txt", True)
data4 = dict_array_from_file("4.txt", True)
data4b = dict_array_from_file("4b.txt", True)


def test_day1_part1():
    assert day1.part1(data1) == 1721 * 299  # 514579


def test_day1_part2():
    assert day1.part2(data1) == 979 * 366 * 675  # 241861950


def test_day2_part1():
    assert day2.part1(data2) == 2


def test_day2_part2():
    assert day2.part2(data2) == 1


def test_day3_part1():
    assert day3.part1(data3) == 7


def test_day3_part2():
    assert day3.part2(data3) == 336


def test_day4_part1():
    assert day4.part1(data4) == 2


def test_day4_valid_year():
    assert day4.is_valid_year("2003","byr") == False
    assert day4.is_valid_year("1919","byr") == False
    assert day4.is_valid_year("2000","byr")
    assert day4.is_valid_year("2a0b","byr") == False
    assert day4.is_valid_year("199","byr") == False
    assert day4.is_valid_year("20011","byr") == False


def test_day4_valid_ecl():
    assert day4.is_valid_ecl("amb")
    assert day4.is_valid_ecl("gry")
    assert day4.is_valid_ecl("oth")
    assert day4.is_valid_ecl("invalid") == False


def test_day4_valid_hgt():
    assert day4.is_valid_hgt("153cm")
    assert day4.is_valid_hgt("59in")
    assert day4.is_valid_hgt("cm") == False
    assert day4.is_valid_hgt("153co") == False
    assert day4.is_valid_hgt("149cm") == False
    assert day4.is_valid_hgt("58in") == False


def test_day4_valid_hcl():
    assert day4.is_valid_hcl("#ABC123")
    assert day4.is_valid_hcl("#1a2B3c")
    assert day4.is_valid_hcl("#12345G") == False
    assert day4.is_valid_hcl("#123ABCD") == False
    assert day4.is_valid_hcl("1a2B3c") == False


def test_day4_valid_pid():
    assert day4.is_valid_pid("000000000")
    assert day4.is_valid_pid("123456789")
    assert day4.is_valid_pid("0123456789") == False
    assert day4.is_valid_pid("1234567890") == False


def test_day4_part2():
    assert day4.part2(data4b) == 4