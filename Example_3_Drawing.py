import networkx as nx
import matplotlib.pyplot as plt

G = nx.dodecahedral_graph() #Return the Platonic Dodecahedral graph.
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
options = {'node_color': 'r','node_size': 100,'width': 3}
nx.draw_shell(G, nlist=shells, **options) #Draw networkx graph with shell layout   #shell layout => Position nodes in concentric circles.
