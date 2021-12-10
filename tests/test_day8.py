'''
Tests for day8
Author: 9uru
12/9/2021
'''
import pytest
from src import day8

def test_count_easy():
    '''
    test accepted word count
    '''
    assert day8.count_easy ("fdgacbe cefdb cefbgd gcbe") == 2
    assert day8.count_easy("fcgedb cgb dgebacf gc") == 3
    assert day8.count_easy("efabcd cedba gadfec cb") == 1

def test_parse_input():
    '''
    test parsing of a words file
    '''
    input_strs, output_strs = day8.parse_input("inputs/day8_input_short.txt")
    assert len(input_strs) == 10
    assert len(output_strs) == 10
    assert output_strs[0] == "fdgacbe cefdb cefbgd gcbe"
    return input_strs, output_strs

def test_str_intersect():
    '''
    test str_intersect and count
    '''
    assert day8.str_intersect("brown", "bow") == 3
    assert day8.str_intersect("brown", "drown") == 4
    assert day8.str_intersect("black", "red") == 0

@pytest.fixture(name="codebook")
def test_decode_words_segment():
    '''
    Generate codebook from a sequence
    '''
    words = ["acedgfb", "cdfbe", "gcdfa", "fbcad",
        "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
    codebook = day8.decode_words_segment(words)
    # print(codebook)
    assert codebook == {
        0: "cagedb",
        1: "ab",
        2: "gcdfa",
        3: "fbcad",
        4: "eafb",
        5: "cdfbe",
        6: "cdfgeb",
        7: "dab",
        8: "acedgfb",
        9: "cefabd"
    }
    return codebook

def test_decode_word(codebook):
    '''
    test decoding a word
    '''
    assert day8.decode_word(codebook, "cdfbe") == 5
    assert day8.decode_word(codebook, "cdfeb") == 5

def test_decode_str(codebook):
    '''
    test decoding a string
    '''
    assert day8.decode_str(codebook, "cdfeb fcadb cdfeb cdbaf") == 5353
