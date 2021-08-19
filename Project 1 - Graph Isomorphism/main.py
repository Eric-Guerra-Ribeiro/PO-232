import networkx as nx
import matplotlib.pyplot as plt
import isomorphismtest

def draw_graphs(G, H):
    """
    Draws graphs G and H.

    :param G: Graph to be drawn.
    :type G: networkx.classes.graph.Graph.
    :param H: Graph to be drawn.
    :type H: networkx.classes.graph.Graph.
    """
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    subax2 = plt.subplot(122)
    nx.draw(H, with_labels=True, font_weight='bold')
    plt.show()


def print_isomorphic_test(G, H, print_labeling):
    """
    Prints the isomorphic test result.

    :param G:
    """
    if isomorphismtest.isomorphism_test(G, H, print_labeling):
        print("Graphs could be isomorphic.")
    else:
        print("Graphs are definitely not isomorphic.")


A = nx.Graph()
A.add_nodes_from([1,2 ,3, 4, 5])
A.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (3, 5), (4, 5)])
B = nx.Graph()
B.add_nodes_from("abcde")
B.add_edges_from([("a", "b"), ("a", "c"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
print_isomorphic_test(A, B, True)
draw_graphs(A, B)

C = nx.Graph()
C.add_nodes_from([1, 2, 3, 4, 5])
C.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])
D = nx.Graph()
D.add_nodes_from("abcdef")
D.add_edges_from([("a", "e"), ("a", "f"), ("b", "c"), ("b", "d"), ("c", "d"), ("e", "f")])
print_isomorphic_test(C, D, True)
draw_graphs(C, D)

E = nx.Graph()
E.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
E.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (5, 6), (5, 8), (6, 7), (7, 8)])
F = nx.Graph()
F.add_nodes_from("abcdefgh")
F.add_edges_from([("a", "b"), ("a", "d"), ("a", "e"), ("b", "c"), ("b", "f"), ("c", "d"), ("e", "f"), ("e", "h"), ("f", "g"), ("g", "h")])
print_isomorphic_test(E, F, True)
draw_graphs(E, F)
