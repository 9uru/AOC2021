'''
Tests for day 5 solution
Author: 9uru
12/7/2021
'''

from src import day5

def test_format_line():
    '''
    test formatting a single line
    '''
    assert day5.format_line("1,2 -> 3,4") == (1, 2, 3, 4)


def test_parse_input():
    '''
    Test input parsing
    '''
    lines = day5.parse_input("inputs/day5_input_short.txt")
    assert len(lines) == 10
    assert lines[5][2] == 2

def test_is_horizontal_vertical():
    '''
    test check for horizontal or vertical
    '''
    assert not day5.is_horizontal_vertical((1, 2, 3, 4))
    assert day5.is_horizontal_vertical((1, 2, 3, 2))
    assert day5.is_horizontal_vertical((1, 2, 1, 8))

def test_is_diagonal():
    '''
    test if a line is diagonal
    '''
    assert day5.is_diagonal((1, 1, 3, 3))
    assert day5.is_diagonal((9, 7, 7, 9))
    assert not day5.is_diagonal((1, 2, 5, 2))

def test_get_ranges():
    '''
    test range creation
    '''
    assert day5.get_ranges((1, 1, 3, 3)) == ([1, 2 ,3], [1, 2, 3])
    assert day5.get_ranges((6, 4, 2, 0)) == ([6, 5, 4, 3, 2], [4, 3, 2, 1, 0])
    assert day5.get_ranges((1, 2, 1, 8)) == ([1] * 7, [2, 3, 4, 5, 6, 7, 8])
    assert day5.get_ranges((5, 0, 0, 5)) == ([5, 4, 3, 2, 1, 0],[0, 1, 2, 3, 4, 5])

def test_populate_points():
    '''
    Test population of points
    '''
    lines = [(1, 2, 5, 2), (5, 1, 5, 9), (0, 1, 2, 3), (6, 1, 4, 3)]
    points = day5.populate_points(lines, False)
    for point, count in points.items():
        if point == (5, 2):
            assert count == 2
        else:
            assert count == 1

    points = day5.populate_points(lines, True)
    for point, count in points.items():
        if point == (5, 2):
            assert count == 3
        elif point == (1, 2):
            assert count == 2
        else:
            assert count == 1

def test_main_phase1():
    '''
    test phase1 with short input
    '''
    assert day5.main_phase1("inputs/day5_input_short.txt") == 5
    assert day5.main_phase1("inputs/day5_input_short.txt", True) == 12
