'''
test solution for day 3
Author: 9uru
12/5/2021
'''

from src import day3


def test_transpose_stream():
    '''
    test string list transposing
    '''
    bin_stream = ["0101", "1010", "1111"]
    assert day3.transpose_stream(bin_stream) == ["011", "101", "011", "101"]

def test_calculate_consumtion(day3_test):
    '''
    test calculation of consumption phase 1
    '''
    assert day3.calculate_consumption(day3_test) == (22, 9, 198)

def test_oxygen_rating(day3_test):
    '''
    test calculation of oxygen rating
    '''
    assert day3.calculate_oxygen_rating(day3_test) == 23

def test_co2_rating(day3_test):
    '''
    test calculation of oxygen rating
    '''
    assert day3.calculate_co2_rating(day3_test) == 10
