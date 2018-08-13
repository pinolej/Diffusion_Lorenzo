import networkx as nx
import numpy as np

G=nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])

H = nx.path_graph(10)

G.add_edge(1,2)

G.number_of_nodes()
G.number_of_edges()
