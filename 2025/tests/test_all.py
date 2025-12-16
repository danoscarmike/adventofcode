import sys
import unittest

sys.path.append("/Users/danielomeara/code/adventofcode/2025")
sys.path.append("/Users/danielomeara/code/adventofcode/2025/utilities")

import day1, day2
from input import read_rows_of_strings, read_line


class TestDay1(unittest.TestCase):
    rows = read_rows_of_strings("input/test_1.txt")

    def test_part_one(self):
        assert day1.part_one(self.rows) == 3

    def test_part_two(self):
        assert day1.part_two(self.rows) == 6


class TestDay2(unittest.TestCase):
    input = read_line("input/test_2.txt")
    ranges = [list(map(int, entry.split("-"))) for entry in input.split(",")]

    def test_part_one(self):
        assert day2.solve(self.ranges, day2.detect_dupe) == 1227775554

    def test_part_two(self):
        assert day2.solve(self.ranges, day2.detect_dupe_two) == 4174379265


if __name__ == "__main__":
    unittest.main()
