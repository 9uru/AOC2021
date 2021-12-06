'''
fixtures for test inputs
'''

import pytest

@pytest.fixture(scope='session')
def day1_test():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

@pytest.fixture(scope='session')
def day2_test():
    return ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
