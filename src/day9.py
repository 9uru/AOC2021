'''
Solution for day9
Author: 9uru
12/10/2021
'''

from typing import List, Tuple
from heapq import heappush, heappop

def find_mins(arr: List[List[int]]) -> Tuple[List[int], List[Tuple[int]]]:
    '''
    Return a list of local mins in a 4-connected sense
    '''
    mins = []
    locs = []
    for row in range(len(arr)):  # pylint: disable=consider-using-enumerate
        for col in range(len(arr[0])):
            vals = []
            if row - 1 >= 0:
                vals.append(arr[row - 1][col])
            if col - 1 >= 0:
                vals.append(arr[row][col - 1])
            if row + 1 < len(arr):
                vals.append(arr[row + 1][col])
            if col + 1 < len(arr[0]):
                vals.append(arr[row][col + 1])
            curr = arr[row][col]
            if curr < min(vals):
                mins.append(curr)
                locs.append((row, col))
    return mins, locs

def parse_input(heights_filename: str) -> List[List[int]]:
    '''
    read file and parse and heights 2d array
    '''
    with open(heights_filename, 'r') as heights_file:
        lines = heights_file.readlines()
    arr = []
    for line in lines:
        vals = [int(x) for x in line.strip("\n")]
        arr.append(vals)
    return arr

def calculate_risk(mins: List[int]):
    '''
    calculate risk given mins
    '''
    return sum((1 + x for x in mins))


def basin_size(arr, row, col, visited=set()):  # pylint: disable=dangerous-default-value
    '''
    Use 4 pixels and grow the basin if appropriate
    '''
    visited.add((row, col))
    curr_val = arr[row][col]
    val = 0
    if row - 1 >= 0 and arr[row - 1][col] > curr_val and arr[row - 1][col] != 9:
        if (row - 1, col) not in visited:
            val += basin_size(arr, row - 1, col, visited)
    if row + 1 < len(arr) and arr[row + 1][col] > curr_val and arr[row + 1][col] != 9:
        if  (row + 1, col) not in visited:
            val += basin_size(arr, row + 1, col, visited)
    if col - 1 >= 0 and arr[row][col - 1] > curr_val and arr[row][col - 1] != 9:
        if (row, col - 1) not in visited:
            val += basin_size(arr, row, col - 1, visited)
    if col + 1 < len(arr[0]) and arr[row][col + 1] > curr_val and arr[row][col + 1] != 9:
        if (row, col + 1) not in visited:
            val += basin_size(arr, row, col + 1, visited)
    return 1 + val


def main(heights_filename: str):
    '''
    read file and calculate outputs
    '''
    arr = parse_input(heights_filename)
    mins, locs = find_mins(arr)
    print(calculate_risk(mins))

    # make a max heap
    basin_sizes = []
    for loc in locs:
        heappush(basin_sizes, -basin_size(arr, loc[0], loc[1]))

    result = 1
    for _ in range(3):
        result *= -1 * heappop(basin_sizes)
    print(result)


if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day9_input.txt"
    main(INPUT_FILENAME)
