import unittest

from day4 import part_one, part_two
from utilities.input import read_rows_from_file


class TestDay4(unittest.TestCase):
    grid = read_rows_from_file('test_4.txt', int=False)

    def test_part_one(self):
        assert part_one(self.grid, 'XMAS') == 18
    
    def test_part_two(self):
        assert part_two(self.grid) == 9
