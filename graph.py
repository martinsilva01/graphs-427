import argparse
import networkx as nx
from cli import analyze, get_parser
from algorithms import multi_bfs, shortest_path
import random
import matplotlib.pyplot as plt

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
            nx.draw(graph, with_labels=True)
        plt.show()
    
elif args.analyze:
    analyze(G)

    if args.plot:
        plot(G)





