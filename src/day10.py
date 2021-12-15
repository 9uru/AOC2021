'''
Solution for day 10
Author: 9uru
12/10/2021
'''
from typing import List, Tuple
import statistics

def calculate_closing_cost(stack: List[str]):
    '''
    Check what remains open and calculate score
    for closing
    '''
    score = 0
    closing_score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    while stack:
        typ = stack.pop(-1)
        score = score * 5 + closing_score[typ]
    return score


def valid_syntax(input_str: str) -> Tuple[str, int]:
    '''
    Determine if the provided syntax is valid
    '''
    valid_opening = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>' : '<'
    }

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    closures = {')', ']', '}', '>'}
    stack = []
    for typ in input_str:
        if typ not in closures:
            stack.append(typ)
        else:
            opening = stack.pop(-1)
            if valid_opening[typ] != opening:
                return "Invalid", points[typ]
    if stack:
        return "Incomplete", calculate_closing_cost(stack)
    return "Valid", None


def parse_input(syntax_filename: str) -> List[str]:
    '''
    Parse command file and get individual syntax strs
    '''
    with open(syntax_filename, 'r') as syntax_file:
        lines = syntax_file.readlines()

    syntaxes = [line.strip("\n") for line in lines]
    return syntaxes


def main(syntax_filename: str):
    '''
    parse file calculate points
    '''
    syntaxes = parse_input(syntax_filename)
    total_points = 0
    closing_scores = []
    for syntax in syntaxes:
        valid, points = valid_syntax(syntax)
        if valid == "Invalid":
            total_points += points
        elif valid == "Incomplete":
            closing_scores.append(points)

    print(total_points)
    print(statistics.median(closing_scores))

if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day10_input.txt"
    main(INPUT_FILENAME)
