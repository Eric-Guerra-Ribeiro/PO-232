import networkx as nx
import matplotlib.pyplot as plt
import isomorphismtest

A = nx.Graph()
A.add_nodes_from([1,2 ,3, 4, 5])
A.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (3, 5), (4, 5)])
B = nx.Graph()
B.add_nodes_from("abcde")
B.add_edges_from([("a", "b"), ("a", "c"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
dictio = {tuple([]): 1}
isomorphismtest.weisfeiler_lehman(A, dictio)
isomorphismtest.weisfeiler_lehman(B, dictio)
subax1 = plt.subplot(121)
nx.draw(A, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw(B, with_labels=True, font_weight='bold')
plt.show()
