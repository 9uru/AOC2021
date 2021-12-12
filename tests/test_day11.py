'''
Tests for day 11 solution
Author: 9uru
12/11/2021
'''

import pytest
from src import day11, day9


@pytest.fixture(name="arr")
def test_parse_input():
    '''
    test if input parses
    '''
    arr = day9.parse_input("inputs/day11_input_short.txt")
    total_rows = len(arr)
    rows_per = int(total_rows / 3)
    grid = arr[:rows_per]
    step1 = arr[rows_per: 2 * rows_per]
    step2 = arr[2 * rows_per: 3 * rows_per]
    return grid, step1, step2

@pytest.fixture(name="octo_grid")
def test_octo_init(arr):
    '''
    test creation of class
    '''
    grid, _, _ = arr
    octo_grid = day11.OctoGrid(grid)
    assert octo_grid.arr == grid
    assert octo_grid.total_flashes == 0
    assert octo_grid.already_flashed == set()
    assert not octo_grid.flashes_each_step
    return octo_grid

def test_update(octo_grid, arr):
    '''
    test update
    '''
    _, step1, step2 = arr
    octo_grid.update()
    assert octo_grid.arr == step1
    octo_grid.update()
    assert octo_grid.arr == step2
    for _ in range(8):
        octo_grid.update()
    assert  sum(octo_grid.flashes_each_step) == 204
    for _ in range(90):
        octo_grid.update()
    assert  sum(octo_grid.flashes_each_step) == 1656
