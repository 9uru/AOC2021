'''
fixtures for test inputs
'''

import pytest

@pytest.fixture()
def day1_test():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

@pytest.fixture()
def day2_test():
    return ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

@pytest.fixture()
def day3_test():
    return ['00100', '11110', '10110', '10111', '10101', '01111',
        '00111', '11100', '10000', '11001', '00010', '01010']

@pytest.fixture()
def day12_test():
    return ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]

@pytest.fixture()
def day12_test_small():
    return ["start-A", "A-b", "A-end", "b-end"]
