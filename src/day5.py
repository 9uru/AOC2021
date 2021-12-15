'''
Solution for day5
Author: 9uru
12/7/2021
Strategy: Maintain a dictionary of point tuples as key with counts as value
'''

from typing import List, Tuple


def format_line(line: str) -> Tuple[int]:
    '''
    takes a single line definition
    and converts to Tuple (p1x, p1y, p2x, p2y)
    '''
    line_formatted = line.strip("\n").split(" -> ")
    p1x, p1y = (int(val) for val in line_formatted[0].split(","))
    p2x, p2y = (int(val) for val in line_formatted[1].split(","))
    return p1x, p1y, p2x, p2y



def parse_input(lines_filename: str) -> List[Tuple[int]]:
    '''
    Parse every line input to a list of
    [(p1x1 p1y1 p1p2x p1p2y),(p2x1 p2y1 p2x2 p2y2),...]
    '''

    with open(lines_filename, 'r') as lines_file:
        lines = lines_file.readlines()

    line_tuples = [format_line(line) for line in lines]
    return line_tuples


def is_horizontal_vertical(line: Tuple[int]):
    '''
    given a line tuple check if its hor or vertical
    '''
    return line[0] == line[2] or line[1] == line[3]

def is_diagonal(line: Tuple[int]):
    '''
    check if given line is diagonal
    '''
    ydiff = line[3] - line[1]
    xdiff = line[2] - line[0]
    if xdiff != 0:
        return abs(ydiff/xdiff ) == 1
    return False


def get_ranges(line_tuple: Tuple[int]) -> Tuple[List[int]]:
    '''
    Adjust the ranges so it can be used in a loop
    '''
    p1x, p1y, p2x, p2y = line_tuple

    if p1x <= p2x:
        xrange = range(p1x, p2x + 1)
    else:
        xrange = range(p1x, p2x - 1, -1)

    if p1y <= p2y:
        yrange = range(p1y, p2y + 1)
    else:
        yrange = range(p1y, p2y - 1, -1)

    if p1x == p2x:
        xrange = [p1x] * len(yrange)

    if p1y == p2y:
        yrange = [p1y] * len(xrange)

    return list(xrange), list(yrange)


def populate_points(line_tuples: List[Tuple[int]], diagonal_allowed: bool) -> dict:
    '''
    Keep a dictionary of points with counts
    diagonal_allowed - whether to consider diagonal lines
    '''
    points = {}
    for line in line_tuples:
        diag = diagonal_allowed and is_diagonal(line)
        if not (diag or is_horizontal_vertical(line)):
            continue

        xrange, yrange = get_ranges(line)

        for pt_x, pt_y in zip(xrange, yrange):
            if (pt_x, pt_y) in points:
                points[(pt_x, pt_y)] += 1
            else:
                points[(pt_x, pt_y)] = 1

    return points

def main_phase1(lines_filename: str, diagonal_allowed=False):
    '''
    read a lines, populate points and count
    '''
    line_tuples = parse_input(lines_filename)
    points = populate_points(line_tuples, diagonal_allowed)
    # print({point: points[point] for point in points if points[point] >= 2})
    return sum((x >= 2 for x in points.values()))

if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day5_input.txt"
    print(main_phase1(INPUT_FILENAME, False))
    print(main_phase1(INPUT_FILENAME, True))
