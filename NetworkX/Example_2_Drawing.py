import networkx as nx
import matplotlib.pyplot as plt

G=nx.cubical_graph() #Return the 3-regular Platonic Cubical graph.
plt.subplot(121) #subplot(nrows, ncols, index)
nx.draw(G) # default spring_layout

plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
