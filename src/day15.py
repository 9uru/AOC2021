'''
solution for day15
Author: 9uru
12/16/2021
'''

from typing import List
from heapq import heappop, heappush
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


def calculate_risk_dijkstra(arr: List[List[int]]) -> int:
    '''
    use Dijkstra to do a complete search
    '''
    visited = {}  # we will store tuple of indices and cost to get there

    num_rows = len(arr)
    num_cols = len(arr[0])
    unvisited = {}
    for i in range(num_rows):
        for j in range(num_cols):
            if i == 0 and j == 0:
                unvisited[(i, j)] = 0
            else:
                unvisited[(i, j)] = float("inf")

    queue = []
    heappush(queue, (0, (0, 0)))

    while True:
        # sorted_dists = sorted([(val, key) for key, val in unvisited.items()])
        curr = heappop(queue)
        cost, (row, col) = curr
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) != 1:
                    continue

                if 0 <= row + i < num_rows and 0 <= col + j < num_cols and \
                    (row + i, col + j) in unvisited:
                    tentative = cost + arr[row + i][col + j]
                    if tentative < unvisited[(row + i, col + j)]:
                        unvisited[(row + i, col + j)] = tentative
                        heappush(queue, (tentative, (row + i, col + j)))

        visited[(row, col)] = cost
        unvisited.pop((row, col), None)
        if row == num_rows - 1 and col == num_cols - 1:
            break

    return visited[(row, col)]



def main(risk_filename: str):
    '''
    main workflow
    '''
    arr = utils.parse_2darray(risk_filename)
    print(calculate_risk(arr))
    print(calculate_risk_dijkstra(arr))


    big_arr = replicate_arr(arr)
    print(calculate_risk(big_arr))
    print(calculate_risk_dijkstra(big_arr))

if __name__ == "__main__":
    main("inputs/day15_input.txt")
