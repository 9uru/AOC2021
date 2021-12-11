'''
test for day 10
Author: 9uru
12/10/2021
'''

from src import day10

def test_valid_syntax():
    '''
    Test if a sequence is valid
    '''
    assert day10.valid_syntax("([])") == ("Valid", None)
    assert day10.valid_syntax("[<>({}){}[([])<>]]") == ("Valid", None)
    assert day10.valid_syntax("{()()()>")  == ("Invalid", 25137)
    assert day10.valid_syntax("{([(<{}[<>[]}>{[]{[(<()>")  == ("Invalid", 1197)
    assert day10.valid_syntax("[{[{({}]{}}([{[{{{}}([]") == ("Invalid", 57)
    assert day10.valid_syntax("<{([{{}}[<[[[<>{}]]]>[]]") == ("Incomplete", 294)

def test_parse_input():
    '''
    test parsing of input
    '''
    syntaxes = day10.parse_input("inputs/day10_input_short.txt")
    assert len(syntaxes) == 10
    assert syntaxes[3] == "(((({<>}<{<{<>}{[]{[]{}"

def test_calculate_clost():
    '''
    calculate closing cost of an incomplete string
    '''
    assert day10.calculate_closing_cost(list("<{([")) == 294
