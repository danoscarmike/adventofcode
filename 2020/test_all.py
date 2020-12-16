import pytest
import day1, day2

data_day1 = [1721, 979, 366, 299, 675, 1456]
data_day2 = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_day1_part1():
    assert day1.part1(data_day1) == 1721 * 299  # 514579


def test_day1_part2():
    assert day1.part2(data_day1) == 979 * 366 * 675  # 241861950


def test_day2_part1():
    assert day2.part1(data_day2) == 2


def test_day2_part2():
    assert day2.part2(data_day2) == 1
