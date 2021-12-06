'''
test day2 solutions
Author: 9uru
12/5/2021
'''

from src import day2

def test_navigate_sub(day2_test):
    '''
    test navigate sub final hor and ver positions
    '''
    hor, ver, prod =  day2.navigate_sub(day2_test)
    assert (hor, ver, prod)  == (15, 10, 150)

def test_navigate_sub_aim(day2_test):
    '''
    test navigate sub final hor and ver positions
    '''
    hor, ver, prod =  day2.navigate_sub_aim(day2_test)
    assert (hor, ver, prod)  == (15, 60, 900)
