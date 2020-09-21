class Graph(object):
    """Graph class."""

    def __init__(self, graph_dict=None):
        """Initialize a constructor."""
        super().__init__()
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def list_vertices(self):
        """List all the available vertices."""
        return list(self.graph_dict.keys())

    def generate_edges(self):
        """Generate all the available edges."""
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({neighbour, vertex})
        return edges

    def add_vertex(self, vertex):
        """Add a new vertex(s)."""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            return vertex

    def add_edge(self, edge):
        """Add a new edge(s)."""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
        return edge


print(Graph({"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }).list_vertices())

print(Graph({"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }).generate_edges())

print(Graph({"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }).add_vertex("g"))

print(Graph({"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }).add_edge({"f", "g"}))
