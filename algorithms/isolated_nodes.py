import networkx as nx

def isolated_nodes(graph: nx.Graph):
    filtered = {node: edges for node, edges in graph.adjacency() if not edges}
    return list(filtered.keys())
