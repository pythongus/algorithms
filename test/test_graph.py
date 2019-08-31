"""
Graph Unit Test Module
"""
import unittest
from algo.graph import Graph
from algo.node import Node


class TestGraph(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph()
        cls.graph.build("graph.dat")

    def setUp(self):
        self.graph = Graph()

    def test_is_graph(self):
        self.assertIsInstance(self.graph, Graph) 

    def test_build_empty_graph(self):
        self.graph.build("no_file.dat")
        self.assertEqual(self.graph.nnodes(), 0) 

    def test_build_graph(self):
        self.assertEqual(TestGraph.graph.nnodes(), 10) 

    def test_node_repr(self):
        node = Node(1)
        self.assertEqual(repr(node), "V1")

    def test_node_str(self):
        node = Node(1)
        self.assertEqual(str(node), "1: []")

    def test_chart_matrix(self):
        matrix = TestGraph.graph.chart_matrix()
        print()
        for row in matrix:
            print(" ".join(row))
        self.assertEqual(len(matrix), TestGraph.graph.nnodes() + 1)


if __name__ == "__main__":
    unittest.main()
