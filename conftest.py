'''
fixtures for test inputs
'''

import pytest

@pytest.fixture(scope='session')
def day1_test():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
