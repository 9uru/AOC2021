'''
tests for day 12 solution
Author: 9uru
12/13/2021
'''
import json
import pytest
from src import day12, day10

@pytest.fixture(name="cave_graphs")
def test_cave_graph(day12_test, day12_test_small):
    '''
    Test creating class
    big caves and small caves
    '''
    cave_graph_small = day12.CaveGraph(day12_test_small)
    assert cave_graph_small.small_caves == {'b', 'start', 'end'}
    assert cave_graph_small.big_caves == {'A'}
    assert cave_graph_small.graph == {
        'start': {'A'},
        'A': {'b', 'end', 'start'},
        'b': {'A', 'end'},
        'end': {'b', 'A'}
    }
    cave_graph = day12.CaveGraph(day12_test)
    assert cave_graph.small_caves == {'b', 'c', 'd', 'start', 'end'}
    assert cave_graph.big_caves == {'A'}
    assert cave_graph.graph == {
        'start': {'A', 'b'},
        'A': {'c', 'b', 'end', 'start'},
        'b': {'A', 'd', 'end', 'start'},
        'c': {'A'},
        'd': {'b'},
        'end': {'A', 'b'}}
    return cave_graph_small, cave_graph

def test_calculate_paths(cave_graphs):
    '''
    Test calculation of paths
    '''
    cave_graph_small, cave_graph = cave_graphs
    # print(cave_graph.paths)
    assert len(cave_graph_small.paths['start-end']) == 3
    assert len(cave_graph.paths['b-end']) == 3
    assert len(cave_graph.paths['start-end']) == 10
    print(json.dumps(cave_graph.paths2['start-end'], indent=2))
    assert len(cave_graph.paths2['start-end']) == 36


def test_bigger():
    '''
    Test with bigger inputs
    '''
    connects = day10.parse_input("inputs/day12_input_short.txt")
    # # print(connects)
    cave_graph_big = day12.CaveGraph(connects)
    # print(cave_graph_big.graph)
    assert len(cave_graph_big.paths['start-end']) == 19
    # pass
    connects_bigger = day10.parse_input("inputs/day12_input_medium.txt")
    # # print(connects)
    cave_graph_bigger = day12.CaveGraph(connects_bigger)
    # print(cave_graph_bigger.graph)
    assert len(cave_graph_bigger.paths['start-end']) == 226
