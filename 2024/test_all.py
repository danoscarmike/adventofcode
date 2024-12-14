import unittest

import day4, day5, day6
from utilities.input import read_rows_of_strings, read_rows_of_chars


class TestDay4(unittest.TestCase):
    grid = read_rows_of_strings('test_4.txt')

    def test_part_one(self):
        assert day4.part_one(self.grid, 'XMAS') == 18
    
    def test_part_two(self):
        assert day4.part_two(self.grid) == 9


class TestDay5(unittest.TestCase):
    rules, updates = day5.read_input('test_5.txt')
    good_updates, bad_updates = day5.triage_updates(rules, updates)

    def test_part_one(self):
        assert day5.part_one(self.good_updates) == 143
    
    def test_part_two(self):
        assert day5.part_two(self.rules, self.bad_updates) == 123



class TestDay6(unittest.TestCase):
    grid = read_rows_of_chars('test_6.txt')

    def test_part_one(self):
        assert day6.part_one(self.grid) == 41
    
    def test_part_two(self):
        assert day6.part_two(self.grid) == 6

