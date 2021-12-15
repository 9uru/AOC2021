'''
day 3 of AOC 2021
solution
Author: 9uru
12/5/2021
'''

from typing import List



def transpose_stream(bin_stream: List[str]) -> List[str]:
    '''
    Given a list of strings transpose the list so that
    first string contains first character of every string
    in original stream, second strign contains second char
    and so on.
    '''
    bit_len = len(bin_stream[0])
    transposed_stream = [""] * bit_len
    for i in range(bit_len):
        for bin_str in bin_stream: # not sure if efficient
            transposed_stream[i] += bin_str[i]

    return transposed_stream

def calculate_consumption(bin_stream: List[str]) -> int:
    '''
    Calculate gamma rate and epsilon rate
    from binary stream and calculate product
    as power consumption
    gamma_rate - formed most common bit in each position
    epsilon rate - formed by least common bit in each position
    '''
    # first transpose it (row first)
    transposed_stream = transpose_stream(bin_stream)
    gamma_rate = ""
    epsilon_rate = ""
    for transpose_seq in transposed_stream:
        one_count = transpose_seq.count("1")
        zero_count = transpose_seq.count("0")
        gamma_rate += str(int(one_count > zero_count))
        epsilon_rate += str(int(one_count < zero_count))
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate, epsilon_rate, gamma_rate * epsilon_rate

def calculate_oxygen_rating(bin_stream: List[str]) -> List[str]:
    '''
    Calculate oxygen rating
    To find oxygen generator rating, determine the most common value (0 or 1)
    in the current bit position, and keep only numbers with that bit in that
    position. If 0 and 1 are equally common, keep values with a 1 in the
    position being considered.
    Keep only numbers selected by the bit criteria for the type of rating value
    for which you are searching. Discard numbers which do not match the bit criteria.
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.
    '''
    curr_stream = bin_stream.copy()
    i = 0
    while len(curr_stream) > 1:

        transposed_stream = transpose_stream(curr_stream)
        transpose_seq = transposed_stream[i]
        one_count = transpose_seq.count("1")
        zero_count = transpose_seq.count("0")
        if one_count >= zero_count:
            curr_stream = [bin_str for bin_str in curr_stream if bin_str[i] == "1"]
        elif one_count < zero_count:
            curr_stream = [bin_str for bin_str in curr_stream if bin_str[i] == "0"]
        i += 1
    return int(curr_stream[0], 2)


def calculate_co2_rating(bin_stream: List[str]) -> List[str]:
    '''
    Calculate oxygen rating
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit
    position, and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 0 in the position being considered.
    Keep only numbers selected by the bit criteria for the type of rating value
    for which you are searching. Discard numbers which do not match the bit criteria.
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.
    '''
    curr_stream = bin_stream.copy()
    i = 0
    while len(curr_stream) > 1:

        transposed_stream = transpose_stream(curr_stream)
        transpose_seq = transposed_stream[i]
        one_count = transpose_seq.count("1")
        zero_count = transpose_seq.count("0")
        if one_count < zero_count:
            curr_stream = [bin_str for bin_str in curr_stream if bin_str[i] == "1"]
        elif zero_count <= one_count:
            curr_stream = [bin_str for bin_str in curr_stream if bin_str[i] == "0"]
        i += 1
    return int(curr_stream[0], 2)

def main():
    '''
    read file and calculate
    '''
    with open('inputs/day3_input.txt', 'r') as bin_stream_file:
        bin_stream = bin_stream_file.readlines()
    bin_stream = [x.strip("\n") for x in bin_stream]
    print(calculate_consumption(bin_stream))

    ox_rating = calculate_oxygen_rating(bin_stream)
    co2_rating = calculate_co2_rating(bin_stream)
    print(ox_rating, co2_rating, ox_rating * co2_rating)

if __name__ == '__main__':
    main()
