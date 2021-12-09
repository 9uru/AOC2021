'''
Solution for day 6
Author: 9uru
12/8/2021
'''

from collections import Counter
from typing import List

from src.day5 import INPUT_FILENAME


class LanternPool:  # pylint: disable=too-few-public-methods
    '''
    Class with datastructure to handle lantern fish
    '''

    def __init__(self, fish_list: List[int]):
        '''
        Create lantern_fish_pool instance
        '''
        self.fish_pool = Counter(fish_list)

    def update_counts(self):
        '''
        update timer of each fish
        '''
        new_count = {}
        for count in self.fish_pool:
            if count > 0:
                new_count[count - 1]  = new_count.get(count - 1, 0) + self.fish_pool[count]
            else:
                new_count[6] = new_count.get(6, 0) + self.fish_pool[count]
                new_count[8] = new_count.get(8, 0) + self.fish_pool[count]
        self.fish_pool = new_count


def parse_input(fish_filename: str) -> List[int]:
    '''
    Given a txt file return a list of fish timers
    '''
    with open(fish_filename, 'r') as fish_file:  # pylint: disable=unspecified-encoding
        lines = fish_file.readlines()
    timer_list = []
    for line in lines:
        timers = [int(x) for x in line.strip("\n").split(",")]
        timer_list.extend(timers)
    return timer_list

def main(fish_filename: str, days: int):
    '''
    Parse input and update
    '''

    timer_list = parse_input(fish_filename)
    fish_pool = LanternPool(timer_list)
    for _ in range(days):
        fish_pool.update_counts()
    print(sum(fish_pool.fish_pool.values()))


if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day6_input.txt"
    main(INPUT_FILENAME, 256)
