'''
tests for day9
Author: 9uru
12/10/2021
'''

import pytest
from src import day9

@pytest.fixture(name="arr")
def test_parse_input():
    '''
    test reading of file
    '''
    arr = day9.parse_input("inputs/day9_input_short.txt")
    assert len(arr) == 5
    assert len(arr[0]) == 10
    assert arr[2][3] == 6
    return arr

@pytest.fixture(name="min_loc")
def test_find_mins(arr):
    '''
    test min finding
    '''
    mins, locs = day9.find_mins(arr)
    assert mins == [1, 0, 5, 5]
    assert locs == [(0, 1), (0, 9), (2, 2), (4, 6)]
    return mins, locs

def test_calculate_risk(min_loc):
    '''
    test risk calc
    '''
    mins, _ = min_loc
    assert day9.calculate_risk(mins) == 15

def test_basin_size(arr):
    '''
    test basin size calculation
    '''
    assert day9.basin_size(arr, 0, 1) == 3
    assert day9.basin_size(arr, 0, 9) == 9
    assert day9.basin_size(arr, 2, 2) == 14
    assert day9.basin_size(arr, 4, 6) == 9
