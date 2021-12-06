'''
Day 1 problem
Author: 9uru
12/5/2021
'''
from typing import List

def count_increment(depths: List[int]) -> int:
    '''
    Count the number of times a depth value was
    more than previous
    Returns count (int)
    '''
    count = sum([depths[i] > depths[i - 1] for i in range(1, len(depths))])
    return count

def count_sliding_window_increment(depths: List[int], window_size=3) -> int:
    '''
    Count the number of times a depth value window sum
    was more than previous
    Returns count (int)
    '''
    count = 0
    for i in range(len(depths) - window_size + 1):

        if i == 0:
            curr_sum = sum(depths[i:i + window_size])
            prev_sum = curr_sum
        else:
            curr_sum -= depths[i - 1]
            curr_sum += depths[i + window_size - 1]
            count += curr_sum > prev_sum
            prev_sum = curr_sum
    return count


def main():
    '''
    read file and count
    '''
    with open('inputs/day1_input.txt', 'r') as depths_file:  # pylint: disable=unspecified-encoding
        depths = depths_file.readlines()
    depths = [int(x.strip("\n")) for x in depths]
    print(count_increment(depths))
    print(count_sliding_window_increment(depths))

if __name__ == '__main__':
    main()
