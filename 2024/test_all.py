import unittest

import day4, day5
from utilities.input import read_rows_from_file


class TestDay4(unittest.TestCase):
    grid = read_rows_from_file('test_4.txt', int=False)

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
        sorted_updates = [day5.sort_update(self.rules, update) for update in self.bad_updates]
        assert day5.part_two(sorted_updates) == 123
