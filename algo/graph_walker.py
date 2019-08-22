from algo.graph import Graph


class GraphWalker:

    def __init__(self, graph):
        self.graph = graph

    def any_path(self, start_vertex, end_vertex):
        """Searches for any path connecting start and end vertices"""

        def search(vertices, accumulator):
            if accumulator and accumulator[-1] == end_vertex:
                return accumulator
            elif not vertices:
                return []
            elif vertices[0] == end_vertex:
                return accumulator + [end_vertex]
            
            return search(list(vertices[1:]),
                          search(list(matrix.get(vertices[0], [])),
                                 accumulator + [vertices[0]]))

        if not all([start_vertex, end_vertex]):
            return []

        matrix = self.graph.adjacency_matrix()
        return search(list(matrix.get(start_vertex, [])), []) 
