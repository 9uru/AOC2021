'''
Test day1
Author: 9uru
12/5/2021
'''

from src import day1

def test_count_increment(day1_test):
    '''
    Test increment counter
    '''
    assert day1.count_increment(day1_test) == 7

def test_count_sliding_window_increment(day1_test):
    '''
    test sliding window sum increments
    '''
    assert day1.count_sliding_window_increment(day1_test) == 5
