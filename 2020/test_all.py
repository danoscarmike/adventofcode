import day1, day2, day3

from helpers.input import *

data1 = int_array_from_list("1.txt", test=True)
data2 = str_array_from_list("2.txt", True)
data3 = str_array_from_list("3.txt", True)


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
