import networkx as nx

def weisfeiler_lehman(G, compression):
    """
    Performs the Weisfeiler-Lehman Algorithm which colours a graphs vertices canonically.

    :param G: Graph which will be coloured.
    :type G: networkx.classes.graph.Graph.
    :param compression: Dicitionary used for the compressed label.
    :type compression: Dictionary.

    :return: Coloured graph G.
    :rtype: networkx.classes.graph.Graph.
    """


def isomorphism_test(G, H):
    """
    Performs a isomorphic test based on the coloring from the Weisfeiler-Lehman Algorithm.
    Cannot give a conclusive answer if the  graphs are isomorphic.
    If they pass the test, they still could be non-isomorphic.
    However, if it fails, they are definitely non-isomorphic.

    :param G: Graph G which we want to know if is isomorphic to H.
    :type G: networkx.classes.graph.Graph.
    :param H: Graph H which we want to know if is isomorphic to G.
    :type H: networkx.classes.graph.Graph.
    :return: True if the graphs could be isomorphic, False if they definitely are not.
    """