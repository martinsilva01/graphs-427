import networkx as nx
from collections import deque 
from itertools import combinations

from networkx.classes import Graph


def multi_bfs(graph: nx.Graph, node_list: list): 
    """
    Returns a list of breadth-first search graphs starting from each node.

    Keyword arguments:
    graph -- A NetworkX Graph object
    node_list -- A list of nodes inside graph
    """
    bfs_list = []
    for node in node_list:
        G = nx.Graph()
        visited = set()
        parent = {node: None}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                for neighbor in graph.neighbors(current):
                    if neighbor not in visited:
                            queue.append(neighbor)
                            parent[neighbor] = current
                            G.add_edge(current, neighbor)
        bfs_list.append((G, parent))
    return bfs_list

def shortest_path(target: str, parent_dict: dict): 
    """
    Returns the shortest path from the target node.

    Keyword arguments:
    target -- The target node
    parent_dict -- A dictionary of key-value pairs of values: { node: parent }.

    """
    path = []
    while target != None:
        path.append(target)
        target = parent_dict[target]
    path.reverse()
    return path

