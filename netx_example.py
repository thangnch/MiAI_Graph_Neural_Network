import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(
    [
        (0, {"color" : "blue", "size": 250}),
        (1, {"color" : "red", "size": 50}),
        (2, {"color" : "yellow", "size": 150}),
        (3, {"color" : "orange", "size": 100})
    ]
)

G.add_edges_from(
    [
        (0,1),
        (1,2),
        (1,0),
        (1,3),
        (2,3),
        (3,0)
    ]
)
for node in G.nodes(data=True):
    print(node)

node_colors = nx.get_node_attributes(G, "color").values()
colors = list(node_colors)
node_sizes = nx.get_node_attributes(G, "size").values()
sizes = list(node_sizes)
nx.draw(G, with_labels=True, node_color=colors, node_size=sizes)
plt.waitforbuttonpress()