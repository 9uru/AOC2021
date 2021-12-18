'''
tests for day 15
Author: 9uru
12/16/2021
'''
import pytest
from src import day15, utils

@pytest.fixture(name="arr")
def test_calculate_risk():
    '''
    test risk calculation for a
    2d array of risks
    '''

    arr = [
        [1, 2, 3],
        [0, 4, 5],
        [7, 8, 2]
    ]

    assert day15.calculate_risk(arr) == 11
    assert day15.calculate_risk_dijkstra(arr) == 11
    arr_big = utils.parse_2darray("inputs/day15_input_short.txt")
    assert day15.calculate_risk(arr_big) == 40
    assert day15.calculate_risk_dijkstra(arr_big) == 40


    return arr_big

def test_replicate_arr(arr):
    '''
    test replication
    '''
    arr_small = [[1, 1], [1, 1]]
    assert day15.replicate_arr(arr_small) == [
        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
        [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
        [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
        [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
        [4, 4, 5, 5, 6, 6, 7, 7, 8 ,8],
        [4, 4, 5, 5, 6, 6, 7, 7, 8, 8],
        [5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
        [5, 5, 6, 6, 7, 7, 8, 8, 9, 9]]

    big_arr = day15.replicate_arr(arr)
    assert big_arr[-1][-1] == 9
