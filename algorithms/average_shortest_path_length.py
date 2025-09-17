import networkx as nx
from collections import deque 
from itertools import combinations 

def average_shortest_path_length(graph: nx.Graph): 
    """
    Returns the average shortest path length for all node combinations of a graph.

    Keyword arguments:
    graph -- A NetworkX Graph object
    """
    shortest_path_lengths = []
    for node_a, node_b in combinations(graph.nodes, 2):
       visited = set()
       queue = deque([(node_a, 0)])
       
       while queue:
           current, dist = queue.popleft()
           if current == node_b:
               shortest_path_lengths.append(dist)
               break
           if current not in visited:
               visited.add(current)
               for neighbor in graph.neighbors(current):
                   if neighbor not in visited:
                       queue.append((neighbor, dist + 1))
    return sum(shortest_path_lengths) / len(shortest_path_lengths)

        
