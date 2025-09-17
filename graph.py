import argparse
import networkx as nx
from cli import analyze, get_parser
from algorithms import multi_bfs, shortest_path
from graph_io import add_bfs_attributes, output, create_random_graph
import matplotlib.pyplot as plt
from visualization import plot

# retrieve parser and its arguments
parser = get_parser()
args = parser.parse_args()

G = None

if args.input_file:
    G = nx.read_gml(args.input_file)

elif args.create_random_graph:
    G = create_random_graph(*args.create_random_graph)

else:
    raise argparse.ArgumentTypeError('Input graph required from file or random graph.')

if args.multi_BFS:
    bfs_list = multi_bfs(G, args.multi_BFS)    

    if args.plot: #multi_BFS-specific plotter plots each BFS graph
        for i, bfs_tuple in enumerate(bfs_list):
            graph, parent_dict = bfs_tuple
            plt.figure(i)
            plot(graph)

    if args.output_file: #multi_BFS-specific output_file adds BFS attributes to main graph
        add_bfs_attributes(G, bfs_list)
        output(G, args.output_file)
    return

else:   #non-multi_BFS-specific logic 

    if args.analyze:    #multi_BFS and analyze are mutually exclusive, 
        analyze(G)      #but neither is required
    
    if args.plot:
        plot(G)
    
    if args.output_file:
        output(G, args.output_file)
    



