import sys
import unittest

sys.path.append("/Users/danielomeara/code/adventofcode/2024")
sys.path.append("/Users/danielomeara/code/adventofcode/2024/utilities")

import day1, day2, day3, day4, day5, day6
from input import (
    read_columns_from_file,
    read_rows_of_strings,
    read_rows_of_chars,
    read_rows_of_ints,
    read_file_to_string,
)


class TestDay1(unittest.TestCase):
    cols = read_columns_from_file("input/test_1.txt", 2)

    def test_part_one(self):
        assert day1.part_one(self.cols) == 11

    def test_part_two(self):
        assert day1.part_two(self.cols) == 31


class TestDay2(unittest.TestCase):
    reports = read_rows_of_ints("input/test_2.txt")

    def test_part_one(self):
        assert day2.part_one(self.reports) == 2

    def test_part_two(self):
        assert day2.part_two(self.reports) == 4


class TestDay3(unittest.TestCase):
    memory_1 = read_file_to_string("input/test_3.txt")
    memory_2 = read_file_to_string("input/test_3_2.txt")

    def test_part_one(self):
        assert day3.part_one(self.memory_1) == 161

    def test_part_two(self):
        assert day3.part_two(self.memory_2) == 48


class TestDay4(unittest.TestCase):
    grid = read_rows_of_strings("input/test_4.txt")

    def test_part_one(self):
        assert day4.part_one(self.grid, "XMAS") == 18

    def test_part_two(self):
        assert day4.part_two(self.grid) == 9


class TestDay5(unittest.TestCase):
    rules, updates = day5.read_input("input/test_5.txt")
    good_updates, bad_updates = day5.triage_updates(rules, updates)

    def test_part_one(self):
        assert day5.part_one(self.good_updates) == 143

    def test_part_two(self):
        assert day5.part_two(self.rules, self.bad_updates) == 123


class TestDay6(unittest.TestCase):
    grid = read_rows_of_chars("input/test_6.txt")

    def test_part_one(self):
        assert day6.part_one(self.grid) == 41

    def test_part_two(self):
        assert day6.part_two(self.grid) == 6
