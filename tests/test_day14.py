'''
Tests for day14
Author: 9uru
12/15/2021
'''
import pytest
from src import day14, utils

@pytest.fixture(name="poly")
def test_read_insertion_rules():
    '''
    Test reading of insertion rules
    '''
    rules_strings = utils.parse_strings("inputs/day14_input_short.txt")
    poly = day14.Polymer(rules_strings, "NNCB")
    assert poly.rules_dict["BH"] == "H"
    return poly

def test_update(poly):
    '''
    test updating polymer template string
    '''

    for _ in range(10):
        poly.update()
        # print(poly.counts)

    max_count, min_count = poly.char_counts()
    assert max_count == 1749
    assert min_count == 161
