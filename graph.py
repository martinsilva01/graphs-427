import argparse
import networkx as nx
import re

def validFileName(str):
    file_name_array = str.split('.')
    if len(file_name_array) != 2:
        raise argparse.ArgumentTypeError('File name requires exactly one .gml extension.')
    if file_name_array[1] != "gml":
        raise argparse.ArgumentTypeError('File name must end in .gml.')
    if re.search(r'[^A-Za-z\d_-]', file_name_array[0]):
        raise argparse.ArgumentTypeError('File name must not contain non-alphanumeric characters.')
    return str 

parser = argparse.ArgumentParser(description='Python application that handles Erdős–Rényi random graph generation, analysis, transformation, and visualization.', formatter_class=argparse.RawTextHelpFormatter)

group_input = parser.add_mutually_exclusive_group(required=True)
group_input.add_argument("--input-file", type=validFileName, help='Reads a graph from the given .gml file and uses it for all subsequent operations.')
group_input.add_argument("--create-random-graph", nargs=2, metavar=('n', 'c'), help='Generates a new Erdős–Rényi graph with n nodes and edge probability p=(c⋅ln(n)/n). Overrides --input. Nodes must be labeled with strings ("0", "1", ..., "n-1").')

group_action = parser.add_mutually_exclusive_group(required=True)
group_action.add_argument("--multi_BFS", nargs='+', metavar=("a1"), help='Accepts one or more starting nodes and computes BFS trees from each, storing all shortest paths. Each BFS tree must be independently visualized and compared.')
group_action.add_argument("--analyze", action="store_true", 
                    help='''Performs additional structural analyses on the graph, including:

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
group_action.add_argument("--plot", action="store_true", 
                    help='''Visualizes the graph with:

    Highlighted shortest paths from each BFS root node;
    
    Distinct styling for isolated nodes;
    
    Optional visualization of individual connected components.''')
parser.add_argument("--output-file", type=validFileName, default="output_graph.gml", help='Saves the final graph, with all computed attributes (e.g., distances, parent nodes, component IDs), to the specified .gml file')

    

args = parser.parse_args()

G = None

if args.input_file:
    G = nx.read_gml(args.input_file)
    print(G.nodes)
    print(G.edges)

elif args.create_random_graph:
    print('add functionality')

else:
    raise argparse.ArgumentTypeError('Input graph required from file or random graph.')




