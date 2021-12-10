'''
Solution for day 8
Author: 9uru
12/9/2021
'''

from typing import List, Tuple

def count_easy(word_str: str) -> int:
    '''
    Given a string of output values
    count 1, 4, 7, 8
    1 has 2 character length word
    4 has 4 character length word
    7 has 3 character length word
    8 has 7 character length word
    '''
    output_words = word_str.split()
    accepted_lengths = {2, 4, 3, 7}
    valid_words = [word for word in output_words if len(word) in accepted_lengths]
    return len(valid_words)

def str_intersect(str1: str, str2: str):
    '''
    Give the intersection and count
    of two strings
    '''
    inter = set(str1).intersection(str2)
    return len(inter)


def decode_words_segment(word_list: List[str]) -> dict:  # pylint: disable=too-many-branches
    '''
    Given a set of words for a display
    return a dictionary with all the unique
    digits
    '''
    codebook = {}
    # first pass get the easy words
    for word in word_list:
        num = len(word)
        if num == 2:
            codebook[1] = word
        elif num == 4:
            codebook[4] = word
        elif num == 3:
            codebook[7] = word
        elif num == 7:
            codebook[8] = word

    completed = set(codebook.values())
    # print(completed, codebook)
    for word in word_list:
        num = len(word)
        if num in {1, 4, 3, 7} or word in completed:
            continue
        intersections = [
            str_intersect(codebook[1], word),
            str_intersect(codebook[4], word),
            str_intersect(codebook[7], word),
            str_intersect(codebook[8], word)]
        # print(word, intersections)
        if intersections == [2, 3, 3, 6]:
            codebook[0] = word
            completed.add(word)
        elif intersections == [1, 2, 2, 5]:
            codebook[2] = word
            completed.add(word)
        elif intersections == [2, 3, 3, 5]:
            codebook[3] = word
            completed.add(word)
        elif intersections == [1, 3, 2, 5]:
            codebook[5] = word
            completed.add(word)
        elif intersections == [1, 3, 2, 6]:
            codebook[6] = word
            completed.add(word)
        elif intersections == [2, 4, 3, 6]:
            codebook[9] = word
            completed.add(word)

    return codebook



def parse_input(words_filename: str) -> Tuple[List[str]]:
    '''
    Parses input into a list of input string
    and list of output strings
    '''
    with open(words_filename, 'r') as words_file:  # pylint: disable=unspecified-encoding
        lines = words_file.readlines()
    input_strs = []
    output_strs = []
    for line in lines:
        in_str, out_str = line.strip("\n").split("|")
        input_strs.append(in_str.strip())
        output_strs.append(out_str.strip())
    return input_strs, output_strs


def decode_word(codebook: dict, word: str) -> int:
    '''
    Given a codebook decode a word
    '''
    ret_val = None
    for key, value in codebook.items():
        if len(word) == len(value) and str_intersect(value, word) == len(word):
            ret_val = key
            break
    return ret_val

def decode_str(codebook: dict, in_str: str) -> int:
    '''
    given a string of 4 words produce 4 digit int
    '''
    words = [str(decode_word(codebook, word)) for word in in_str.split()]
    return int("".join(words))


def main(words_filename: str):
    '''
    Count digits
    '''
    input_strs, output_strs = parse_input(words_filename)
    phase1_count = 0
    for out_str in output_strs:
        phase1_count += count_easy(out_str)
    print("phase1:", phase1_count)

    value = 0
    for in_str, out_str in zip(input_strs, output_strs):
        # print(in_str)
        codebook = decode_words_segment(in_str.split())
        # print(codebook)
        value += decode_str(codebook, out_str)

    print("phase2:", value)


if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day8_input.txt"
    main(INPUT_FILENAME)
