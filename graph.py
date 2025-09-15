import argparse

parser = argparse.ArgumentParser(
        description='Python application that handles Erdős–Rényi random graph generation, analysis, transformation, and visualization.',
        formatter_class=argparse.RawTextHelpFormatter
        )

parser.add_argument("--input-file", help='Reads a graph from the given .gml file and uses it for all subsequent operations.')
parser.add_argument("--create-random-graph", nargs=2, metavar=('n', 'c'), help='Generates a new Erdős–Rényi graph with n nodes and edge probability p=(c⋅ln(n)/n). Overrides --input. Nodes must be labeled with strings ("0", "1", ..., "n-1").')
parser.add_argument("--multi_BFS", nargs='+', metavar=("a1"), help='Accepts one or more starting nodes and computes BFS trees from each, storing all shortest paths. Each BFS tree must be independently visualized and compared.')
parser.add_argument("--analyze", action="store_true", help='''Performs additional structural analyses on the graph, including:

    Connected Components
    Counts how many distinct connected subgraphs exist.

    Cycle Detection
    Determines whether the graph contains any cycles.
    A cycle is a path that starts and ends at the same node, without repeating any edges or nodes (except the start/end).

    Isolated Nodes
    Identifies nodes that are not connected to any other node.

    Graph Density
    Computes how dense the graph is.
    Graph density measures how many edges exist in the graph compared to the maximum possible. 
    It is a number between 0 (very sparse) and 1 (fully connected).

    Average Shortest Path Length
    If the graph is connected, computes the average number of steps along the shortest paths for all pairs of nodes.''')
parser.add_argument("--plot", 
                    help='''Visualizes the graph with:

    Highlighted shortest paths from each BFS root node;
    
    Distinct styling for isolated nodes;
    
    Optional visualization of individual connected components.''')
parser.add_argument("--output-file", help='Saves the final graph, with all computed attributes (e.g., distances, parent nodes, component IDs), to the specified .gml file')


args = parser.parse_args()
