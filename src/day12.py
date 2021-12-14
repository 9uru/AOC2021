'''
Solution for day 12
Author: 9uru
12/13/2021
'''

from typing import List

class CaveGraph:
    '''
    CaveGraph class
    construct graph and find paths
    '''

    def add_to_graph(self,start: str, end: str):
        '''
        add to graph bidirectionally when applicable
        '''
        if start in self.graph:
            self.graph[start].add(end)
        else:
            self.graph[start] = {end}

        if start != "start" and end != "end":
            if end in self.graph:
                self.graph[end].add(start)
            else:
                self.graph[end] = {start}

        keywords = {"start", "end"}
        for word in [start, end]:
            if word not in keywords:
                if word.lower() == word:
                    self.small_caves.add(word)
                else:
                    self.big_caves.add(word)


    def __init__(self, connects: List[str]):
        '''
        Connects is a list of connections e.g A-B
        '''
        self.small_caves = set()
        self.big_caves = set()
        self.graph = {}
        # cache for storing paths
        self.paths = {}

        for connect in connects:
            start, end = connect.split("-")
            self.add_to_graph(start, end)

        self.calculate_paths()

    def calculate_paths(self, start='start', end='end', visited_small=set()):
        '''
        Find all paths from start to end
        while going through small caves only once
        '''
        key = start + "-" + end
        if start == end:
            return [end]

        paths = []

        if start in self.graph:
            for next_node in self.graph[start]:
                cur_visited = visited_small.copy()

                if next_node in self.small_caves:
                    if next_node in visited_small:
                        continue
                    else:
                        cur_visited.add(next_node)
                for next_path in self.calculate_paths(next_node, end, cur_visited):
                    paths.append(start + "-" + next_path)
        self.paths[key] = paths
        return paths
