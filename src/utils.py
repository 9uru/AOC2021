'''
Common utils
Author: 9uru
12/14/2021
'''

from typing import List

def parse_strings(input_filename: str) -> List[str]:
    '''
    Use to read as list of strings
    '''
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
    return [line.strip("\n") for line in lines]

def parse_2darray(input_filename: str, delimiter="") -> List[List[int]]:
    '''
    Use to read 2d array of ints
    '''
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
    arr = []
    for line in lines:
        line = line.strip("\n")
        if delimiter == "":
            arr.append([int(x) for x in line])
        else:
            arr.append([int(x) for x in line.split(delimiter)])
    return arr
