from __future__ import print_function
import os
from itertools import chain
from collections import OrderedDict
from algo.node import Node


class Graph(object):
    """A graph object"""

    def __init__(self):
        self.matrix = OrderedDict()
        self.edges = []

    def _create_adjacency_matrix(self):

        def get_node(node):
            node_pool.setdefault(node, Node(node))
            return node_pool[node]

        node_pool = {}
        for start, end in self.edges:
            snode = get_node(start)
            enode = get_node(end)
            if snode in self.matrix:
                self.matrix[snode].add(enode)
            else:
                self.matrix.setdefault(snode, {enode})

    def _read_data(self, file_name):

        def valid_line(edge):
            edg = edge.strip()
            return (edg and not edg.startswith("#"))

        def edge_endpoints(edge):
            edg = edge.strip().split(",")
            return int(edg[0]), int(edg[1])

        with open(file_name) as data:
            self.edges = [edge_endpoints(edge) for edge in data.readlines()
                              if valid_line(edge)]

    def build(self, file_name):

        if not os.path.isfile(file_name):
            return self.nnodes()

        self._read_data(file_name)
        self._create_adjacency_matrix()

        return self.nnodes()
    
    def nnodes(self):
        """Convenience function that provides the number of vertices in the graph"""
        return len(self.matrix.keys())

    def adjacency_matrix(self):
        """Returns the adjacency matrix for the unlying graph"""
        return self.matrix

    def chart_matrix(self):
        """Returns the adjacency matrix as a list of lines to be ploted or printed"""
        matrix = [["." for _ in range(self.nnodes())] for _ in range(self.nnodes())]
        header = []
        for key, values in self.matrix.items():
            header.append(str(hash(key)))
            for value in values:
                matrix[hash(key) - 1][hash(value) - 1] = "X"
            matrix[hash(key) - 1].append(str(hash(key)))
        matrix.insert(0, header)

        return matrix
