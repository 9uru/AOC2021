'''
day2 of advent of coding
Author: 9uru
12/5/2021
'''

from typing import List

def navigate_sub(directions: List[str]) -> int:
    '''
    Parse list of strings of directions
    calculate final hor and ver positions
    return their product
    '''
    hor = 0
    ver = 0
    for direction in directions:
        dir_list = direction.split()
        dir_cmd = dir_list[0]
        dir_val = int(dir_list[1])
        if dir_cmd.lower() == "forward":
            hor += dir_val
        elif dir_cmd.lower() == "up":
            ver -= dir_val
        else:
            ver += dir_val
    return hor, ver, hor * ver
