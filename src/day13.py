'''
Solution for day13
Author: 9uru
12/14/2021
'''

from typing import List, Tuple
from src import utils

def generate_grid(arr: List[List[int]]) -> set:
    '''
    Generate a grid
    '''
    grid = set()
    for point in arr:
        grid.add((point[0], point[1]))
    return grid

def fold_grid(grid: set, axis: str, val: int) -> set:
    '''
    fold a grid along axis
    x: right to left
    y: bottom to top
    val: axis value around which to fold
    return grid_folded - set
    '''
    index = 0 if axis == "x" else 1
    folded_grid = set()
    for point in grid:
        curr = point[index]
        new  = list(point)
        if curr > val:
            new[index] = 2 * val - curr
        folded_grid.add(tuple(new))
    return folded_grid

def parse_folds(folds_filename: str) -> List[Tuple[str, int]]:
    '''
    split folds instructions
    to axis and value
    '''
    with open(folds_filename, 'r') as folds_file:
        lines = folds_file.readlines()
    folds_vals = []
    for line in lines:
        commands = line.strip("\n").split()
        axis, val = commands[2].split("=")
        folds_vals.append((axis, int(val)))
    return folds_vals

def main():
    '''
    parse input and count points after
    each fold
    '''

    arr = utils.parse_2darray("inputs/day13_input.txt", delimiter=",")
    grid = generate_grid(arr)
    folds_vals = parse_folds("inputs/day13_folds.txt")

    for axis, val in folds_vals:
        grid_folded = fold_grid(grid, axis, val)
        print(len(grid_folded))
        grid = grid_folded

    # print final grid
    max_x = 0
    max_y = 0
    for point in grid:
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])
    for j in range(max_y + 1):
        disp_str = ""
        for i in range(max_x + 1):
            if (i, j) in grid:
                disp_str += "x"
            else:
                disp_str += " "
        print(disp_str)




if __name__ == "__main__":
    main()
