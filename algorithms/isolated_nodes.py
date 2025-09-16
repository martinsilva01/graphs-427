import networkx as nx

def isolated_nodes(graph: nx.Graph):
"""
Returns a list of isolated nodes of a NetworkX graph.

Keyword arguments:
graph -- A NetworkX graph object
"""
    filtered = {node: edges for node, edges in graph.adjacency() if not edges}
    return list(filtered.keys())
