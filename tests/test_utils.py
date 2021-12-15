'''
Tests for utils
Author: 9uru
12/14/2021
'''

from src import utils

def test_parse_strings():
    '''
    test parse strings
    '''
    strings = utils.parse_strings("inputs/day5_input_short.txt")
    assert len(strings) == 10

def test_parse_2darray():
    '''
    parse array
    '''
    arr = utils.parse_2darray("inputs/day9_input_short.txt")
    assert len(arr) == 5
    assert len(arr[0]) == 10

    arr = utils.parse_2darray("inputs/day6_input_short.txt", delimiter=",")
    assert arr == [[3, 4, 3, 1, 2]]
