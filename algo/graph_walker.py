"""
Graph Walker

Provides methods for traversing a graph.
"""


class GraphWalker:
    """The Graph Walker"""

    def __init__(self, graph):
        self.graph = graph

    def any_path(self, start_vertex, end_vertex):
        """Searches for any path connecting start and end vertices"""

        def search(vertices, accumulator):
            if not vertices:
                return accumulator
            if end_vertex in vertices:
                return accumulator + [end_vertex]
            next_vertices = [vertex for vertex
                             in matrix.get(vertices[0], [])
                             if vertex not in accumulator]

            return search(vertices[1:],
                          search(next_vertices,
                                 accumulator + [vertices[0]]))

        if not all([start_vertex, end_vertex]):
            return []

        matrix = self.graph.adjacency_matrix()
        return search(matrix.get(start_vertex, []), [])
