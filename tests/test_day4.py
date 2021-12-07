'''
Tests for day 4 solution
Author: 9uru
12/6/2021
'''
import pytest
from src import day4

@pytest.fixture(name="board")
def test_class_board():
    '''
    test class creation and methods
    '''
    board_str = ["14 21 17 24  4", "10 16 15  9 19",
        "18  8 23 26 20", "22 11 13  6  5", "2  0 12  3  7"]
    board = day4.Board(board_str)
    assert isinstance(board, day4.Board)
    return board

def test_update_victory(board):
    '''
    test updating of value
    '''
    for val in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]:
        board.update(str(val))
    assert not board.check_victory()
    board.update(str(24))
    assert board.check_victory()
    assert board.remaining_sum() == 188

def test_parse_input():
    '''
    test parsing input txt file for sequence and boards
    '''
    sequence, boards = day4.parse_input("inputs/day4_input.txt")
    assert sequence[0] == "28"
    assert sequence[-1] == "52"
    assert len(boards) == 100
    for board in boards:
        assert len(board.board) == 5
        assert len(board.board[0]) == 5
