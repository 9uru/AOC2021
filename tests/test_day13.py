'''
unit test for day 13
Author: 9uru
12/14/2021
'''
import pytest
from src import day13, utils

@pytest.fixture(name="grids")
def test_generate_grid():
    '''
    test generating grid set
    '''
    arr = [
        [1, 0],
        [2, 1],
        [4, 2],
        [1, 4],
        [2, 5],
        [5, 6]]
    grid = day13.generate_grid(arr)
    assert len(grid) == 6
    assert (1, 0) in grid

    arr_big = utils.parse_2darray("inputs/day13_input_short.txt", delimiter=",")
    grid_big = day13.generate_grid(arr_big)
    assert len(grid_big) == 18
    assert (3, 0) in grid_big
    return grid, grid_big

def test_fold(grids):
    '''
    test applying fold
    '''
    grid, grid_big = grids
    grid_folded = day13.fold_grid(grid, axis='y', val=3)
    assert grid_folded == {(1, 0), (5, 0), (1, 2), (2, 1), (4, 2)}
    grid_folded2 = day13.fold_grid(grid_folded, axis='x', val=3)
    assert grid_folded2 == {(1, 0), (2, 1), (1, 2), (2, 2)}

    # test example
    grid_big_folded = day13.fold_grid(grid_big, axis='y', val=7)
    assert len(grid_big_folded) == 17

def test_parse_folds():
    '''
    test parsing folds data
    '''
    folds_vals = day13.parse_folds("inputs/day13_folds.txt")
    assert len(folds_vals) == 12
    assert folds_vals[-1] == ('y', 6)
