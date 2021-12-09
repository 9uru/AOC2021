'''
tests for day 6 solution
Author: 9uru
12/8/2021
'''

import pytest
from src import day6

@pytest.fixture(name="pool")
def test_lantern_fish_pool():
    '''
    test class creation
    '''
    lantern_pool = day6.LanternPool([3, 4, 3, 1, 2])
    assert isinstance(lantern_pool, day6.LanternPool)
    assert lantern_pool.fish_pool == {4: 1, 3: 2, 2: 1, 1: 1}
    return lantern_pool


def test_update_counts(pool):
    '''
    test update of counts
    '''
    pool.update_counts()
    assert pool.fish_pool == {3: 1, 2: 2, 1: 1, 0: 1}
    pool.update_counts()
    assert pool.fish_pool == {1: 2, 2: 1, 6: 1, 0: 1, 8: 1}

def test_update_ndays(pool):
    '''
    lets check number of fish after n days in example
    '''
    for _ in range(18):
        pool.update_counts()
    assert sum(pool.fish_pool.values()) == 26

    for _ in range(62):
        pool.update_counts()
    assert sum(pool.fish_pool.values()) == 5934

def test_parse_input():
    '''
    test input file parsing
    '''
    timers = day6.parse_input("inputs/day6_input.txt")
    assert isinstance(timers, list)
