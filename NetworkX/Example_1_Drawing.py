#graph types are provided as Python classes:
#Graph => This class implements an undirected graph. It ignores multiple edges between two nodes. It does allow self-loop edges between a node and itself.
#DiGraph => Directed graphs, that is, graphs with directed edges. Provides operations common to directed graphs, (a subclass of Graph).
#MultiGraph => A ﬂexible graph class that allows multiple undirected edges between pairs of nodes. The additional ﬂexibility leads to some degradation in performance, though usually not signiﬁcant.
#MultiDiGraph => A directed version of a MultiGraph.

#Empty graph-like objects are created with:
# >>> G=nx.Graph()
# >>> G=nx.DiGraph()
# >>> G=nx.MultiGraph()
# >>> G=nx.MultiDiGraph()


#import the networkx module 
import networkx as nx

#pylab combines pyplot with numpy into a single namespace.
import matplotlib.pyplot as plt

points_list = [(0,1), (1,5), (5,6), (5,4), (1,2), (2,3), (2,7), (2,8), (5,8)]
G=nx.Graph()
G.add_edges_from(points_list)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
plt.show()
