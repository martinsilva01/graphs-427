import networkx as nx
from algorithms import isolated_nodes, connected_components 
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def plot(graph: nx.Graph):
    isolated_list = isolated_nodes(graph)
    connected_list = connected_components(graph)
    patch_list = []
    patch_list.append(Patch(facecolor="red", edgecolor='black', label = "Isolated Nodes"))
    color_map = ["black" for _ in graph.nodes]
    for i, node in enumerate(graph.nodes):
        if node in isolated_list:
            color_map[i] = "red"
    
    component_count = 1
    for component in connected_list:
        if len(component) < 2:
            continue
        color = "#{:06x}".format(random.randint(0xAAAAAA, 0xFFFFFF))
        label = 'Component '+ str(component_count)
        patch_list.append(Patch(facecolor=color, edgecolor='black', label=label))
        for node in component:
            idx = list(graph.nodes).index(node) 
            color_map[idx] = color
        component_count += 1
    
    nx.draw(graph, with_labels=True, node_color=color_map)
    plt.legend(handles=patch_list)
    plt.show()
