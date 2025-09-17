import networkx as nx

def density(graph: nx.Graph):
    """
    Returns the density of a given NetworkX graph.

    Keyword arguments:
    graph -- A NetworkX Graph object
    """
    v = len(graph.nodes)
    e = len(graph.edges)
    return e / ( v * ( v - 1 ) / 2)

