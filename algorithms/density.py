import networkx as nx

def density(graph: nx.Graph):
    v = len(graph.nodes)
    e = len(graph.edges)
    return e / ( v * ( v - 1 ) / 2)

