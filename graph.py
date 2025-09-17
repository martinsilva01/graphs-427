import argparse
import networkx as nx
from networkx.algorithms.traversal import bfs_tree

from cli import analyze, get_parser
from algorithms import multi_bfs, shortest_path
from graph_io import add_bfs_attributes, output, create_random_graph
import matplotlib.pyplot as plt
from visualization import plot

# retrieve parser and its arguments
parser = get_parser()
args = parser.parse_args()

G = None

if args.create_random_graph:
    G = create_random_graph(*args.create_random_graph)

elif args.input_file:
    G = nx.read_gml(args.input_file)

else:
    raise argparse.ArgumentTypeError('Input graph required from file or random graph.')

if args.multi_BFS:
    bfs_list = multi_bfs(G, args.multi_BFS)

    bfs_tree_list = []
    for starting_node in args.multi_BFS:
        bfs_tree_list.append(bfs_tree(G, starting_node))

    if args.plot: #multi_BFS-specific plotter plots each BFS graph
        for i, bfs_tuple in enumerate(bfs_tree_list):
            #graph, parent_dict = bfs_tuple

            plt.figure(i)
            pos = nx.spring_layout(bfs_tuple)
            nx.draw(bfs_tuple, pos, with_labels=True)
            plt.savefig("bft_plot" + str(i) + ".png")
            #plot(graph)

    if args.output: #multi_BFS-specific output_file adds BFS attributes to main graph
        add_bfs_attributes(G, bfs_list)
        output(G, args.output)

else:   #non-multi_BFS-specific logic

    if args.plot:
        plot(G)

    if args.output:
        output(G, args.output)

if args.analyze:
    analyze(G)

    



