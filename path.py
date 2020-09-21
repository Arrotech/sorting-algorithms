def paths(g):

    print(g.keys())
    edges = []
    for vertex in g:
        for neighbour in g[vertex]:
            if {neighbour, vertex} not in edges:
                edges.append({neighbour, vertex})
    print(edges)


if __name__ == '__main__':
    g = {"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }
    paths(g)