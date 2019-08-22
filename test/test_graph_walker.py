"""
Graph Unit Test Module
"""
from __future__ import print_function
from algo.graph_walker import GraphWalker
from algo.graph import Graph
from algo.node import Node
import unittest


class TestGraphWalker(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        graph = Graph()
        graph.build("graph.dat")
        cls.walker = GraphWalker(graph)

    def test_graph_walker_instance(self):
        self.assertIsInstance(TestGraphWalker.walker, GraphWalker)

    def test_any_path_to_same(self):
        wlkr = TestGraphWalker.walker
        self.assertEqual(wlkr.any_path(None, None), [])

    def test_any_path_next_node(self):
        wlkr = TestGraphWalker.walker
        self.assertEqual(wlkr.any_path(Node(1), Node(2)), [Node(2)])

    def test_any_path_2_vertices(self):
        wlkr = TestGraphWalker.walker
        self.assertEqual(wlkr.any_path(Node(1), Node(3)), [Node(2), Node(3)])

    def test_any_path_8_vertices(self):
        wlkr = TestGraphWalker.walker
        self.assertEqual(wlkr.any_path(Node(1), Node(8)), [Node(i) for i in range(2, 9)])

    def test_any_path_1_10_vertices(self):
        wlkr = TestGraphWalker.walker
        self.assertEqual(wlkr.any_path(Node(1), Node(10)), [Node(i) for i in range(2, 11)])


if __name__ == "__main__":
    unittest.main()
