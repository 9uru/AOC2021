'''
tests for day 12 solution
Author: 9uru
12/13/2021
'''
import json
import pytest
from src import day12

@pytest.fixture(name="cave_graphs")
def test_cave_graph(day12_test, day12_test_small):
    '''
    Test creating class
    big caves and small caves
    '''
    cave_graph_small = day12.CaveGraph(day12_test_small)
    assert cave_graph_small.small_caves == {'b'}
    assert cave_graph_small.big_caves == {'A'}
    assert cave_graph_small.graph == {
        'start': {'A'},
        'A': {'b', 'end'},
        'b': {'A', 'end'}
    }
    cave_graph = day12.CaveGraph(day12_test)
    assert cave_graph.small_caves == {'b', 'c', 'd'}
    assert cave_graph.big_caves == {'A'}
    assert cave_graph.graph == {
        'start': {'A', 'b'},
        'A': {'c', 'b', 'end'},
        'b': {'A', 'd', 'end'},
        'c': {'A'},
        'd': {'b'}}
    return cave_graph_small, cave_graph

def test_calculate_paths(cave_graphs):
    '''
    Test calculation of paths
    '''
    cave_graph_small, cave_graph = cave_graphs
    assert len(cave_graph_small.paths['start-end']) == 3
    assert len(cave_graph.paths['b-end']) == 3
    assert len(cave_graph.paths['start-end']) == 10
