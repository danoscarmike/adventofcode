import sys
import unittest

sys.path.append("/Users/danielomeara/code/adventofcode/2025")
sys.path.append("/Users/danielomeara/code/adventofcode/2025/utilities")

import day1
from input import read_rows_of_strings


class TestDay1(unittest.TestCase):
    rows = read_rows_of_strings("input/test_1.txt")

    def test_part_one(self):
        assert day1.part_one(self.rows) == 3

    def test_part_two(self):
        assert day1.part_two(self.rows) == 6
