import argparse
import networkx as nx
from cli import analyze, get_parser
from algorithms import multi_bfs, shortest_path
from graph_io import add_bfs_attributes, output
import matplotlib.pyplot as plt
from visualization import plot

parser = get_parser()
args = parser.parse_args()

G = None

if args.input_file:
    G = nx.read_gml(args.input_file)

elif args.create_random_graph:
    print('add functionality')

else:
    raise argparse.ArgumentTypeError('Input graph required from file or random graph.')

if args.multi_BFS:
    bfs_list = multi_bfs(G, args.multi_BFS)    

    if args.plot:
        for i, bfs_tuple in enumerate(bfs_list):
            graph, parent_dict = bfs_tuple
            plt.figure(i)
            plot(graph)

    if args.output_file:
        add_bfs_attributes(G, bfs_list)
        output(G, args.output_file)

elif args.analyze:
    analyze(G)

    if args.plot:
        plot(G)

    if args.output_file:
        output(G, args.output_file)




