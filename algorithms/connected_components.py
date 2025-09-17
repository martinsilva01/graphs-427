import networkx as nx

def connected_components(graph: nx.Graph):
""" 
Returns a list of lists denoting connected components of a graph 

Keyword arguments:
graph -- A NetworkX graph object
""" 

    components = []
    visited = set()

    for node in graph.nodes:

        if node not in visited:
            component = []
            stack = [node]
            
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    for neighbor in graph.neighbors(current):
                        if neighbor not in visited:
                            stack.append(neighbor)

            components.append(component)

    return components
