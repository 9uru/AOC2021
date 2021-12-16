'''
Solution for day 14
Author: 9uru
12/15/2021
'''
from collections import Counter
from typing import List, Tuple
from src import utils


class Polymer:
    '''
    Class to stroe rules for insertion
    and update
    '''

    def __init__(self, rule_strings: List[str], initial: str):
        '''
        Generate a rules dictionary
            key: a pair of polymers
            value: insert polymer
        '''
        self.rules_dict = {}
        for rule in rule_strings:
            pair, insert = rule.split(" -> ")
            self.rules_dict[pair] = insert

        self.counts = Counter()
        for i in range(len(initial) - 1):
            self.counts[initial[i: i + 2]] += 1
        self.initial = initial


    def update(self):
        '''
        update the polymer pair counts
        with insertion rules for 1 step
        set original count to 0
        and reassign count value to left and right pair
        '''
        old_counts = self.counts.copy()
        for pair, count in old_counts.items():
            if count > 0 and pair in self.rules_dict:
                val = self.rules_dict[pair]
                self.counts[pair] -= count
                pair_left = pair[0] + val
                pair_right = val + pair[1]
                self.counts[pair_left] += count
                self.counts[pair_right] += count

    def char_counts(self) -> Tuple[int]:
        '''
        return max and min counts of characters
        '''
        char_counts = Counter()
        # first char doesnt change
        # we will count only second characer of pairs
        # e.g. "NNCB" -> counts = {"NN": 1, "NC": 1, "CB": 1}
        # we need {"N": 2, "C": 1, "B": 1}
        char_counts[self.initial[0]] += 1
        for pair, count in self.counts.items():
            # print(pair)
            char_counts[pair[1]] += count
        counts = sorted(char_counts.values())
        # print(counts)
        return max(counts), min(counts)



def main(polymer_filename: str, initial: str, steps: int):
    '''
    Read rules update template
    for steps number of times
    '''
    rules_strings = utils.parse_strings(polymer_filename)
    poly = Polymer(rules_strings, initial)
    for i in range(steps):
        print("step", i)
        poly.update()
    max_count, min_count = poly.char_counts()
    print(max_count - min_count)


if __name__ == "__main__":
    main("inputs/day14_input.txt", "PFVKOBSHPSPOOOCOOHBP", 40)
