'''
Solution for day 11
Author: @9uru
12/11/2021
'''

import sys
from typing import List
from src import day9

class OctoGrid:
    '''
    Class for Octopus grid
    '''
    def __init__(self, arr: List[List[int]]):
        '''
        Initialize octogrid with grid data
        '''
        self.arr = arr
        # counter of flashes in current step
        self.total_flashes = 0
        # track # of flashes each step
        self.flashes_each_step = []
        # track which locations are flashed this step
        self.already_flashed = set()
        self.num_rows = len(self.arr)
        self.num_cols = len(self.arr[0])

    def flash(self, row, col):
        '''
        call this to update if energy
        exceeds 9
        '''
        self.arr[row][col] = 0
        if (row, col) not in self.already_flashed:
            self.total_flashes += 1
            self.already_flashed.add((row, col))
            self.recursive_update(row, col)

    def valid(self, row, col):
        '''
        check if given row and col are within bounds
        '''
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return True
        return False

    def recursive_update(self, row, col):
        '''
        this will be called when there is a flash
        to update 8 connected neighbors
        if any of them flash call the same function
        '''
        for curr_x in [row - 1, row, row + 1]:
            for curr_y in [col -1, col, col + 1]:
                if (curr_x, curr_y) != (row, col):
                    if self.valid(curr_x, curr_y) and (curr_x, curr_y) not in self.already_flashed:
                        self.arr[curr_x][curr_y] += 1
                        if self.arr[curr_x][curr_y] > 9:
                            self.flash(curr_x, curr_y)

    def update(self):
        '''
        This is one step
        where all elements are incremented
        and flashed accordingly
        '''
        # reset flashed and total flashes
        self.already_flashed = set()
        self.total_flashes = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.arr[row][col] += 1

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.arr[row][col] > 9:
                    self.flash(row, col)
        self.flashes_each_step.append(self.total_flashes)

    def check_allzero(self) -> bool:
        '''
        if every element is 0 return True
        '''
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.arr[row][col] != 0:
                    return False
        return True


def main(grid_filename: str, part1: bool=True):
    '''
    main workflow read grid
    update N steps and check result
    '''
    arr = day9.parse_input(grid_filename)
    octo_grid = OctoGrid(arr)
    if part1:
        for _ in range(100):
            octo_grid.update()
        print(sum(octo_grid.flashes_each_step))
    else:
        count = 0
        while True:
            octo_grid.update()
            count += 1
            # check if everything flashed
            if octo_grid.check_allzero():
                print(count)
                break




if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day11_input.txt"
    if sys.argv[1] == "1":
        main(INPUT_FILENAME)
    else:
        main(INPUT_FILENAME, False)
