import networkx as nx
from algorithms import connected_components, isolated_nodes
from cli import analyze

def add_bfs_attributes(graph, bfs_results):
"""
Adds multi_BFS-specific attributes to all graph nodes.

Keyword arguments:
graph -- The original NetworkX Graph object used in the multi_bfs function.
bfs_results -- A list of tuples containing each BFS graph and the parent dictionary created.
The return value of multi_bfs.
"""
    for i, (bfs_tree, parent_dict) in enumerate(bfs_results):
        for node, parent in parent_dict.items():
            graph.nodes[node][f'bfs_{i}_parent'] = parent if parent is not None else -1
            dist = 0
            current = node
            while parent_dict[current] is not None:
                dist += 1
                current = parent_dict[current]
            graph.nodes[node][f'bfs_{i}_distance'] = dist

def output(graph: nx.Graph, file_name: str):
"""
Writes a graph to a file, with additional attributes (connected components and isolated nodes).

Keyword arguments:
graph -- A NetworkX graph object
file_name -- A valid file name
"""
    for node in graph.nodes:
        graph.nodes[node]['component'] = 0
        graph.nodes[node]['isolated'] = False
    for i, component in enumerate(connected_components(graph)): 
        for node in component:
            graph.nodes[node]['component'] = i
    for node in isolated_nodes(graph):
        graph.nodes[node]['isolated'] = True

    nx.write_gml(graph, file_name)
