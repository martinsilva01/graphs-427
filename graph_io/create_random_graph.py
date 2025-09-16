import networkx as nx
import random
import math
from itertools import combinations

def create_random_graph(n: int, c: float):
    n = int(n)
    c = float(c)
    p = min(1.0, ( c * math.log(n) ) / n)
    G = nx.Graph()
    for i in range(0, n):
        G.add_node(str(i))

    for a, b in combinations(range(n), 2):
        if random.random() < p:
            G.add_edge(str(a), str(b))

    return G

