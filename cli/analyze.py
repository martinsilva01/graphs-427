import networkx as nx
from algorithms import connected_components, find_cycle, isolated_nodes, density, average_shortest_path_length

def analyze(graph: nx.Graph):
    """ 
    Prints various algorithm results to terminal. 
    Only prints average shortest path length if graph is connected.
    """
    print("Connected Components:")
    print(connected_components(graph))

    print("Cycle Detection:")
    print(find_cycle(graph))

    print("Isolated Nodes: ", end='')
    print(isolated_nodes(graph))
    print("Graph Density: ", end='')
    print(density(graph))
    if nx.is_connected(graph):
        print("Average Shortest Path Length: ", end='')
        print(average_shortest_path_length(graph))
