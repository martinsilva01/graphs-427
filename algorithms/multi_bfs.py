import networkx as nx
from collections import deque 
from itertools import combinations 

def multi_bfs(graph: nx.Graph, node_list: list): 
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
    path = []
    while target != None:
        path.append(target)
        target = parent_dict[target]
    path.reverse()
    return path

