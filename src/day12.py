'''
Solution for day 12
Author: 9uru
12/13/2021
'''
from collections import defaultdict
from typing import List
from src import day10

class CaveGraph:
    '''
    CaveGraph class
    construct graph and find paths
    '''

    def add_to_graph(self,start: str, end: str):
        '''
        add to graph bidirectionally when applicable
        '''
        if end == "start":
            start, end = end, start

        self.graph[start].add(end)
        self.graph[end].add(start)
        for word in [start, end]:
            if word.islower():
                self.small_caves.add(word)
            else:
                self.big_caves.add(word)


    def __init__(self, connects: List[str]):
        '''
        Connects is a list of connections e.g A-B
        '''
        self.small_caves = set()
        self.big_caves = set()
        self.graph = defaultdict(set)
        self.keywords = {"start", "end"}
        # cache for storing paths
        self.paths = {}
        self.paths2 = {}

        for connect in connects:
            start, end = connect.split("-")
            self.add_to_graph(start, end)

        self.calculate_paths('start', 'end', set())
        self.calculate_paths2('start', 'end', set(), set())


    def calculate_paths(self, start='start', end='end', visited_small=None):
        '''
        Find all paths from start to end
        while going through small caves only once
        '''
        key = start + "-" + end
        if start in self.small_caves:
            visited_small.add(start)
        if start == end:
            return [end]

        paths = []

        if start in self.graph:
            for next_node in self.graph[start]:
                cur_visited = visited_small.copy()
                if next_node in self.small_caves:
                    if next_node in cur_visited:
                        continue
                    cur_visited.add(next_node)
                for next_path in self.calculate_paths(next_node, end, cur_visited):
                    paths.append(start + "-" + next_path)
        self.paths[key] = paths
        return paths

    def calculate_paths2(
            self, start='start', end='end', visited_once=None, visited_twice=None):
        '''
        Find all paths from start to end
        while going through small caves only once
        '''
        key = start + "-" + end
        if start in self.keywords:
            visited_once.add(start)
        if start == end:
            return [end]

        paths = []

        if start in self.graph:
            for next_node in self.graph[start]:
                # print(next_node)
                cur_visited_once = visited_once.copy()
                cur_visited_twice = visited_twice.copy()
                if next_node in self.keywords:
                    if next_node in cur_visited_once:
                        continue
                    cur_visited_once.add(next_node)
                elif next_node in self.small_caves:
                    if cur_visited_twice and next_node in cur_visited_once:
                        continue

                    if next_node in cur_visited_once:
                        cur_visited_twice.add(next_node)
                    else:
                        cur_visited_once.add(next_node)

                for next_path in self.calculate_paths2(
                    next_node, end, cur_visited_once, cur_visited_twice):
                    paths.append(start + "-" + next_path)
        self.paths2[key] = paths
        return paths



def main(paths_filename: str):
    '''
    main workflow
    '''
    connects = day10.parse_input(paths_filename)
    cave_graph = CaveGraph(connects)
    print(len(cave_graph.paths['start-end']))
    print(len(cave_graph.paths2['start-end']))

if __name__ == "__main__":
    INPUT_FILENAME = "inputs/day12_input.txt"
    main(INPUT_FILENAME)
