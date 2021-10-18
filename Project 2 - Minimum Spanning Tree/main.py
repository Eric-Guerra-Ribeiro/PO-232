import networkx as nx
import matplotlib.pyplot as plt
import mst

# YouTube Video link: 

def show_result(G, show_all=False):
    """
    Draws graphs G and its mininum spanning trees as well as displaying the overall cost.

    :param G: Graph to be drawn along with its minimum spanning trees.
    :type G: networkx.classes.graph.Graph.
    :param show_all: calculate and draw all minimum spanning trees.
    :type show_all: bool
    """
    if show_all:
        trees, cost = mst.jarnik_prim_all(G)
        print("Minimum cost of spanning tree: {}.".format(cost))
        print("{} minimum spanning trees found, may contain duplicates.".format(len(trees)))
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        for i in range(0, len(trees)):
            nx.draw(trees[i], with_labels=True, font_weight='bold')
            plt.show()
    else:
        trees, cost = mst.jarnik_prim_simple(G)
        print("Minimum cost of spanning tree: {}.".format(cost))
        subax1 = plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        subax2 = plt.subplot(122)
        nx.draw(trees[0], with_labels=True, font_weight='bold')
        plt.show()
    

A = nx.Graph()
A.add_nodes_from([1, 2, 3, 4, 5, 6])
A.add_weighted_edges_from([(1, 2, 1), (1, 4, 4), (1, 5, 3), (2, 4, 4), (2, 5, 2),
                          (3, 5, 4), (3, 6, 5), (4, 5, 4), (5, 6, 7)])
show_result(A, False)
B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4])
B.add_weighted_edges_from([(1, 2, 1), (1, 3, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 4, 1)])
show_result(B, False)
