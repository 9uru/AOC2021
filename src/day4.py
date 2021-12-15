'''
day4 of AOC 2021
Solution
Author: 9uru
12/6/2021
'''

from typing import List, Tuple

class Board:
    '''
    Board class that contains
    a board 2d array and an indicator
    array of the same size
    '''

    def __init__(self, board_strings: List[str]):
        '''
        constructed using list of strings representing
        the bingo board
        '''
        self.board = []
        self.indicator = []
        for line in board_strings:
            self.board.append([x.strip("\n") for x in line.split()])
            self.indicator.append([0, 0, 0, 0, 0])

    def update(self, val: str):
        '''
        check if board has val
        if yes update indicator
        '''
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == val:
                    self.indicator[i][j] = 1

    def check_victory(self):
        '''
        check if there is a row of 1s
        or a column of 1s in the indicator
        '''
        for i in range(5):
            if sum(self.indicator[i]) == 5:
                return True

            col = [self.indicator[j][i] for j in range(5)]
            if sum(col) == 5:
                return True
        return False

    def remaining_sum(self):
        '''
        Calculate sum of elements corresponding to 0
        '''
        rem_sum = 0
        for i in range(5):
            for j in range(5):
                if self.indicator[i][j] == 0:
                    rem_sum += int(self.board[i][j])
        return rem_sum


def parse_input(input_file: str) -> Tuple[List[str], List[Board]]:
    '''
    Parses input text for this problem
    Returns sequence of numbers : List[str]
    and individual boards : List[Board]
    '''

    with open(input_file, 'r') as bingo_file:
        lines = bingo_file.readlines()

    sequence = [x.strip("\n") for x in lines[0].split(",")]
    lines.pop(0)
    count = 0
    str_list = []
    board_list = []
    while lines:
        line = lines.pop(0)
        if line.strip("\n") == "":
            continue
        str_list.append(line)
        count += 1
        if count == 5:
            board = Board(str_list)
            board_list.append(board)

            str_list = []
            count = 0
    return sequence, board_list

def main_phase1():
    '''
    main flow
    '''
    sequence, boards = parse_input("inputs/day4_input.txt")
    for val in sequence:
        for board in boards:
            board.update(val)
            if board.check_victory():
                print(board.remaining_sum() * int(val))
                break
        else:
            continue
        break

def main_phase2():
    '''
    what is the last board to win
    '''
    sequence, boards = parse_input("inputs/day4_input.txt")
    boards_won = set()
    num_won = 0
    for val in sequence:
        for i, board in enumerate(boards):
            board.update(val)
            if board.check_victory():
                if i not in boards_won:
                    boards_won.add(i)
                    num_won += 1
                    if num_won == len(boards):
                        print(board.remaining_sum() * int(val))


if __name__ == "__main__":
    main_phase2()
