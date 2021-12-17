'''
solution for day15
Author: 9uru
12/16/2021
'''

from typing import List
import numpy as np
from src import utils

def calculate_risk(arr: List[List[int]]) -> int:
    '''
    Given a 2d array of risks calculate
    min total risk of TL to BR
    '''

    rows = len(arr)
    cols = len(arr[0])

    # we will use DP and min costs in another matrix
    costs = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if i == rows - 1 and j == cols -1:
                costs[i][j] = arr[i][j]
            else:
                vals = []
                if i + 1 < rows:
                    vals.append(costs[i + 1][j])
                if j + 1 < cols:
                    vals.append(costs[i][j + 1])
                costs[i][j] = arr[i][j] + min(vals)
    # print(costs)
    return costs[0][0] - arr[0][0]

def inc_arr(arr: np.ndarray):
    '''
    increment and wrap after 9
    (IN PLACE)
    '''
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            arr[i, j] += 1
            if arr[i, j] > 9:
                arr[i, j] = 1



def replicate_arr(arr: List[List[int]]) -> List[List[int]]:
    '''
    repeat arr
    '''
    arr_np = np.array(arr)
    rows, cols = arr_np.shape
    new_arr = np.zeros((rows * 5, cols * 5), dtype=int)
    curr_arr = arr_np.copy()
    for i in range(5):
        curr_col = curr_arr.copy()
        for j in range(5):
            new_arr[i * rows: (i + 1) * rows, j * cols: (j + 1) * cols] = curr_col
            inc_arr(curr_col)
        inc_arr(curr_arr)
    # print(new_arr)
    return new_arr.tolist()

def main(risk_filename: str):
    '''
    main workflow
    '''
    arr = utils.parse_2darray(risk_filename)
    risk_part1 = calculate_risk(arr)
    print(risk_part1)

    big_arr = replicate_arr(arr)
    risk_part2 = calculate_risk(big_arr)
    print(risk_part2)

if __name__ == "__main__":
    main("inputs/day15_input.txt")
