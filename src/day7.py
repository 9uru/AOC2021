'''
Solution for day 7
Author: 9uru
12/8/2021
'''

from typing import List


def fuel_cost(val: int) -> int:
    '''
    calculate fuel such that
    nstead, each change of 1 step in horizontal position costs 1 more unit of fuel
    than the last: the first step costs 1, the second step costs 2, the third step
    costs 3, and so on.
    '''
    return (val * (val + 1))/ 2

def calc_fuel_bf(positions: List[int], fuel_scaling=False) -> int:
    '''
    Calculate min fuel required to bring
    make all positions same
    '''
    min_fuel = float("inf")
    # O(nlogn)
    positions = sorted(positions)
    # O(n^2)
    for pos1 in range(positions[0], positions[-1] + 1):
        total_fuel = 0
        for pos2 in positions:
            diff = abs(pos2 - pos1)
            if fuel_scaling:
                fuel = fuel_cost(diff)
            else:
                fuel = diff
            total_fuel += fuel
        min_fuel = min(min_fuel, total_fuel)
    return min_fuel


def calc_fuel_opt(positions: List[int]) -> int:
    '''
    Calculate min fuel using median
    '''
    # O(nlogn) sort
    positions = sorted(positions)
    num_pos = len(positions)
    if num_pos % 2 == 1:
        median_pos = (num_pos + 1) / 2
    else:
        median_pos = num_pos / 2
    median_val = positions[int(median_pos)]
    min_fuel = 0
    for pos in positions:
        min_fuel += abs(pos - median_val)
    return min_fuel

def parse_input(positions_filename: str) -> List[int]:
    '''
    Read positions
    '''
    with open(positions_filename, 'r') as positions_file:
        lines = positions_file.readlines()
    positions = []
    for line in lines:
        pos = [int(x) for x in line.strip("\n").split(",")]
        positions.extend(pos)
    return positions


def main(positions_filename: str):
    '''
    process file and calculate fuel
    '''
    positions = parse_input(positions_filename)
    # print(calc_fuel_opt(positions, fuel_scaling=True))
    print(calc_fuel_bf(positions, fuel_scaling=True))

if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day7_input.txt"
    main(INPUT_FILENAME)
