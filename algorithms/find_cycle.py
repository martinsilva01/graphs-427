import networkx as nx

def find_cycle(graph: nx.Graph):
    visited = set()
    parent = {}

    for node in graph.nodes:
        if node not in visited:
            stack = [node]
            parent[node] = None 
            
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph.neighbors(current):
                        if neighbor not in visited:
                            stack.append(neighbor)
                            parent[neighbor] = current 
                        elif parent[current] != neighbor: # isnt 2 node cycle
                            path = [current]
                            p = current
                            while p != neighbor and p is not None: #stop at full cycle
                                p = parent[p]
                                path.append(p) #[n, n-1, n-2, ... 1]
                            path.reverse() # [1, ... n-1, n]
                            return path
    return []
