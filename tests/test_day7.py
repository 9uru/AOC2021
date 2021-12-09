'''
Tests for day 7
Author: 9uru
12/8/2021
'''

from time import perf_counter
from random import randint
from src import day7

def test_calc_fuel_bf():
    '''
    test brute force method
    '''
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert day7.calc_fuel_bf(positions) == 37

def test_calc_fuel_opt():
    '''
    test optimal method
    '''
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert day7.calc_fuel_opt(positions) == 37

def test_random_positions():
    '''
    Generate random sequences of increasing length
    and compare two methods
    '''
    lengths = [100, 1000, 10000]
    min_val = 0
    max_val = 1e5
    for length in lengths:
        positions = [randint(min_val, max_val) for _ in range(length)]

        bf_start = perf_counter()
        min_fuel_bf = day7.calc_fuel_bf(positions)
        bf_end = perf_counter()

        opt_start = perf_counter()
        min_fuel_opt = day7.calc_fuel_opt(positions)
        opt_end = perf_counter()

        assert min_fuel_bf == min_fuel_opt
        print("*" * 50)
        print("length:", length)
        print("bf time:", bf_end - bf_start)
        print("opt_time:", opt_end - opt_start)
        print("*" * 50)


def test_parse_input():
    '''
    test file parsing
    '''
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert day7.parse_input("inputs/day7_input_short.txt") == positions


def test_fuel_cost():
    '''
    check if fuel formula works
    '''
    val = 1
    assert day7.fuel_cost(val) == 1
    val = 2
    assert day7.fuel_cost(val) == 3
    val = 11
    assert day7.fuel_cost(val) == 66
